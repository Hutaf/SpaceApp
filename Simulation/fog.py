import mqttclient
from time import *
from gpio import *

broker_add ='192.168.0.100'						#Broker Address
username= 'user1'								#Username
password = '1234'								#Password
sub = 'waterLevel'
sub2 = 'temp'									#Subscription topic
sub3 = 'humidity'
waterList = []
tempList = []
humidityList = []
pinMode(0,OUT)
pinMode(1,OUT)
pinMode(2,OUT)

def on_connect(status, msg, packet):			#show connection status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	
def on_disconnect(status, msg, packet):			#show disconnection status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_subscribe(status, msg, packet):			#show subscription status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_unsubscribe(status, msg, packet):		#show unsubscription status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	

def on_publish(status, msg, packet):			#show publishing status
	if status == "Success" or status == "Error":
		print status + ": " + msg
	elif status == "":
		print msg
	
def on_message_received(status, msg, packet):  #Invoked when new message received
	# check received message and take action
	countW=0
	countT=0
	countH=0
	if status == "Success" or status == "Error":
		print status + ": " + msg
	
	elif status == "":
		msg2 = msg.split(":")
		print msg2
		
		if msg2[0]=='waterLevel':
			valueW = int(msg2[1])
			waterList.insert(countW,valueW)
			avgW = sum(waterList)/len(waterList)
			print avgW
			customWrite(0,avgW)
			print waterList
			countW=countW+1
		elif msg2[0]=='temp':
			valueT = int(msg2[1])
			tempList.insert(countT,valueT)
			avgT = sum(tempList)/len(tempList)
			print avgT
			customWrite(1,avgT)
			print tempList
			countT=countT+1
		elif msg2[0]=='humidity':
			valueH = int(msg2[1])
			humidityList.insert(countH,valueH)
			avgH = sum(humidityList)/len(humidityList)
			print avgH
			customWrite(2,avgH)
			print humidityList
			countH=countH+1
		#print msg
		
	
def main():
	
	mqttclient.init()

	mqttclient.onConnect(on_connect)
	mqttclient.onDisconnect(on_disconnect)
	mqttclient.onSubscribe(on_subscribe)
	mqttclient.onUnsubscribe(on_unsubscribe)
	mqttclient.onPublish(on_publish)
	mqttclient.onMessageReceived(on_message_received)
	print('Client Initialized')

	mqttclient.connect(broker_add,username,password)
	while not mqttclient.state()["connected"]:		#wait until connected
 		pass											#do nothing
 
	
	mqttclient.subscribe(sub)
	mqttclient.subscribe(sub2)
	mqttclient.subscribe(sub3)
	

	while True:
		delay(6000);
		
if __name__ == "__main__":
	main()