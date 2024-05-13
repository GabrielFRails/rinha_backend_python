runall:
	docker-compose up --build

stopall:
	docker-compose down

logs:
	docker-compose logs

clean:
	docker image prune && \
	docker container prune
