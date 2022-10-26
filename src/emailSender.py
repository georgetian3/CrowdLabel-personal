from typing import Iterable
from flask import Flask
import flask_mail


CROWDLABEL_EMAIL = 'crowdlabel@163.com'

# 异步发送邮件
class EmailSender:
    def __init__(self):
        self.app = Flask(__name__)
        # SMTP服务器地址，例如QQ邮箱的smtp.qq.com
        self.app.config['MAIL_SERVER'] = 'smtp.163.com'
        # SMTP服务器端口，一般为465
        self.app.config['MAIL_PORT'] = 465
        # 是否启用SSL加密
        self.app.config['MAIL_USE_SSL'] = True
        # 是否启用TLS加密
        self.app.config['MAIL_USE_TLS'] = False
        self.app.config['MAIL_USERNAME'] = 'crowdlabel@163.com'
        # 授权码，在设置smtp的时候有
        self.app.config['MAIL_PASSWORD'] = 'YLCRKXFODXVADHBB'
        # 初始化对象
        self.mail_obj = flask_mail.Mail(self.app)

    def send_email(self,
        subject: str,
        body: str,
        recipients: list,
        sender: str=CROWDLABEL_EMAIL):

        sender = sender.replace('%40', '@')
        for i in range(len(recipients)):
            recipients[i] = recipients[i].replace('%40', '@')

        msgObject = flask_mail.Message(
            subject=subject,
            body=body,
            sender=sender,
            recipients=recipients
        )
        app = self.app
        with app.app_context():
            self.mail_obj.send(msgObject)