# create client interface
import tkinter
from client.client import Client

class ClientInterface():
    def __init__(self, client: Client) -> None:
        self.client = client

    # creates client window
    def create_client_window(self):
        window = tkinter.Tk()

        # window general settings
        window.title("Client")
        window.geometry("960x960")

        # labels for inputs
        tkinter.Label(window, text="Type the Server's IP").grid(column=0, row=0)
        tkinter.Label(window, text="Type the Server's Port").grid(column=0, row=1)
        tkinter.Label(window, text="Type your message").grid(column=0, row=2)

        # labels for inputs read-only

        tkinter.Label(window, text="Message sent (text)").grid(column=0, row=3)
        tkinter.Label(window, text="Message sent (binary)").grid(column=0, row=4)
        tkinter.Label(window, text="Message sent (binary and encrypted)").grid(column=0, row=5)

        # inputs
        server_ip_input = tkinter.Entry(window, width=40)
        server_port_input = tkinter.Entry(window, width=40)
        message_input = tkinter.Entry(window, width=40)

        # placeholders
        server_ip_input.insert(0, self.client.clientSocket.server_ip)
        server_port_input.insert(0, self.client.clientSocket.server_port)
        message_input.insert(0, "Hello, World!")

        # griding inputs
        server_ip_input.grid(column=1, row=0)
        server_port_input.grid(column=1, row=1)
        message_input.grid(column=1, row=2)

        # inputs read-only
        message_sent_t = tkinter.Label(window, text="")
        message_sent_b = tkinter.Label(window, text="")
        message_sent_b_e = tkinter.Label(window, text="")

        # griding read-only inputs
        message_sent_t.grid(column=1, row=3)
        message_sent_b.grid(column=1, row=4)
        message_sent_b_e.grid(column=1, row=5)

        # send button
        tkinter.Button(window, text="Send message", command=self.client.send_message).grid(column=2, row=2)

        window.mainloop()
    
