import json
import redis

def main():
# {
	r = redis.Redis(host='redis', port=6379)

	clients = [
		{
			"id": 1,
			"limite": 100000,
			"saldo": 0
		},
		{
			"id": 2,
			"limite": 80000,
			"saldo": 0
		},
		{
			"id": 3,
			"limite": 1000000,
			"saldo": 0
		},
		{
			"id": 4,
			"limite": 10000000,
			"saldo": 0
		},
		{
			"id": 5,
			"limite": 500000,
			"saldo": 0
		}
	]

	if not r.keys(): # means empty db
		for c in clients:
			client_key = f"client:{c['id']}"
			client_value = json.dumps(c)
			r.set(client_key, client_value)
		return

	print("Database already set!")
# }

if __name__ == "__main__":
	main()