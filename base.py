from unittest.mock import patch
from requests_oauthlib import OAuth1Session
from settings import settings

def set_property( klass, name, **kargs):
	"""
	"""
	klass._properties[ name ] = kargs
	default = kargs.get( 'default' )
	is_read_only = kargs.get( 'read_only', False )
	property_name = '_{name}'.format( name=name )
	def getter( self ):
		return getattr( self, property_name, default )
	if is_read_only:
		setattr( klass, name, property( getter ) )
	else:
		def setter( self, value ):
			setattr( self, property_name, value ) 
		setattr( klass, name, property( getter, setter ) )

class Model():
	class Meta:
		base_url = settings[ 'url' ]
		url = ''

	_properties = {}

	_oauth = OAuth1Session( settings[ 'CLIENT_KEY' ],
		client_secret=settings[ 'CLIENT_SECRET' ],
		resource_owner_key=settings[ 'OWNER_KEY' ],
		resource_owner_secret=settings[ 'OWNER_SECRET' ] )

	def __init__( self, account=None, **kargs ):
		self.account = account
		self.from_response( kargs )

	def _get_params( self ):
		"""
		Obtiene todos los parametros de la instancia
		"""
		result = {}
		for name in self._properties:
			name_attr = '_{name}'.format( name=name )
			val = getattr( self, name_attr, None )

			if val is None:
				continue
			result[ name ] = val

		return result

	def from_response( self, data ):
		"""
		asigna los parametros de un request a la instancia
		"""
		for name in self._properties:
			attr = '_{name}'.format( name=name )
			value = data.get( name )
			if value is None:
				continue
			setattr( self, attr, value )
		return self


	@classmethod
	def read( klass, account=None, id=None, query=None, url_params=None ):
		"""
		Obtiene los datos del api regresa un array de objetos si se asigna el id
		"""
		if url_params is None:
			url_params = {}
		if account is None:
			url_params[ 'account_id' ] = ''
		else:
			url_params[ 'account_id' ] = account.id
		if id is None:
			url_params[ 'id' ] = ''
			is_array = False
		else:
			url_params[ 'id' ] = id
			is_array = True
		url = klass._build_url( url_params=url_params )
		response = klass._oauth.get( url, params=query )
		klass.check_error( response )
		json = response.json()
		data = json[ 'data' ]
		if id is None:
			return [ klass( account=account, **d ) for d in data ]
		else:
			return klass( account=account, **data )
	
	def save( self ):
		query = self._get_params()
		url_params = {}
		url_params[ 'account_id' ] = self.account.id
		if self.id is None:
			url_params[ 'id' ] = ''
			url = self._build_url( url_params=url_params )
			response = self._oauth.post( url, params=query )
		else:
			url_params[ 'id' ] = self.id
			url = self._build_url( url_params=url_params )
			response = self.oauth.put( url, params=query )
		self.check_error( response )
		json = response.json()
		json = json.get( 'data', json )
		if isinstance( json, list ):
			json = json[0]
		self.from_response( json )

	@classmethod
	def _build_url( klass, url_params=None ):
		url = klass.Meta.base_url + klass.Meta.url
		if not url_params:
			url_params = {}
		return url.format( **url_params )

	@staticmethod
	def check_error( response ):
		if response.status_code != 200:
			message = response.json()[ 'errors'][0][ 'message' ]
			raise ValueError( message )

