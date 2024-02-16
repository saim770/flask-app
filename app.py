from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# IP Whitelisting Middleware
@app.before_request
def limit_remote_addr():
    if request.remote_addr not in {'127.0.0.1', '::1'}:  # Add allowed IPs here
        return make_response(jsonify(error="IP not allowed"), 403)

# Secure Headers
@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

@app.route('/')
def home():
    return 'Hello, World!'

# Method Restriction Policy Example
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data="This is a GET request response")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
