from base import Model, set_property
from .funding_instrument import Funding_instrument
from .tweet import Tweet

class Account( Model ):
	_properties = {}
	class Meta( Model.Meta ) :
		url = 'account/{id}'

	def __init__( self, account, **kargs ):
		super().__init__( self, **kargs )

	def read_funding_instrument( self, id=None ):
		return Funding_instrument.read( account=self, id=id )

	def create_tweet_promotion( self, text ):
		tweets = Tweet( text=text )
		return tweets.create( self.pk )

	def __str__( self ):
		return "id: {}\nname: {}".format( self.id, self.name )

set_property( Account, 'approval_status' )
set_property( Account, 'create_at' )
set_property( Account, 'deleted' )
set_property( Account, 'id' )
set_property( Account, 'name' )
set_property( Account, 'timezone' )
