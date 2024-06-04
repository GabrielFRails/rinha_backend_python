import uuid
from fastapi import HTTPException

from api_models import *
from libtransaction import *
from libstatement import *
from libclient import *
from libutils import *

def api_transaction(clientid, transaction):
# {
	if not check_client_existence(clientid):
		return 1, None, HTTPException(status_code=404, detail="Cliente não encontrado na base de dados")  

	transaction_value = transaction.valor
	transaction_type = transaction.tipo

	err = transaction_exe(clientid, transaction_value, transaction_type)
	log_info(f"transaction err: {err == True}")

	if not err:
		api_upate_statement(clientid, transaction)
		return 0, {
			"saldo": client_get_balance(clientid),
			"limite": client_get_limit(clientid)
		}, None

	return 1, None, HTTPException(status_code=422, detail="Não foi possível realizar a transação")
# }

def api_upate_statement(clientid, transaction):
# {
	transaction_dict = transaction.__dict__
	transaction_dict['tipo'] = transaction.tipo.value
	transaction_dict['tid'] = str(uuid.uuid4())
	statement_update(clientid, transaction_dict)
# }

def api_get_statement(clientid):
# {
	statement_db = statement_get(clientid)

	data = []
	for s in statement_db:
		d = json.loads(s[0])
		dt_formated = utils_convert_timestamp_to_datetime(s[1])
		d['realizada_em'] = dt_formated
		data.append(d)

	return data
# }

def api_client_get(clientid):
# {
	if not check_client_existence(clientid):
		return -1, None, HTTPException(status_code=404, detail="Cliente não encontrado na base de dados")  

	return 0, client_data_get(clientid), None
# }