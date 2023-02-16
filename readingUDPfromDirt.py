import socket
import time
import struct

from sendTCP import TCPSender

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 20777

    sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

    sock.bind((UDP_IP, UDP_PORT))

    

    while True:
        sender = TCPSender("192.168.1.17", 12345)
        
        data, addr = sock.recvfrom(4096)

        values = extract_values(data)

        print("____________________")

        #lap
        print(f"Time = {values[0]}")
        print(f"CurLap = {values[1]}")
        print(f"distancedrivenCurLap = {values[2]}")
        print(f"distanceDrivenOverall = {values[3]}")


        #geo
        print(f"X = {values[4]}")
        print(f"Y = {values[5]}")
        print(f"Z = {values[6]}")

        print(f"Speed<km/h> = {values[7] * 3600 / 1000}")


        # velocity
        print(f"velocityX = {values[8]}")
        print(f"velocityY = {values[9]}")
        print(f"velocityZ = {values[10]}")

        # roll vector
        print(f"rollX = {values[11]}")
        print(f"rollY = {values[12]}")
        print(f"rollZ = {values[13]}")

        # pitch vector
        print(f"pitchX = {values[14]}")
        print(f"pitchY = {values[15]}")
        print(f"pitchZ = {values[16]}")

        # suspension position
        print(f"RLsuspensionPosition = {values[17]}")
        print(f"RRsuspensionPosition = {values[18]}")
        print(f"FLsuspensionPosition = {values[19]}")
        print(f"FRsuspensionPosition = {values[20]}")

        # suspension velocity
        print(f"RLsuspensionVelocity = {values[21]}")
        print(f"RRsuspensionVelocity = {values[22]}")
        print(f"FLsuspensionVelocity = {values[23]}")
        print(f"FRsuspensionVelocity = {values[24]}")

        # wheel velocity
        print(f"RLwheelVelocity = {values[25]}")
        print(f"RRwheelVelocity = {values[26]}")
        print(f"FLwheelVelocity = {values[27]}")
        print(f"FRwheelVelocity = {values[28]}")


        # Steering
        print(f"Throttle = {values[29]}")
        print(f"Steer = {values[30]}")
        print(f"Brake = {values[31]}")
        print(f"Clutch = {values[32]}")
        print(f"Gear = {values[33]}")

        # G Force
        print(f"G-Force Lateral = {values[34]}")
        print(f"G-Force Longitudinal= {values[35]}")
        print(f"RPM = {values[37] * 10}")


        # Send message and close connection
        sender.send_tcp_message(f"Speed<km/h> = {values[7] * 3600 / 1000}")
        sender.close_connection_with_client()


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

if __name__ == "__main__":
    main()