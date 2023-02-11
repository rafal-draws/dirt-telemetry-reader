import socket
import time
import struct

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 20777

    sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(4096)

        values = extract_values(data)

        print("____________________")
        print(f"Time = {values[0]}")
        print(f"CurLap = {values[1]}")
        print(f"distancedrivenCurLap = {values[2]}")
        print(f"distanceDrivenOverall = {values[3]}")
        print(f"X = {values[4]}")
        print(f"Y = {values[5]}")
        print(f"Z = {values[6]}")
        print(f"Speed<m/s> = {values[7]}")
        print(f"RPM<rpm/10> = {values[37]}")
        print(f"velocityX = {values[8]}")
        print(f"velocityY = {values[9]}")
        print(f"G-Force Lateral = {values[34]}")
        print(f"G-Force Longitudinal= {values[35]}")



def extract_values(data):
    values = []
    i = 0
    offsets = [] # [0, 4, 8...]

    while i < 255:
        offsets.append(i)
        i += 4

    for offset in offsets:
        value = struct.unpack('f', data[offset:offset+4])[0]
        values.append(value)

    return values

while __name__ == "__main__":
    main()