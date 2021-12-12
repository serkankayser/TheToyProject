.SELECT: build up start down exec flake8 test
PROJECT_DIR = $(shell pwd)

build:
	docker-compose up --build
up:
	docker-compose up
ssh:
	# For Ubuntu: sudo apt install sshpass
	sshpass -p "root" ssh root@`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' blogapp`
server:
	docker exec -ti blogapp bash -c "python manage.py runserver 0.0.0.0:8001"
down:
	docker-compose down
flake8:
	# IGNORING ERROR -> Line too long
	flake8 --ignore=E501 --exit-zero $(PROJECT_DIR)
test:
	docker-compose run blogapp python3 manage.py test --verbosity 2
