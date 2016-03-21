from settings import settings
from unittest.mock import patch
from requests_oauthlib import OAuth1Session
import debug
from base import Manager_base
from line import Manager_line

class Campaign():
	def __init__( self, **kargs ):
		self.name = kargs.get( 'name' )
		self.created_at = kargs.get( 'created_at' )
		self.end_time = kargs.get( 'end_time' )
		self.update_at = kargs.get( 'update_at' )
		self.account_id = kargs.get( 'account_id' )
		self.deleted = kargs.get( 'deleted' )
		self.pk = kargs.get( 'id' )
		self.pause = kargs.get( 'pause' )
		self.currency = kargs.get( 'currency' )
		self.total_budget_amount = kargs.get( 'total_budget_amount_local_micro' )
		self.daily_budget_amount = kargs.get( 'daily_budget_amount_local_micro|' )
		self.funding_instrument_id = kargs.get( 'funding_instrument_id' )
		self.start_time = kargs.get( 'start_time' )

	def create_line( self, bid_amount, product_type, placements, is_paused ):
		manager = Manager_line()
		return manager.create( self.account_id, self.pk, bid_amount, product_type, placements, is_paused )

	def __str__( self ):
		return "pk: {}\nname: {}".format( self.pk, self.name)

class Manager_campaign( Manager_base ):
	class Meta:
		debug_all_objects = debug.all_campaigns
		debug_one_objects = debug.one_campaigns
		model = Campaign
		url = settings[ 'url' ] + 'account/'

	def get_all( self, account_id ):
		return super().get_all( account_id, 'campaigns' )

	def get( self, account_id, pk ):
		return super().get( account_id, 'campaigns', pk )

	def create( self, account_id, start_time, funding_instrument_id, name,
		total_budget_amount, daily_budget_amount ):
		
		return super().create( account_id, 'campaing',
			account_id=account_id, start_time=start_time,
				funding_instrument_id=funding_instrument_id,
				name=name,
				total_budget_amount_local_micro=total_budget_amount,
				daily_budget_amount_local_micro=daily_budget_amount )
