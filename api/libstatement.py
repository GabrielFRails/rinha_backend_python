import time
import json

from libclient import *
from liblog import *
from api_models import *

def statement_get(clientid, n=10):
# {
	log_info(f"statement_get({clientid}, {n})")
	db = _clientdb()
	return db.get_client_statement(clientid, n)
# }

def statement_update(clientid, transaction):
# {
	log_info(f"statement_update({clientid}, {transaction})")
	db = _clientdb()
	ts = int(time.time())
	transaction_dumps = json.dumps(transaction)
	db.update_client_statement(clientid, transaction_dumps, ts)
# }

__client_db = None
def _clientdb():
	global __client_db
	if not __client_db:
		__client_db = Client()

	return __client_db