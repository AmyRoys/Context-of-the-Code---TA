import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    try:
        while True:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()