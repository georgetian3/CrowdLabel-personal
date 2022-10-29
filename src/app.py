from flask import Flask, render_template, redirect
import api
import platform

app = Flask(__name__)
app.register_blueprint(api.api, url_prefix='/api/v1')

"""
Communication is performed through JSON requests and responses
Missing keys will return an error
Extraneous keys will be ignored
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return redirect('/')


@app.route('/login')
def login():
    """
    API: accepts login details in the following dict format:
    {
        'username': '',
        'password': '',
    }
    """

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/user/<username>')
def user(username):
    return 'requested info for ' + username

@app.route('/tasks')
def tasks():
    pass

@app.route('/task/<id>')
def task(id):
    return 'requested task with id ' + str(id)

@app.route('/verify/<token>')
def verify(token):
    # TODO: verify token
    pass


@app.route('/admin')
def admin():
    return 'admin'


@app.route('/about')
def about():
    return 'Software Engineering 2022 fall group project'


if __name__ == '__main__':
    if platform.system() == 'Linux':
        app.run(debug=False, host='0.0.0.0', port=8000)
    else:
        app.run(debug=True, host='127.0.0.1', port=8000)
