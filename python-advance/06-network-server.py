# coding=gbk
#!/usr/bin/python3
# �ļ�����server.py

# ���� socket��sys ģ��
import socket
import sys

# ���� socket ����
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# ��ȡ����������
host = socket.gethostname()

port = 9999

# �󶨶˿�
serversocket.bind((host, port))

# ����������������������Ŷ�
serversocket.listen(5)

while True:
    # �����ͻ�������
    clientsocket,addr = serversocket.accept()      

    print("���ӵ�ַ: %s" % str(addr))
    
    msg='��ӭ���ʲ���̳̣�'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()