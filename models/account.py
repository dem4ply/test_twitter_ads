from base import Model
from .funding_instrument import Funding_instrument
from .tweet import Tweet

class Account( Model ):
	class Meta:
		url = 'account/{pk}'

	def __init__( self, **kargs ):
		super().__init__()

		self.name = kargs.get( 'name' )
		self.timezone = kargs.get( 'timezone' )
		self.pk = kargs.get( 'id' )
		self.create_at = kargs.get( 'created_at' )
		self.approval_status = kargs.get( 'approval_status' )
		self.is_deleted = kargs.get( 'deleted' )

	def read_funding_instrument( self, pk=None ):
		instruments = Funding_instrument()
		return instruments.read( self.pk, pk )

	def create_tweet_promotion( self, text ):
		tweets = Tweet( text=text )
		return tweets.create( self.pk )

	def __str__( self ):
		return "pk: {}\nname: {}".format( self.pk, self.name )
