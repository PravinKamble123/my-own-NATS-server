import threading
from .protocol import parse_message, generate_response

# Define a class to represent a connected client
class ClientHandler:
    def __init__(self, client_socket, server):
        self.client_socket = client_socket
        self.server = server
        self.username = None  # You can track client identities here

    def send_message(self, message):
        # Implement sending a message to the client
        try:
            self.client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message to {self.username}: {e}")
            # Handle the error, e.g., disconnect the client

    def receive_message(self):
        # Implement receiving a message from the client
        try:
            data = self.client_socket.recv(1024)
            if data:
                message = data.decode('utf-8')
                return message
            else:
                # Client disconnected
                return None
        except Exception as e:
            print(f"Error receiving message from {self.username}: {e}")
            # Handle the error, e.g., disconnect the client

    def handle_client(self):
        # Implement the main logic for handling the client's messages
        while True:
            message = self.receive_message()
            if message is None:
                # Client disconnected
                break

            # Process the received message based on your protocol
            parsed_message = parse_message(message)  # Implement your parsing logic
            if parsed_message:
                response = generate_response(parsed_message)  # Implement your response logic
                self.send_message(response)

    def start(self):
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=self.handle_client)
        client_thread.start()
