runall:
	docker-compose up --build -d

stop:
	docker-compose down

logs:
	docker-compose logs -f

clean:
	docker image prune && \
	docker container prune

cleandata:
	docker exec -i rinha_backend_python_redis_1 redis-cli FLUSHALL
