from emailsender import EmailSender

sender = EmailSender()

def verify_email(email):
    sender.send_email(
        'CrowdLabel 邮箱验证'
        '验证码：xxxxxx',
        'noreply@crowdlabel.org',
        email
    )