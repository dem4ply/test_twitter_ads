from base import Model, set_property
from .line import Line

class Campaign( Model ):
	_properties = {}
	class Meta( Model.Meta ):
		url = 'account/{account_id}/campaigns/{id}'

	def init_line( self, bid_amount, product_type, placements ):
		line = Line( account=self.account )
		line.campaign_id = self.id
		line.bid_amount_local_micro= bid_amount
		line.product_type = product_type
		line.placements = placements
		line.paused = True

		line.save()

		return line



	def __str__( self ):
		return "id: {}\nname: {}".format( self.id, self.name)

set_property( Campaign, 'name' )
set_property( Campaign, 'created_at' )
set_property( Campaign, 'end_time' )
set_property( Campaign, 'id' )
set_property( Campaign, 'update_at' )
set_property( Campaign, 'account_id' )
set_property( Campaign, 'deleted' )
set_property( Campaign, 'paused' )
set_property( Campaign, 'currency' )
set_property( Campaign, 'total_budget_amount_local_micro' )
set_property( Campaign, 'daily_budget_amount_local_micro' )
set_property( Campaign, 'funding_instrument_id' )
set_property( Campaign, 'start_time' )
