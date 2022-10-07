from flask import Flask, request
from crowdlabel import CrowdLabelServer

server = CrowdLabelServer()
app = Flask(__name__)

@app.route('/')
def index(request):
    return 'CrowdLabel'

@app.route('/login')
def login(request):
    return 'Login'

@app.route('/admin')
def admin(request):
    return 'admin'
