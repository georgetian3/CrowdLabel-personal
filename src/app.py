from flask import Flask, request, render_template, redirect
from crowdlabel import CrowdLabel

server = CrowdLabel()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print('json', request.get_json(force=True))
        return 'test'
        # TODO: handle user login
        pass

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':

        return render_template('register.html')
    elif request.method == 'POST':
        # TODO: handle user registration
        pass

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/about')
def about():
    return 'Software Engineering 2022 fall group project'

if __name__ == '__main__':
    app.run(debug=True, port=5000)