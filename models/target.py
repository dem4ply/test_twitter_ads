from base import Model

class Target( Model ):
	class Meta:
		url = 'account/{account_pk}/targeting_criteria/{pk}'

	def __init__( self, **kargs ):
		self.name = kargs.get( 'name' )
		self.created_at = kargs.get( 'created_at' )
		self.update_at = kargs.get( 'update_at' )
		self.account_id = kargs.get( 'account_id' )
		self.pk = kargs.get( 'id' )
		self.deleted = kargs.get( 'deleted' )
		self.targeting_value = kargs.get( 'targeting_value' )
		self.line_item_id = kargs.get( 'line_item_id' )
		self.targeting_type = kargs.get( 'targeting_type' )

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

class Target_phrase():
	def __init__( self, **kargs ):
		self.kind = kargs.get( 'kind', 'PHRASE_KEYWORD' )
		self.value = kargs.get( 'value' )

class Target_location( Model ):
	class Meta:
		url = 'targeting_criteria/locations/'

	def __init__( self, **kargs ):
		self.name = kargs.get( 'name' )
		self.kind = kargs.get( 'targeting_type' )
		self.value = kargs.get( 'targeting_value' )

	def get_city( self, q ):
		return self.read( 'CITY', q )

	def get_country( self, q ):
		return self.read( 'COUNTRY', q )

	def get_region( self, q ):
		return self.read( 'REGION', q )

	def get_postal_code( self, q ):
		return self.read( 'POSTAL_CODE', q )

	def read( self, kind, q ):
		query = {
			'location_type': kind,
			'q': q,
		}

		return super().read( query=query )

