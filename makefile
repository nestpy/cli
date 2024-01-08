build-poetry:
	docker build -t poetry:1.7.1 .

bash:
	docker run --rm \
	-w /app \
	-v ${PWD}:/app \
	-it poetry:1.7.1 bash
