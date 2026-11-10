.PHONY: dev tailwind install-npm build-css build-js build-docker build-all run stop restart restart-dev deploy

dev:
	docker compose up dev db adminer -d

tailwind:
	npx tailwindcss -i app/static/css/input.css -o app/static/css/styles.css --watch

install-npm:
	npm ci

build-css:
	npx tailwindcss -m -i app/static/css/input.css -o app/static/css/styles.css

build-js:
	npx terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m

build-docker:
	docker build -t nihilne/webtools .

build-all: install-npm build-css build-js build-docker

run:
	docker compose up web db -d

stop:
	docker compose down

restart: stop run

restart-dev: stop dev

deploy: build-all run