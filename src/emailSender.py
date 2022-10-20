from flask import Flask
import flask_mail


# 异步发送邮件
class EmailSender:
    def __init__(self):
        self.app = Flask(__name__)
        # SMTP服务器地址，例如QQ邮箱的smtp.qq.com
        self.app.config['MAIL_SERVER'] = 'smtp.163.com'
        # SMTP服务器端口，一般为465
        self.app.config['MAIL_PORT'] = 465
        # 是否启用SSL加密（反正很牛逼的东西）
        self.app.config['MAIL_USE_SSL'] = True
        # 是否启用TLS加密（反正很牛逼的东西）
        self.app.config['MAIL_USE_TLS'] = False
        # 登入的邮箱，例如2731510961@qq.com，不能使用无法其他服务的邮箱，例如snbckcode@gmail.com不能使用smtp.qq.com
        self.app.config['MAIL_USERNAME'] = 'crowdlabel@163.com'
        # 授权码，在设置smtp的时候有
        self.app.config['MAIL_PASSWORD'] = 'YLCRKXFODXVADHBB'
        # 初始化对象
        self.mail_obj = flask_mail.Mail(self.app)

    def sendAsyncEmail(self, msg):
        app = self.app
        with app.app_context():
            self.mail_obj.send(msg)

    def emailGenerator(self, email):
        email = email.replace("%40", "@")
        msgObject = flask_mail.Message(
            subject="test",
            body="text",
            sender="crowdlabel@163.com",
            recipients=[email]
        )
        return msgObject
