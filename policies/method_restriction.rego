package httpapi

default allow_method = false

allow_method {
    input.method == "GET"
}
