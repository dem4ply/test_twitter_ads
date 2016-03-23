from base import Model
from .line import Line

class Campaign( Model ):
	class Meta:
		url = 'account/{account_pk}/campaigns/{pk}'

	def __init__( self, **kargs ):
		super().__init__()
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

	def init_line( self, bid_amount, product_type, placements ):
		line = Line()
		query = {
			'campaign_id': self.pk,
			'bid_amount_local_micro': bid_amount,
			'product_type': product_type,
			'placements': placements,
			'paused': True,
		}
		url_params = {
			'account_id': self.account_id
		}
		return line.create( url_params=url_params, query=query )

	def __str__( self ):
		return "pk: {}\nname: {}".format( self.pk, self.name)

	def read( self, account=None, pk=None, url_params=None, query=None ):
		if not url_params:
			url_params = {}
		if not account:
			if not self.account_id:
				raise ValueError( "El objeto no tiene definido el account_id" )
			else:
				account_id = self.account_id
		else:
			account_id = account.pk
		url_params[ 'account_id' ] = account_id
		return super().read( pk, url_params, query )

	def create( self, funding_instrument,
		name, start_time, total_budget_amount,
		daily_budget_amount, url_params=None, query=None ):

		if not url_params:
			url_params = {}
		url_params[ 'account_id' ] = account_id
		if not query:
			query = {
					'account_id': funding_instrument.account_id,
					'start_time': start_time,
					'funding_instrument_id': funding_instrument.pk,
					'name': name,
					'total_budget_amount_local_micro': total_budget_amount,
					'daily_budget_amount_local_micro': daily_budget_amount,
					'pause': True,
			}
		return super().create( url_params=url_params, query=query )
