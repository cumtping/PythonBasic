# coding=gbk
#!/usr/bin/python3
# �ļ�����client.py

# ���� socket��sys ģ��
import socket
import sys

# ���� socket ����
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# ��ȡ����������
host = socket.gethostname() 

# ���ö˿ں�
port = 9999

# ���ӷ���ָ�������Ͷ˿�
s.connect((host, port))

# ����С�� 1024 �ֽڵ�����
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))