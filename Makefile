dev:
	flask run --debug

watch-css:
	tailwindcss -i app/static/css/input.css -o app\static\css\styles.css --watch

build-css:
	tailwindcss -m -i app/static/css/input.css -o app\static\css\styles.css

build-docker:
	docker build -t nihilne/webtools .

build-js:
	terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m