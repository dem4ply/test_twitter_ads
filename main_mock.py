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
	with patch.object( Account._oauth, 'get', return_value=debug.all_account ) as m:
		accounts = Account.read()
	print ( m.mock_calls )
	for account in accounts:
		print( account )

#se envio solo el primer parametro el del id de la cuenta
elif ( l_argv == 2 ):
	account_id = sys.argv[1]
	with patch.object( Account._oauth, 'get', return_value=debug.one_account ) as m:
		account = Account.read( id=account_id )
	print ( m.mock_calls )
	with patch.object( Funding_instrument._oauth, 'get', return_value=debug.all_instruments ) as m:
		instruments = account.read_funding_instrument()
	print ( m.mock_calls )
	for instrument in instruments:
		print( instrument )

elif ( l_argv == 3 ):
	date = datetime.date.today() + datetime.timedelta(days=3)
	date = date.strftime('%Y-%m-%dT%XZ')

	account_id = sys.argv[1]
	instrument_id = sys.argv[2]

	with patch.object( Account._oauth, 'get', return_value=debug.one_account ) as m:
		account = Account.read( id=account_id )
	print ( m.mock_calls )
	with patch.object( Funding_instrument._oauth, 'get', return_value=debug.one_instrument) as m:
		instrument = account.read_funding_instrument( id=instrument_id )
	print ( m.mock_calls )

	with patch.object( Campaign._oauth, 'post', return_value=debug.one_campaigns ) as m:
		campaign = instrument.init_campaign( 'campaing_test', date, 500000000, 50000000 )
	print ( m.mock_calls )

	print( campaign )

	with patch.object( Line._oauth, 'post', return_value=debug.one_line ) as m:
		line = campaign.init_line( 1500000, 'PROMOTED_TWEET', 'ALL_ON_TWITTER' )
	print ( m.mock_calls )

	print( line )

	with patch.object( Target_location._oauth, 'get', return_value=debug.all_target) as m:
		location = Target_location.get_city( 'San Francisco' )[0]
	print ( m.mock_calls )

	phrase = Target_phrase( value='grumpy cat' )

	with patch.object( Line._oauth, 'post', return_value=debug.one_target ) as m:
		line.add_target( location )
		line.add_target( phrase )
	print ( m.mock_calls )

	tweet = Tweet( account=account )
	tweet.status = 'Hola mundo'
	with patch.object( Tweet._oauth, 'post', return_value=debug.one_tweet) as m:
		tweet.save()
	print ( m.mock_calls )

	with patch.object( Tweet_promoted._oauth, 'post', return_value=debug.one_tweet_promoted) as m:
		line.add_tweet_promoted( tweet )
	print ( m.mock_calls )

