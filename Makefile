.PHONY: dev tailwind install-npm install-htmx build-css build-js build-docker build-all run stop deploy

HTMX_VERSION = 2.0.10

dev:
	flask run --debug

tailwind:
	npx tailwindcss -i app/static/css/input.css -o app/static/css/styles.css --watch

install-npm:
	npm ci

install-htmx:
	curl -o app/static/js/htmx.min.js https://cdn.jsdelivr.net/npm/htmx.org@$(HTMX_VERSION)/dist/htmx.min.js

build-css:
	npx tailwindcss -m -i app/static/css/input.css -o app/static/css/styles.css

build-js:
	npx terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m

build-docker:
	docker build -t nihilne/webtools .

build-all: install-npm install-htmx build-css build-js build-docker

run:
	docker compose up -d

stop:
	docker compose down

deploy: build-all run