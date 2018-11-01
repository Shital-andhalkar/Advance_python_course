from socketserver import TCPServer, BaseRequestHandler
from time import ctime

class CustomRequestHandler(BaseRequestHandler):
    def handle(self):
        client_addr=self.client_address
        print('recv request from :',client_addr)
        ts=ctime().encode('ascii')
        self.request.sendall(ts)

def main():
    server_address = ('localhost', 9090)
    server = TCPServer(server_address, CustomRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

