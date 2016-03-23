import sys
from requests_oauthlib import OAuth1Session
from settings import settings
import datetime

from unittest.mock import patch

from models.account import Account
from models.campaign import Campaign
from models.line import Line
from models.target import Target, Target_phrase, Target_location
from models.funding_instrument import Funding_instrument
from models.tweet import Tweet, Tweet_promoted

import debug


l_argv = len( sys.argv )
# no se manadaron parametros
if ( l_argv ==  1 ):
	accounts = Account.read()
	for account in accounts:
		print( account )

#se envio solo el primer parametro el del id de la cuenta
elif ( l_argv == 2 ):
	account_id = sys.argv[1]
	account = Account.read( id=account_id )
	instruments = account.read_funding_instrument()
	for instrument in instruments:
		print( instrument )

elif ( l_argv == 3 ):
	date = datetime.date.today() + datetime.timedelta(days=3)
	date = date.strftime('%Y-%m-%dT%XZ')

	account_id = sys.argv[1]
	instrument_id = sys.argv[2]

	account = Account.read( id=account_id )
	instrument = account.read_funding_instrument( id=instrument_id )

	campaign = instrument.init_campaign( 'campaing_test', date, 500000000, 50000000 )
	print( campaign )

	line = campaign.init_line( 1500000, 'PROMOTED_TWEET', 'ALL_ON_TWITTER' )
	print( line )

	location = Target_location.get_city( 'San Francisco' )[0]
	print ( m.mock_calls )

	phrase = Target_phrase( value='grumpy cat' )

	line.add_target( location )
	line.add_target( phrase )

	tweet = Tweet( account=account )
	tweet.status = 'Hola mundo'
	tweet.save()

	line.add_tweet_promoted( tweet )

