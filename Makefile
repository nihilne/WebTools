.PHONY: dev watch-css npm css js build run deploy docker-build docker-run db-init db-migrate db-upgrade db-downgrade db-reset

dev:
	flask run --debug

sort-imports:
	ruff check --select I --fix

watch-css:
	npx tailwindcss -i app/static/css/input.css -o app/static/css/styles.css --watch

npm:
	npm install

css:
	npx tailwindcss -m -i app/static/css/input.css -o app/static/css/styles.css

js:
	npx terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m

run:
	docker compose up -d

stop:
	docker compose down

build: npm css js
	docker build -t nihilne/webtools .

deploy: build run