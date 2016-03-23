from base import Model
from .campaign import Campaign

class Funding_instrument( Model ):
	class Meta:
		url = 'account/{account_pk}/funding_instruments/{pk}'

	def __init__( self, **kargs ):
		super().__init__()
		self.account_id = kargs.get( 'account_id' )
		self.cancelled = kargs.get( 'cancelled' )
		self.created_at = kargs.get( 'created_at' )
		self.credit_limit = kargs.get( 'credit_limit_local_micro' )
		self.pk = kargs.get( 'id' )
		self.kind = kargs.get( 'type' )
		self.start_time = kargs.get( 'start_time' )

	def read( self, account_id, pk=None, url_params=None, query=None ):
		if not url_params:
			url_params = {}
		url_params[ 'account_id' ] = account_id
		return super().read( pk, url_params, query )

	def init_campaign( self, name, start_time,
		total_budget_amount, daily_budget_amount ):

		campaign = Campaign()
		return campaign.create( self, name, start_time,
			total_budget_amount, daily_budget_amount )
