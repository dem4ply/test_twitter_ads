import sys
from requests_oauthlib import OAuth1Session
from settings import settings
from account import Manager_account, Account
from target import Manager_target
import datetime


manager = Manager_account()
l_argv = len( sys.argv )
# no se manadaron parametros
if ( l_argv ==  1 ):
	accounts = manager.get_all()
	for account in accounts:
		print( account )

#se envio solo el primer parametro el del id de la cuenta
elif ( l_argv == 2 ):
	account = manager.get( sys.argv[1] )
	instruments = account.get_all_funding_instrument()
	for instrument in instruments:
		print( instrument )

elif ( l_argv == 3 ):
	date = datetime.date.today() + datetime.timedelta(days=3)
	date = date.strftime('%Y-%m-%dT%XZ')
	account = manager.get( sys.argv[1] )
	instrument = account.get_one_funding_instrument( sys.argv[2] )
	campaign = instrument.start_campaing( date, "My First Campaign",
		500000000, 50000000 )
	line = campaign.create_line( 1500000, 'PROMOTED_TWEET', 'ALL_ON_TWITTER', True )
	manager_target = Manager_target()
	target = manager_target.get_all( 'CITY', 'San Francisco' )[0]
	target_2 = line.set_target_location( target )
	line.set_target_phrase( 'grumpy cat' )
	line = line.set_paused( False )
