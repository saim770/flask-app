package httpapi

default secure_headers = false

secure_headers {
    input.headers["X-Frame-Options"] == "SAMEORIGIN"
    input.headers["Content-Security-Policy"] == "default-src 'self'"
}
