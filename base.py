from unittest.mock import patch
from requests_oauthlib import OAuth1Session
from settings import settings

class Manager_base():
	class Meta:
		debug_all_objects = None
		debug_one_objects = None
		model = None
		url = settings[ 'url' ]

	def __init__( self ):

		self.oauth = OAuth1Session( settings[ 'CLIENT_KEY' ],
			client_secret=settings[ 'CLIENT_SECRET' ],
			resource_owner_key=settings[ 'OWNER_KEY' ],
			resource_owner_secret=settings[ 'OWNER_SECRET' ] )


	def get_all( self, *argv, **kargs ):
		"""
		Obtiene todas los datos de un objeto

		Arguments
		---------
		argv: array
			lista de eleimento qe se le concatenaran a la url

		Returns
		-------
		array: lista de todos los objetos
		"""
		url = self.Meta.url + '/'.join( argv )
		response = self._do_request( url, self.Meta.debug_all_objects, query=kargs )

		data = response.json()[ 'data' ]
		result = []
		for d in data:
			result.append( self.Meta.model( **d ) )
		return result

	def get( self, *argv ):
		"""
		regresa una objeto

		Arguments
		---------
		argv: array
			lista de eleimento qe se le concatenaran a la url

		Returns
		-------
		model: regresa el objeto que se definio en el Meta
		"""
		url = self.Meta.url + '/'.join( argv )
		response = self._do_request( url, self.Meta.debug_one_objects )
		data = response.json()[ 'data' ]
		return self.Meta.model( **data )

	def create( self, *argv, **kargs):
		"""
		crea un objeto

		Arguments
		---------
		argv: array
			lista de eleimento qe se le concatenaran a la url
		kargs: dict
			diccionario de parametros para la funcion de creacion

		Returns
		-------
		model: regresa el objeto que se definio en el Meta
		"""
		url = self.Meta.url + '/'.join( argv )
		response = self._do_request_post( url, self.Meta.debug_one_objects, query=kargs )
		data = response.json()[ 'data' ]
		return self.Meta.model( **data )

	def update( self, *argv, **kargs):
		"""
		actualiza un objeto

		Arguments
		---------
		argv: array
			lista de eleimento qe se le concatenaran a la url
		kargs: dict
			diccionario de parametros para la funcion de actualizacion

		Returns
		-------
		model: regresa el objeto que se definio en el Meta
		"""
		url = self.Meta.url + '/'.join( argv )
		response = self._do_request_post( url, self.Meta.debug_one_objects, query=kargs )
		data = response.json()[ 'data' ]
		return self.Meta.model( **data )

	def _do_request( self, url, debug_object, query=None ):
		"""
		genera el response usando la url y si esta en modo debug le regresa el mock
		"""
		if settings[ 'debug' ]:
			with patch.object( self.oauth, 'get', return_value=debug_object):
				response = self.oauth.get( url )
		else:
			response = self.oauth.get( url )
		if response.status_code != 200:
			message = response.json()[ 'errors'][0][ 'message' ]
			raise ValueError( message )
		return response

	def _do_request_post( self, url, debug_object, query=None ):
		"""
		genera el response usando la url y si esta en modo debug le regresa el mock
		"""
		if settings[ 'debug' ]:
			with patch.object( self.oauth, 'post', return_value=debug_object):
				response = self.oauth.post( url, params=query )
		else:
			response = self.oauth.post( url, params=query )
		if response.status_code != 200:
			message = response.json()[ 'errors' ][0][ 'message' ]
			raise ValueError( message )
		return response

	def _do_request_put( self, url, debug_object, query=None ):
		"""
		genera el response usando la url y si esta en modo debug le regresa el mock
		"""
		if settings[ 'debug' ]:
			with patch.object( self.oauth, 'put', return_value=debug_object):
				response = self.oauth.put( url, params=query )
		else:
			response = self.oauth.put( url, params=query )
		if response.status_code != 200:
			message = response.json()[ 'errors' ][0][ 'message' ]
			raise ValueError( message )
		return response
		
