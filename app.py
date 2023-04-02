from flask import Flask, request, jsonify
import cloudscraper
import random
import os

app = Flask(__name__)

# List of allowed IP addresses
ALLOWED_IPS = os.getenv('ALLOWED_IPS')

# Get debug mode
DEBUG = os.getenv('DEBUG', True)

# Get the secret key from the environment variable
SECRET_KEY = os.getenv('SECRET_KEY')

# Middleware to check the client's IP address against the whitelist
@app.before_request
def check_ip():
    allowed_ips = ALLOWED_IPS.split(",")
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr).split(",")
    app.logger.info('visitor IP %s', client_ip)
    if client_ip[0] not in allowed_ips:
        return jsonify({'error': 'Forbidden'}), 403

# Middleware to check the secret key
@app.before_request
def check_secret_key():
    if request.headers.get('X-Secret-Key') != SECRET_KEY:
        return jsonify({'error': 'Invalid secret key'}), 401

@app.route('/request', methods=['POST'])
def handle_request():
    # Get URL from form input
    url = request.form.get('url')

    # Check if URL is valid
    if not url or not url.startswith('http'):
        return jsonify({'error': 'Invalid URL'}), 400

    # Create a new Cloudscraper session
    scraper = cloudscraper.create_scraper(browser='chrome')

    try:
        # Make the HTTP request using the Cloudscraper session
        response = scraper.get(url)
        response.raise_for_status()

        return response.text

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the server
    app.run(debug=DEBUG, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
