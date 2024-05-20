from libclient import *
from liblog import *

def transaction_credit(clientid, value):
# {
	log_info(f"transaction_credit({clientid}, {value})")
	db = _clientdb()
	success = db.increase_client_balance(clientid, value)

	log_info(f"transaction_credit success: {success}")
	return success
# }

def transaction_debit(clientid, value):
# {
	log_info(f"transaction_debit({clientid}, {value})")
	db = _clientdb()
	success = db.decrease_client_balance(clientid, value)

	log_info(f"transaction_debit success: {success}")
	return success
# }

__client_db = None
def _clientdb():
	global __client_db
	if not __client_db:
		__client_db = Client()

	return __client_db