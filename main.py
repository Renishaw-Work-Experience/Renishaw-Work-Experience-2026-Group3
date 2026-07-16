import socket
import keyboard

def send_message(server_ip, port=5000, message="Hello from client!"):
    """Send a string message to the server."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, port))
            client_socket.sendall(message.encode('utf-8'))
            response = client_socket.recv(1024)
            print("Server replied:", response.decode('utf-8'))
    except Exception as e:
        print(f"Client error: {e}")

def recieve_message(host='127.0.0.1', port=5000):
    """Start a TCP server that listens for incoming strings."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(1024)  # Receive up to 1024 bytes
                if not data:
                    return None  # No data received
                else:
                    conn.sendall(b"Success")  # Send acknowledgment
                    return data.decode('utf-8')
    except Exception as e:
        print(f"Server error: {e}")

name = input("Enter 'c' or 's' to start client or server: ")
end = False
if name.lower() == 's':
    stop = False
    end = keyboard.is_pressed('q')
    while (not stop) and (not end):
        result = recieve_message()
        if result is not None:
            print("Received message:", result)
elif name.lower() == 'c':
    player = input("Enter 'r' or 'y': ")
    send_message("127.0.0.1", message=input(player+"C"))