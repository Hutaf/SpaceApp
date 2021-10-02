from realtcp import *
from time import *

serverIP = "127.0.0.1"
serverPort = 1334
received = False
result = None;
	
def onTCPReceive(data):						# Callback function to handel receiving
	print("received Result: " + data);
	result = int(data)
	received = True
	
def send(data):
	client = RealTCPClient()
	client.onReceive(onTCPReceive)
	client.connect(serverIP, serverPort)
	while not client.connected():			# Wait for connection to be established
		pass
	
	client.send(data)
											# Send data
	#while not received:						# Wait to receive response
	#	sleep(1)
	return result							# return results to caller			
