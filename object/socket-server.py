#coding=utf-8
#服务端

#导入socket模块
import socket

#创建 socket对象
s = socket.socket()
#绑定端口
s.bind(("127.0.0.1",8888))

#等待客户端连接
s.listen(6)

while True:
    # 建立客户端连接
    c, addr = s.accept()
    print("连接地址：",addr)
    c.send('Welcome'.encode("utf-8"))
    #关闭连接
    c.close()