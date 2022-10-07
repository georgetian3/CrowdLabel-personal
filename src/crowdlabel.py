from flask import Flask, request

app = Flask(__name__)


class CrowdLabelServer:
    def __init__(self) -> None:
        pass

class CrowdLabelWeb:
    def __init__(self) -> None:
        pass


@app.route('/')
def index(request):
    return ('CrowdLabel')