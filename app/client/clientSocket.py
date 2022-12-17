# establish and end connection with the server
import socket

class ClientSocket:
    # handle IP, PORT and creates the socket
    def __init__(self, server_ip, server_port) -> None:
        self.server_ip = server_ip
        self.server_port = server_port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # estabilishe connection with the server
    def establish_connection(self) -> None:
        self.socket.connect((self.server_ip, self.server_port))
    
    # end connection with the server
    def end_connection(self) -> None:
        self.socket.close()
