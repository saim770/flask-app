package httpapi

default allow_ip = false

allow_ip {
    input.ip == "127.0.0.1"  # Add additional allowed IPs as needed
    # For IPv6, you might add: input.ip == "::1"
}
