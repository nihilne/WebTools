.PHONY: dev tailwind install-npm install-htmx build-css build-js build-docker build-all run stop restart restart-dev deploy

HTMX_VERSION = 2.0.10
SORTABLEJS_VERSION = 1.15.2

dev:
	docker compose up dev db adminer -d

tailwind:
	npx tailwindcss -i app/static/css/input.css -o app/static/css/styles.css --watch

install-npm:
	npm ci

install-js-pkgs:
	curl -o app/static/js/htmx.min.js https://cdn.jsdelivr.net/npm/htmx.org@$(HTMX_VERSION)/dist/htmx.min.js
	curl -o app/static/js/Sortable.min.js https://cdn.jsdelivr.net/npm/sortablejs@$(SORTABLEJS_VERSION)/Sortable.min.js

build-css:
	npx tailwindcss -m -i app/static/css/input.css -o app/static/css/styles.css

build-js:
	npx terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m

build-docker:
	docker build -t nihilne/webtools .

build-all: install-npm install-js-pkgs build-css build-js build-docker

run:
	docker compose up web db -d

stop:
	docker compose down

restart: stop run

restart-dev: stop dev

deploy: build-all run