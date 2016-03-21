from settings import settings
from unittest.mock import patch
from requests_oauthlib import OAuth1Session
import debug
from base import Manager_base
from target import Target

class Line():
	def __init__( self, **kargs ):

		self.bid_type = kargs.get( 'bid_type' )
		self.name = kargs.get( 'name' )
		self.placements= kargs.get( 'placements' )
		self.bid_amount = kargs.get( 'bid_amount_local_micro' )
		self.kind= kargs.get( 'product_type' )
		self.pk = kargs.get( 'id' )
		self.account_id = kargs.get( 'account_id' )

	def set_target_location( self, target ):
		manager = Manager_line_targeting()
		return manager.create( self.pk, self.account_id, 'LOCATION', target.value )

	def set_target_phrase( self, phrase ):
		manager = Manager_line_targeting()
		return manager.create( self.pk, self.account_id, 'PHRASE_KEYWORD', phrase )

	def set_paused( self, paused ):
		manager = Manager_line()
		return manager.update( self, paused )

	def __str__( self ):
		return "pk: {}\nname: {}".format( self.pk, self.name)

class Manager_line( Manager_base ):
	class Meta:
		#debug_all_objects = debug.all_line
		debug_one_objects = debug.one_line
		model = Line
		url = settings[ 'url' ] + 'accounts/'

	def get_all( self, account_id ):
		return super().get_all( account_id, 'line_items' )

	def get( self, account_id, pk ):
		return super().get( account_id, 'line_items', pk )

	def create( self, account_id, campaign_id, bid_amount, product_type,
		placements, is_paused):
		
		return super().create( account_id, 'line_items',
			campaign_id=campaign_id, bid_amount_local_micro=bid_amount,
			product_type=product_type, placements=placements,
			paused=is_paused )

	def update( self, line, paused ):
		
		return super().create( line.account_id, 'line_items', line.pk,
			paused=paused )

class Manager_line_targeting( Manager_base ):
	class Meta:
		debug_all_objects = debug.all_target
		debug_one_objects = debug.one_target
		model = Target
		url = settings[ 'url' ] + 'accounts/'

	def create( self, account_id, line_id, kind, value ):
		return super().create( account_id, 'targeting_criteria',
			line_item_id=line_id, targeting_type=kind,
			targeting_value=value )
