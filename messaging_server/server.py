import socket
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# Import other necessary modules like client_handler, protocol, and config

# Initialize server configuration (e.g., port, maximum connections)
from config import SERVER_ADDRESS, MAX_CONNECTIONS

# Initialize your custom protocol functions
from protocol import parse_message, generate_response

# Function to handle a single client connection
def handle_client(client_socket):
    try:
        # Perform the desired action upon client connection here
        # For example, send a welcome message
        welcome_message = "Welcome to the server!"
        client_socket.send(welcome_message.encode('utf-8'))

        # Logic to handle a single client's messages using your protocol
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by client
            message = data.decode('utf-8')
            parsed_message = parse_message(message)
            print("parsed_message", parse_message)
            response = generate_response(parsed_message)
            print("response", response)
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Cleanup and close the client socket
        client_socket.close()

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(MAX_CONNECTIONS)

# Create a thread pool for handling clients
with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
    while True:
        print("Server is listening for incoming connections...")
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Submit the client handling function to the thread pool
        executor.submit(handle_client, client_socket)
