from api_models import *
from libtransaction import *
from libclient import *

def api_transaction(clientid, transaction):
# {
	value = transaction.valor
	type = transaction.tipo
	success = -1

	if type == TransactionType.CREDITO.value:
		success = transaction_credit(clientid, value)
	
	elif type == TransactionType.DEBITO.value:
		success = transaction_debit(clientid, value)

	if success == 0:
		return 0, {
			"saldo": client_get_balance(clientid),
			"limite": client_get_limit(clientid)
		}

	return -1, None
# }