from settings import settings
from unittest.mock import patch
from requests_oauthlib import OAuth1Session
from base import Manager_base
import debug
from campaign import Manager_campaign

class Funding_instrument():
	def __init__( self, **kargs ):
		self.account_id = kargs[ 'account_id' ]
		self.cancelled = kargs[ 'cancelled' ]
		self.created_at = kargs[ 'created_at' ]
		self.credit_limit = kargs[ 'credit_limit_local_micro' ]
		self.pk = kargs[ 'id' ]
		self.kind = kargs[ 'type' ]
		self.start_time = kargs[ 'start_time' ]
	
	def start_campaing( self, start_time, name,
		total_budget_amount, daily_budget_amount ):

		manager = Manager_campaign()
		return manager.create( self.account_id, start_time, self.pk,
			name, total_budget_amount, daily_budget_amount )

	def __str__( self ):
		return "pk: {}\nkind: {}".format( self.pk, self.kind )


class Manager_funding_instrument( Manager_base ):
	class Meta:
		debug_all_objects = debug.all_instruments
		debug_one_objects = debug.one_instrument
		model = Funding_instrument
		url = settings[ 'url' ] + 'account/'

	def get_all( self, account_id ):
		return super().get_all( account_id, 'funding_instruments' )

	def get( self, account_id, pk ):
		return super().get( account_id, 'funding_instruments', pk )
