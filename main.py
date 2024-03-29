import os
import responder
import httpx

api = responder.API()


@api.route("/")
def index(req, res):
    res.text = "app-a"


# Endpoint which uses an external service "debugkit"
@api.route("/debugkit")
def debugkit(req, res):
    r = httpx.get("http://debugkit/info/hostname")
    res.text = r.text


# Endpoint which uses an external service "app-b"
@api.route("/app-b")
def app_b(req, res):
    app_b_svc = os.getenv("APPB_SVC", "app-b")
    r = httpx.get("http://" + app_b_svc)
    res.text = r.text


# New endpoint 1
@api.route("/new-endpoint-1")
def new_endpoint_1(req, res):
    res.text = "new endpoint 1"


# New endpoint 2
@api.route("/new-endpoint-2")
def new_endpoint_1(req, res):
    res.text = "new endpoint 2"


if __name__ == "__main__":
    port = os.getenv("APPA_PORT", "8080")
    api.run(address="0.0.0.0", port=int(port))
