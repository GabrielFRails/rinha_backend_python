from fastapi import FastAPI
from api_models import *

from libclient import *

app = FastAPI()

@app.get("/")
def root_path():
	return {
		"msg": "Saudações ser pensante"
	}

@app.get("/clientes/{id}")
def get_client(id: int):
    return {
		"id": id,
		"saldo": client_get_balance(id),
		"limite": client_get_limit(id)
    }

@app.post("/clientes/{id}/transacoes")
def transaction_request(id: int, request: TransactionRequest):
	return {
		"limite" : 100000,
		"saldo" : -9098
	}

@app.get("/clientes/{id}/extrato")
def client_statement(id: int):
	return {
		"saldo": {
			"total": -9098,
			"data_extrato": "2024-01-17T02:34:41.217753Z",
			"limite": 100000
		},
		"ultimas_transacoes": [
			{
				"valor": 10,
				"tipo": "c",
				"descricao": "descricao",
				"realizada_em": "2024-01-17T02:34:38.543030Z"
			},
			{
				"valor": 90000,
				"tipo": "d",
				"descricao": "descricao",
				"realizada_em": "2024-01-17T02:34:38.543030Z"
			}
		]
	}