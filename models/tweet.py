from base import Model
from target import Target

class Tweet( Model ):
	class Meta:
		url = 'account/{account_pk}/tweet/{pk}'

	def __init__( self, **kargs ):
		super().__init__()
		self.pk = kargs.get( 'id' )
		self.text = kargs.get( 'text' )

	def create( self, account_id, text=None ):
		if not text:
			if not self.text:
				raise ValueError( "No se mando el texto del tweet" )
			text = self.text

		url_params = {
			'account_id': account_id,
		}
		query = {
			'status': text,
		}
		return super().create( url_params=url_params, query=query )
