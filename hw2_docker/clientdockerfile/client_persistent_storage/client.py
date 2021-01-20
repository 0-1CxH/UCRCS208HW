import socket
import os

CLIENT_PORT = 7788

SERVER_IP = "172.71.0.2"
SERVER_PORT = 7789

BLOCK_SIZE = 1024

FILENAME = "MYDATA_CLIENT_COPY.txt"

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(("",CLIENT_PORT))
tcp_socket.connect((SERVER_IP, SERVER_PORT))

with open(FILENAME, "wb") as f:
    while True:
        block = tcp_socket.recv(BLOCK_SIZE)
        if(block):
            f.write(block)
        else:
            break
print("Transfer Completed.")

tcp_socket.close()

print("Client Connection Closed.")

print("MD5 Sum of File "+FILENAME+":")
os.system("md5sum "+FILENAME)