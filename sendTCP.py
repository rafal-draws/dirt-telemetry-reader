import socket

def connect_to_client():
    receiver_ip = "192.168.1.17"
    receiver_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((receiver_ip, receiver_port))

    return client_socket


def send_tcp_message(client_socket, message):
    
    client_socket.sendall(message.encode("utf-8"))


def main():
    send_tcp_message("elo")

if __name__ == "__main__":
    main()