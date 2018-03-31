from email.mime.text import MIMEText
from email.header import Header
import smtplib

def send_email(newest_file):
    with open(newest_file, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('163邮箱登录自动化测试报告', 'utf-8')
    msg['From'] = '17727820013@163.com'
    msg['To'] = '1554186085@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('17727820013@163.com', 'abc1234')
    smtp.sendmail('17727820013@163.com', '1554186085@qq.com', msg.as_string())
    smtp.quit()
    print('邮件已经发送！')


