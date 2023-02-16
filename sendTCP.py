import socket


class TCPSender:
    def __init__(self, receiver_ip: str, receiver_port: int):
        self.receiver_ip = receiver_ip
        self.receiver_port = receiver_port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.receiver_ip, self.receiver_port))
    def close_connection_with_client(self):
        self.client_socket.close()

    def send_tcp_message(self, message):
        socket = self.client_socket
        socket.sendall(message.encode("utf-8"))


def main():
    sender = TCPSender("192.168.1.17", 12345)
    sender.send_tcp_message("elo")

if __name__ == "__main__":
    main()