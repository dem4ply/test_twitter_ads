from base import Model
from target import Target

class Tweet_promote( Model ):
	class Meta:
		url = 'account/{account_pk}/promoted_tweet/{pk}'

	def __init__( self, **kargs ):
		super().__init__()
		self.tweet_id = kargs.get( 'tweet_id' )
		self.created_at = kargs.get( 'created_at' )
		self.update_at = kargs.get( 'update_at' )
		self.pk = kargs.get( 'id' )
		self.deleted = kargs.get( 'deleted' )
		self.paused = kargs.get( 'paused' )
		self.line_item_id = kargs.get( 'line_item_id' )

	def create( self, account, line, tweet )
		url_params = {
			'account_id': account.pk,
		}
		query = {
			'line_item_id': line.pk,
			'tweet_ids': tweet.pk,
		}

		return super().create( url_params=url_params, query=query )
