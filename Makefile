runall:
	docker-compose up --build -d

stopall:
	docker-compose down

logs:
	docker-compose logs

clean:
	docker image prune && \
	docker container prune
