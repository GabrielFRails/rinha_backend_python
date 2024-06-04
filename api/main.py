from fastapi import FastAPI, HTTPException

from api_models import *

from libclient import *
from libapi import *

app = FastAPI()

@app.get("/")
def root_path():
	return {
		"msg": "Saudações ser pensante"
	}

@app.get("/clientes/{id}")
def get_client(id: int):
	err, data, exception = api_client_get(id)
	if not err:
		return data

	raise exception
@app.post("/clientes/{id}/transacoes")
def transaction_request(id: int, request: TransactionRequest):
# {
	err, data, exception = api_transaction(id, request)

	if not err:
		return data
	
	raise exception
# }

@app.get("/clientes/{id}/extrato")
def client_statement(id: int):
	err, client_data, exception = api_client_get(id)
	if not err:
		return {
			"saldo": {
				"total": client_data['saldo'],
				"data_extrato": utils_convert_timestamp_to_datetime(time.time()),
				"limite": client_data['limite']
			},
			"ultimas_transacoes": api_get_statement(id)
		}
	
	raise exception