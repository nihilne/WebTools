.PHONY: dev watch-css npm css js build run deploy docker-build docker-run

dev:
	flask run --debug

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
	docker rm -f webtools || true
	docker run -d --name webtools -p 127.0.0.1:8000:8000 nihilne/webtools

build: npm css js 
	docker build -t nihilne/webtools .

deploy: build run