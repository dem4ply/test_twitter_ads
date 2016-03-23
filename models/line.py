from base import Model
from target import Target

class Line( Model ):
	class Meta:
		url = 'account/{account_pk}/line_items/{pk}'

	def __init__( self, **kargs ):
		super().__init__()
		self.account_id = kargs.get( 'account_id' )
		self.bid_amount = kargs.get( 'bid_amount_local_micro' )
		self.bid_type = kargs.get( 'bid_type' )
		self.kind= kargs.get( 'product_type' )
		self.name = kargs.get( 'name' )
		self.pk = kargs.get( 'id' )
		self.placements= kargs.get( 'placements' )

	def read( self, account_id, pk=None, url_params=None, query=None ):
		if not url_params:
			url_params = {}
		url_params[ 'account_id' ] = account_id
		return super().read( pk, url_params, query )

	def add_target( self, target ):
		_target = Target()
		return _target.create( self, target )
