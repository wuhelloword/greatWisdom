import socket


class TcpClient(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM    # 协议类型tcp
    allow_reuse_address = False
    max_packet_size = 8192      # 最大传输字节
    coding = 'gbk'      # 编码格式
    downloads_dir = r""     # 目录 待定变量

    def __init__(self, server_address, connect=True) -> None:
        self.server_address = server_address
        self.socket = socket.socket(self.address_family, self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise
    
    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            print('test run')
            pass

    def put(self, args, **kwargs):
        pass

if __name__ == '__main__':
    server_ip = '127.0.0.1'
    server_port = 8891
    server_add = (server_ip, server_port)
    _obj = TcpClient(server_add)
    _obj.run()