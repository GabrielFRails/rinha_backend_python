import redis

class RedisClient:
	def __init__(self, host="redis", port="6379"):
		self.r = redis.Redis(host=host, port=port)

	def set(self, key, value):
		self.r.set(key, value)

	def get(self, key):
		return self.r.get(key)