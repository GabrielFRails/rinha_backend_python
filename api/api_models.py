from pydantic import BaseModel, Field
from enum import Enum

class Client(BaseModel):
	id: int
	limite: int
	saldo_inicial: int

class TransactionType(str, Enum):
	CREDITO = 'c'
	DEBITO = 'd'

class TransactionRequest(BaseModel):
	valor: int
	tipo: TransactionType
	descricao: str = Field(max_length=10)
	