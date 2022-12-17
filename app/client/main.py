from client.clientSocket import ClientSocket
from client.client import Client
from client.clientInterface import ClientInterface

from lib.env import get_env_info

def run_client():
    # loads environment information
    env = get_env_info()
    # create socket
    clientSocket = ClientSocket(env.get("SERVER_IP"), env.get("SERVER_PORT"))
    # create client
    client = Client(clientSocket)
    # create window
    clientInterface = ClientInterface(client)
    # establish connection
    clientInterface.create_client_window()

def main():
    print("running client...")
    
    run_client()
