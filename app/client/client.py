# client methods
from client.clientSocket import ClientSocket

class Client:
    def __init__(self, clientSocket: ClientSocket) -> None:
        self.clientSocket = clientSocket

    def send_message(self, message) -> None:
        self.clientSocket.socket.send(message)