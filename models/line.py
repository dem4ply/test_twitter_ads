from base import Model, set_property
from .target import Target
from .tweet import Tweet_promoted

class Line( Model ):
	class Meta( Model.Meta ):
		url = 'account/{account_id}/line_items/{id}'

	def add_target( self, target ):
		_target = Target( account=self.account )
		_target.targeting_type = target.targeting_type
		_target.targeting_value= target.targeting_value
		_target.line_item_id = self.id

		_target.save()
		return _target

	def add_tweet_promoted( self, tweet ):
		tweet_promoted = Tweet_promoted( account=self.account )
		tweet_promoted.tweet_ids = tweet.id
		tweet_promoted.line_item_id = self.id
		
		tweet_promoted.save()

		return tweet_promoted


	def __str__( self ):
		return "id: {}\nname: {}".format( self.id, self.name )


set_property( Line, 'account_id' )
set_property( Line, 'bid_amount_local_micro' )
set_property( Line, 'bid_type' )
set_property( Line, 'id' )
set_property( Line, 'name' )
set_property( Line, 'placements' )
set_property( Line, 'product_type' )
set_property( Line, 'paused' )
set_property( Line, 'campaign_id' )

