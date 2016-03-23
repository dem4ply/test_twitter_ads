import sys
from requests_oauthlib import OAuth1Session
from settings import settings
from account import Manager_account, Account
from target import Manager_target
import datetime

from models.account import Account
from models.target import Target, Target_phrase, Target_location


manager = Manager_account()
l_argv = len( sys.argv )
# no se manadaron parametros
if ( l_argv ==  1 ):
	accounts = Account().read()
	for account in accounts:
		print( account )

#se envio solo el primer parametro el del id de la cuenta
elif ( l_argv == 2 ):
	account_id = sys.argv[1]
	account = Account().read( account_id )
	instruments = account.read_funding_instrument()
	for instrument in instruments:
		print( instrument )

elif ( l_argv == 3 ):
	date = datetime.date.today() + datetime.timedelta(days=3)
	date = date.strftime('%Y-%m-%dT%XZ')

	account_id = sys.argv[1]
	instrument_id == sys.argv[2]

	account = Account().read( account_id )
	instrument = account.read_funding_instrument( instrument_id )

	campaign = instrument.init_campaign( 'campaing_test', date, 500000000, 50000000 )
	line = campaign.init_line( 1500000, 'PROMOTED_TWEET', 'ALL_ON_TWITTER' )

	location = Target_location()
	location = location.get_city( 'San Francisco' )[0]

	phrase = Target_phrase( value='grumpy cat' )

	line.add_target( location )
	line.add_target( phrase )
