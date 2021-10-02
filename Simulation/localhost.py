import socket
import sys
from matplotlib import pyplot as plt

host = ""
port = 1334
waterLevel = []
Temperature = []
humidtiy = []

mySocket = socket.socket()
mySocket.bind((host, port))  # Bind to localhost:1234

mySocket.listen(1)  # Wait for a connection
while True:
    print("Listening...")
    while True:
        conn, addr = mySocket.accept()  # If new connection receives, return conn obj
        # print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()  # Receive data (buffer size 1024 bytes)
        # print ("Received Data is: " + str(data))
        data2 = data.split(":")
        if data2[0] == 'water':
            valueW = int(data2[1])
            if (valueW > 0):
                print ("Dust over the panel")
            waterLevel.insert(0, valueW)
            
        elif data2[0] == 'temp':
            valueT = int(data2[1])
            Temperature.insert(0, valueT)
            
            print("Neighborhood: ")
            print(Temperature)
        elif data2[0] == 'humidity':
            valueH = int(data2[1])
            humidtiy.insert(0, valueH)
            
            print("House: ")
            print(humidtiy)
        elif str(data) == "exit":
            conn.close()
            break;
        elif len(humidtiy) == 100:
            conn.close()
            break;
                # Send data back.
    conn.close()  # Close connection
    sys.exit()