from flask import Flask, request, render_template
from crowdlabel import CrowdLabel

server = CrowdLabel()
app = Flask(__name__)

@app.route('/')
def index(request=None):
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login(request=None):
    if request.method == 'GET':

        return render_template('login.html')
    elif request.method == 'POST':
        # TODO: handle user login
        pass

def register(request=None, methods = ['GET', 'POST']):
    if request.method == 'GET':

        return render_template('register.html')
    elif request.method == 'POST':
        # TODO: handle user registration
        pass

@app.route('/admin')
def admin(request=None):
    return 'admin'

@app.route('/about')
def about(request=None):
    return 'Software Engineering 2022 fall group project'

if __name__ == '__main__':
    app.run(debug=True, port=5000)