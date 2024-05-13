from libdb import *

class Client(RedisClient):
	def __init__(self, host="redis", port="6379"):
		super().__init__(host, port)
		self.client_balance_field = "saldo"
		self.client_limit_field = "limite"

	def get_client_key(self, id):
		return f"client:{id}"

	def get_client_balance(self, clientid):
		field = self.client_balance_field
		client_key = self.get_client_key(clientid)
		balance = self.r.hget(client_key, field)
		return balance

	def get_client_limit(self, clientid):
		field = self.client_limit_field
		client_key = self.get_client_key(clientid)
		limit = self.r.hget(client_key, field)
		return limit

def client_get_balance(clientid):
	db = _clientdb()
	return db.get_client_balance(clientid)

def client_get_limit(clientid):
	db = _clientdb()
	return db.get_client_limit(clientid)

__client_db = None
def _clientdb():
	global __client_db
	if not __client_db:
		__client_db = Client()

	return __client_db

		