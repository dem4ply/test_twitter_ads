from base import Model, set_property

class Target( Model ):
	_property = {}
	class Meta( Model.Meta ):
		url = 'account/{account_id}/targeting_criteria/{id}'

	def create( self, line, target ):
		query = {
			'line_item_id': line.pk,
			'targeting_type': target.kind,
			'targeting_value': target.value,
		}
		url_params = {
			'account_pk': line.account_id,
		}
		super().create( query=query )

set_property( Target, 'account_id' )
set_property( Target, 'created_at' )
set_property( Target, 'deleted' )
set_property( Target, 'id' )
set_property( Target, 'line_item_id' )
set_property( Target, 'name' )
set_property( Target, 'targeting_type' )
set_property( Target, 'targeting_value' )
set_property( Target, 'update_at' )

class Target_phrase( Model ):
	def __init__( self, value, **kargs ):
		super().__init__( **kargs )
		if self.targeting_type is None:
			self.targeting_type = 'PHRASE_KEYWORD'
		if self.targeting_value is None:
			self.targeting_value = value
	pass

set_property( Target_phrase, 'targeting_value' )
set_property( Target_phrase, 'targeting_type' )

class Target_location( Model ):
	_property = {}
	class Meta( Model.Meta ):
		url = 'targeting_criteria/locations/'

	@classmethod
	def get_city( klass, q ):
		return klass.read( 'CITY', q )

	@classmethod
	def get_country( klass, q ):
		return klass.read( 'COUNTRY', q )

	@classmethod
	def get_region( klass, q ):
		return klass.read( 'REGION', q )

	@classmethod
	def get_postal_code( klass, q ):
		return klass.read( 'POSTAL_CODE', q )

	@classmethod
	def read( klass, kind, q ):
		query = {
			'location_type': kind,
			'q': q,
		}

		return super().read( query=query )

	def __str__( self ):
		return "name: {}\nvalue: {}\ntype: {}".format( self.name,
			self.targeting_value, self.targeting_type )

set_property( Target_location, 'name' )
set_property( Target_location, 'targeting_type' )
set_property( Target_location, 'targeting_value' )
