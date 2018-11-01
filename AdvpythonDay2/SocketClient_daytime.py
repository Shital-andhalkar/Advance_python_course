"""tcp client"""
import socket

try:
    server_address='localhost',9090
    sock=socket.socket()
    sock.connect(server_address)
    payload=sock.recv(2048)

    print(payload.decode('ascii'))

finally:
    sock.close()