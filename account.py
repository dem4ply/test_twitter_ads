from base import Manager_base
from settings import settings
from unittest.mock import patch
from requests_oauthlib import OAuth1Session
from funding_instrument import ( Funding_instrument,
	Manager_funding_instrument )
import debug

class Account():
	
	def __init__( self, **kargs ):
		self.name = kargs[ 'name' ]
		self.timezone = kargs[ 'timezone' ]
		self.pk = kargs[ 'id' ]
		self.create_at = kargs[ 'created_at' ]
		self.approval_status = kargs[ 'approval_status' ]
		self.is_deleted = kargs[ 'deleted' ]

	def get_all_funding_instrument( self ):
		manager = Manager_funding_instrument()
		return manager.get_all( self.pk )

	def get_one_funding_instrument( self, pk ):
		manager = Manager_funding_instrument()
		return manager.get( self.pk, pk )

	def __str__( self ):
		return "pk: {}\nname: {}".format( self.pk, self.name )


class Manager_account( Manager_base ):

	class Meta:
		debug_all_objects = debug.all_account
		debug_one_objects = debug.one_account
		model = Account
		url = settings[ 'url' ] + 'account/'
