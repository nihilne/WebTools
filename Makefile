dev:
	flask run --debug

watch-css:
	npx @tailwindcss/cli -i app/static/css/input.css -o app\static\css\styles.css --watch

css:
	npx @tailwindcss/cli -m -i app/static/css/input.css -o app\static\css\styles.css

js:
	npx terser app/static/js/main.js \
	-o app/static/js/main.min.js -c -m

docker:
	docker build -t nihilne/webtools .

build: css js docker