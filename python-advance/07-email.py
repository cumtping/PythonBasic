# coding=gbk
#!/usr/bin/python3

#����socket.error: [Errno 10061] http://blog.csdn.net/u014156690/article/details/52877727
#ԭ�򣺱���δ��װsendmail
#�����������װsendmail��ʹ�õ������ʼ��������ṩ��SMTP���ʣ�

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.163.com"  #���÷�����
mail_user="wenping0820@163.com"   #�û���
mail_pass="***"   #����

sender = 'wenping0820@163.com'
receivers = ['wenping0820@163.com']  # �����ʼ���������Ϊ���QQ���������������

# ������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� utf-8 ���ñ���
message = MIMEText('Python �ʼ����Ͳ���...', 'plain', 'utf-8')
message['From'] = Header("����̳�", 'utf-8')
message['To'] =  Header("����", 'utf-8')

subject = 'Python SMTP �ʼ�����'
message['Subject'] = Header(subject, 'utf-8')

try:
    #smtpObj = smtplib.SMTP('localhost')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 Ϊ SMTP �˿ں�
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("�ʼ����ͳɹ�")
except smtplib.SMTPException:
    print ("Error: �޷������ʼ�")