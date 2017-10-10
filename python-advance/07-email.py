# coding=gbk
#!/usr/bin/python3

#报错socket.error: [Errno 10061] http://blog.csdn.net/u014156690/article/details/52877727
#原因：本机未安装sendmail
#解决方法：安装sendmail或使用第三方邮件服务器提供的SMTP访问；

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.163.com"  #设置服务器
mail_user="wenping0820@163.com"   #用户名
mail_pass="***"   #口令

sender = 'wenping0820@163.com'
receivers = ['wenping0820@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    #smtpObj = smtplib.SMTP('localhost')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")