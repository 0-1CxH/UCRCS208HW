import socket

CLIENT_PORT = 7788

SERVER_PORT = 7789

BLOCK_SIZE = 1024

FILENAME = "MYDATA.txt"


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(("",SERVER_PORT))
tcp_socket.listen(128)
print("Server Now Listening At:",SERVER_PORT)

while True:
    accept_socket, client_addr = tcp_socket.accept()
    print("Connection Accepted:", client_addr)
    with open(FILENAME, "rb") as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if(block):
                accept_socket.send(block)
            else:
                break
    accept_socket.close()
    print("Transfer Completed.")



tcp_socket.close()



