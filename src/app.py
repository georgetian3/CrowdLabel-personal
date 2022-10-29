from flask import Flask, request, render_template, redirect
from user import *
app = Flask(__name__)
import platform

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    API: accepts login details in the following dict format:
    {
        'username': '',
        'password': '',
    }
    """
    if request.method == 'GET':
        return render_template('login.html')


    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if correct_credentials(username, password):
            return render_template('index.html', username=username)
        elif username_exists(username):
            login_massage = "密码错误，请输入正确密码"
            return render_template('login.html', message=login_massage)
        else:
            login_massage = "不存在该用户，请先注册"
            return render_template('login.html', message=login_massage)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if username_exists(username):
            login_massage = "温馨提示：用户已存在，请直接登录"
            return render_template('register.html', message=login_massage)
        else:
            create_user(
                username,
                request.form['email'],
                password,
                0
            )

            return render_template('index.html', username=username)

        pass

@app.route('/user/<username>')
def user(username):
    return 'requested info for ' + username

@app.route('/tasks')
def tasks():
    pass

@app.route('/task/<id>')
def task(id):
    return 'requested task with id ' + str(id)

@app.route('/verify', methods=['POST'])
def verify():
    username = request.form['username']
    email = request.form['email']
    verification_code = request.form['code']
    verify_email(username, email, verification_code)


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
