from base import Model, set_property
from .target import Target

class Tweet( Model ):
	_property = {}
	class Meta( Model.Meta ):
		url = 'account/{account_id}/tweet/{id}'

set_property( Tweet, 'id' )
set_property( Tweet, 'status' )

class Tweet_promoted( Model ):
	_property = {}
	class Meta( Model.Meta ):
		url = 'account/{account_id}/promoted_tweets/{id}'

set_property( Tweet_promoted, 'id' )
set_property( Tweet_promoted, 'line_item_id' )
set_property( Tweet_promoted, 'tweet_ids' )
