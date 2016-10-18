WORKDIR = $(shell pwd)
NAME = demo
HOST_PORT = 5050
REMOTE_PORT = 5050

build:
	docker build -t $(NAME):latest .

runi:
	docker run -it --rm \
		--name $(NAME) \
		--volume=$(WORKDIR):/opt/sps/demo/ \
		$(NAME):latest /bin/bash

run:
	docker run -d \
		-p $(HOST_PORT):$(REMOTE_PORT) \
		--volume=$(WORKDIR):/opt/sps/demo/ \
		--name $(NAME) \
		$(NAME):latest python3 app.py

repl:
	docker exec -it $(NAME) ipython

remote_watch:
	docker exec -it $(NAME) make watch

watch:
	ptw --ignore __pycahce__

tail:
	docker logs -f $(NAME)

clean:
	docker stop $(NAME)
	docker rm $(NAME)