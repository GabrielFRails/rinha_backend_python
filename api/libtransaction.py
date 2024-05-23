from libclient import *
from liblog import *
from api_models import *

def transaction_debit(clientid, transaction_value):
# {
	log_info(f"transaction_debit({clientid}, {transaction_value})")
	db = _clientdb()

	client_balance = client_get_balance(clientid)
	client_limit = client_get_limit(clientid)

	if (client_balance - transaction_value) < (client_limit * (-1)):
		log_info("client limit exced")
		return 1
	
	return db.decrease_client_balance(clientid, transaction_value)
# }

def transaction_credit(clientid, transaction_value):
# {
	log_info(f"transaction_credit({clientid}, {transaction_value})")
	db = _clientdb()
	
	return db.increase_client_balance(clientid, transaction_value)
# }

def transaction_exe(clientid, transaction_value, transaction_type):
# {
	if transaction_type == TransactionType.CREDITO.value:
		return transaction_credit(clientid, transaction_value)
	
	elif transaction_type == TransactionType.DEBITO.value:
		return transaction_debit(clientid, transaction_value)
# }

__client_db = None
def _clientdb():
	global __client_db
	if not __client_db:
		__client_db = Client()

	return __client_db