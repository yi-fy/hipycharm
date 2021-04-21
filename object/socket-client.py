# coding: utf-8
#导入socket模块
import socket

#创建socket对象
s = socket.socket()

#连接服务器
s.connect(("127.0.0.1",8888))
print(s.recv(1024).decode("utf-8"))
s.close()