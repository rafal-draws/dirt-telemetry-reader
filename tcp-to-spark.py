import socket


def send_tcp_message(message):
    receiver_ip = "192.168.1.17"
    receiver_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((receiver_ip, receiver_port))
    client_socket.sendall(message.encode("utf-8"))
    client_socket.close()


def main():
    send_tcp_message("elo")

if __name__ == "__main__":
    main()