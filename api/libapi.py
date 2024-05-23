from fastapi import HTTPException

from api_models import *
from libtransaction import *
from libclient import *

def api_transaction(clientid, transaction):
# {
	if not check_client_existence(clientid):
		return 1, None, HTTPException(status_code=404, detail="Cliente não encontrado na base de dados")  

	transaction_value = transaction.valor
	transaction_type = transaction.tipo

	err = transaction_exe(clientid, transaction_value, transaction_type)
	log_info(f"transaction err: {err == True}")

	if not err:
		return 0, {
			"saldo": client_get_balance(clientid),
			"limite": client_get_limit(clientid)
		}, None

	return 1, None, HTTPException(status_code=422, detail="Não foi possível realizar a transação")
# }

def api_client_get(clientid):
# {
	if not check_client_existence(clientid):
		return -1, None, HTTPException(status_code=404, detail="Cliente não encontrado na base de dados")  

	return 0, {
		"id": clientid,
		"saldo": client_get_balance(clientid),
		"limite": client_get_limit(clientid)
    }, None
# }