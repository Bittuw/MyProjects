import MySQLdb

class Connection:
	def __init__(self, user, password, db, host):
		self.user = user
		self.password = password
		self.db = db
		self.host = host
		self._connection = None

	@property
	def connection(self):
		return self._connection

	def __enter__(self):
		self.connect()

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.disconnect()

	def connect(self):
		if not self._connection:
			self._connection = MySQLdb.connect(
				user = self.user, 
				passwd = self.password,
				db  = self.db,
				host = self.host,
			)
	def disconnect(self):
		if self._connection:
			self._connection.close()

class ConsertModal:
	def __init__(name):
		self.name = name
	


class Consert:
	def __init__(self, db_connection) :
		self.db_connection = db_connection.connection

	def save(self, db_connection, name, theatre, description):
		db_connection.connect()
		# self.db_connection = db_connection.connection
		c = self.db_connection.cursor()
		c.execute("INSERT INTO my_app_consert (name, theatre, description) VALUES (%s, %s, %s)", (name, theatre, description))
		self.db_connection.commit()
		c.close()

	@staticmethod
	def get_conserts(db_connection):
		db_connection.connect()
		c = db_connection.connection.cursor()
		# c = db_connection.cursor()
		c.execute("SELECT * FROM my_app_consert")
		result = list(c.fetchall())
		RESULT = []
		for rez in result:
			RESULT.append(list(rez)[1])
		c.close()
		return RESULT