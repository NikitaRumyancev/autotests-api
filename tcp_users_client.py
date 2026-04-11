import socket


def tcp_client_up():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address_server = ("localhost", 12345)
    client_socket.connect(address_server)
    message = f"Привет, сервер!"
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(response)
    client_socket.close()


if __name__ == "__main__":
    tcp_client_up()