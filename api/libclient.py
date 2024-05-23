from libdb import *
from liblog import *

class Client(RedisClient):
	def __init__(self, host="redis", port="6379"):
		super().__init__(host, port)
		self.client_balance_field = "saldo"
		self.client_limit_field = "limite"

	def get_client_key(self, id):
		return f"client:{id}"
	
	def check_client_existence(self, clientid):
		client_key = self.get_client_key(clientid)
		return self.r.hgetall(client_key)

	def get_client_balance(self, clientid):
		field = self.client_balance_field
		client_key = self.get_client_key(clientid)
		balance = self.r.hget(client_key, field)
		return float(balance)

	def get_client_limit(self, clientid):
		field = self.client_limit_field
		client_key = self.get_client_key(clientid)
		limit = self.r.hget(client_key, field)
		return float(limit)
	
	def increase_client_balance(self, clientid, value):
		field = self.client_balance_field
		client_key = self.get_client_key(clientid)
		balance = self.get_client_balance(clientid)
		new_balance = balance + value
		
		result = self.r.hset(client_key, field, new_balance)
		return result
	
	def decrease_client_balance(self, clientid, value):
		field = self.client_balance_field
		client_key = self.get_client_key(clientid)
		balance = self.get_client_balance(clientid)
		new_balance = balance - float(value) 
		
		result = self.r.hset(client_key, field, new_balance)
		return result

def client_get_balance(clientid):
	log_info(f"client_get_balance({clientid})")
	db = _clientdb()
	return db.get_client_balance(clientid)

def client_get_limit(clientid):
	log_info(f"client_get_limit({clientid})")
	db = _clientdb()
	return db.get_client_limit(clientid)

def check_client_existence(clientid):
	log_info(f"check_client_existence({clientid})")
	db = _clientdb()
	return db.check_client_existence(clientid)

__client_db = None
def _clientdb():
	global __client_db
	if not __client_db:
		log_info(f"Client()")
		__client_db = Client()

	return __client_db

		