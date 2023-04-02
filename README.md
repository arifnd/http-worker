# HTTP Worker

![CI/CD](https://github.com/arifnd/http-worker/actions/workflows/main.yaml/badge.svg)

HTTP Worker is a simple REST API built with [Flask](https://github.com/pallets/flask) and [cloudscraper](https://github.com/VeNoMouS/cloudscraper) that allows you to send HTTP requests to any URL.

## Getting Started

### Prerequisites

- Docker

### Installation

1. Clone the repository:

```bash
git clone https://github.com/arifnd/http-worker.git
```

2. Change into the project directory:

```bash
cd http-worker
```

3. Build the Docker image:

```
docker build -t http-worker .
```

4. Start the application using Docker:

```bash
docker run --rm -e SECRET_KEY=my-secret-key -e ALLOWED_IPS=127.0.0.1,192.168.1.1 -p 8080:8080 http-worker
```

Note: Replace `my-secret-key` and `127.0.0.1,192.168.1.1` with your own values for the `SECRET_KEY` and `ALLOWED_IPS` environment variables.

This command will start a new Docker container. Once the tests are complete, the container will be automatically deleted.

### Usage

You can use any HTTP client to send a POST request to the `/request` endpoint with the `url` parameter set to the URL you want to request.

For example, using `curl`:

```bash
curl -X POST -H "X-Secret-Key: my-secret-key" http://localhost:8080/request -d "url=https://www.google.com"
```

You should receive a response with the HTTP status code and body of the response.

### Testing

To run the unit tests, use the following command:

```bash
docker run --rm -e SECRET_KEY=my-secret-key -e ALLOWED_IPS=127.0.0.1,192.168.1.1 http-worker python -m unittest discover -s test
```

Note: Replace `my-secret-key` and `127.0.0.1,192.168.1.1` with your own values for the `SECRET_KEY` and `ALLOWED_IPS` environment variables.

This command will start a new Docker container and run the tests inside it. Once the tests are complete, the container will be automatically deleted.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.