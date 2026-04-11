import socket


history_cl_messages = []


def tcp_server_up():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        client_message = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {client_message}")
        history_cl_messages.append(client_message)
        client_socket.send('\n'.join(history_cl_messages).encode())
        client_socket.close()


if __name__ == "__main__":
    tcp_server_up()
