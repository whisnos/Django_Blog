# coding: utf-8
# Author: www.debug5.com
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# 实例化一个select 这个类会根据我们的平台 自动选择，如果再Windows自动选择select，在Linux会选择epoll
selector = DefaultSelector()


class Fetcher:
    def connected(self, key):
        # 这个key就是传进来的文件描述符
        self.client.send("GET {} HTTP/1.1 Host:{} Connection:close ".format("/", self.host).encode("utf8"))
        # 因为发送后，我们又需要注册一个事件，
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 因为没有数据了，就需要去释放socket
            selector.unregister(key.fd)
            self.data = self.data.decode("utf8")

    def get_url(self, url):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置为非阻塞的socket
        self.client.setblocking(False)
        self.host = "www.debug5.com"
        self.data = b""
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            print("做了一些事")
            pass
        # 注册一个事件
        # 参数说明，
        # 第一个参数 哪个socket，
        # 第二个参数 因为一旦连接上 就要进行send 这时候是等待可写操作，
        # 第三个参数 可写了之后调用这个方法 注意咯：这个self.connected 系统无法帮我们进行，是需要我们自己来调用，后面会讲
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
