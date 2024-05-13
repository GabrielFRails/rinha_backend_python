runall:
	docker-compose up --build -d

stopall:
	docker-compose down

logs:
	docker-compose logs

clean:
	docker image prune && \
	docker container prune

cleandata:
	docker exec -i rinha_backend_python_redis_1 redis-cli FLUSHALL
