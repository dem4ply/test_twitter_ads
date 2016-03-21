from settings import settings
from unittest.mock import patch
from requests_oauthlib import OAuth1Session
import debug
from base import Manager_base

class Target():
	def __init__( self, **kargs ):

		self.name = kargs.get( 'name' )
		self.kind = kargs.get( 'targeting_type' )
		self.value = kargs.get( 'targeting_value' )

	def __str__( self ):
		return "name: {}".format( self.name)

class Manager_target( Manager_base ):
	class Meta:
		debug_all_objects = debug.all_target
		debug_one_objects = debug.one_target
		model = Target
		url = settings[ 'url' ] + 'targeting_criteria/locations/'

	def get_all( self, kind, q ):
		return super().get_all( location_type=kind, q=q )
