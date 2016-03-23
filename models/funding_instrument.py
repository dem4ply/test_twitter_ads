from base import Model, set_property
from .campaign import Campaign

class Funding_instrument( Model ):
	_properties = {}
	class Meta( Model.Meta ):
		url = 'account/{account_id}/funding_instruments/{id}'

	def init_campaign( self, name, start_time,
		total_budget_amount, daily_budget_amount ):

		campaign = Campaign( account=self.account)
		campaign.name = name
		campaign.start_time= start_time
		campaign.account_id = self.account.id
		campaign.funding_instrument_id = self.id
		campaign.total_budget_amount_local_micro = total_budget_amount
		campaign.daily_budget_amount_local_micro = daily_budget_amount 
		campaign.paused = True

		campaign.save()

		return campaign


	def __str__( self ):
		return "id: {}\ntype: {}".format( self.id, self.type)


set_property( Funding_instrument, 'account_id' )
set_property( Funding_instrument, 'cancelled' )
set_property( Funding_instrument, 'created_at' )
set_property( Funding_instrument, 'credit_limit_local_micro' )
set_property( Funding_instrument, 'id' )
set_property( Funding_instrument, 'start_time' )
set_property( Funding_instrument, 'type' )
