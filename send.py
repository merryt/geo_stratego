import socket

UDP_IP = "192.168.1.26"
UDP_PORT = 5005
MESSAGE = b"Hello, world"

print(f"UDP target IP: {UDP_IP}, on port: {UDP_PORT}")
print(MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
