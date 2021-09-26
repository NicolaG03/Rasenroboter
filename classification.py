import imageClassification  as i
import paho.mqtt.client as mqtt #import the client1


if __name__ == '__main__':
	broker_address="localhost"
	#broker_address="iot.eclipse.org"
	client = mqtt.Client("ground") #create new instance
	print("new instance created")
	client.connect(broker_address) #conne
	print("connected to broker")

	while True:
		client.loop_start()
		result = i.classification()
		if result:
			msg = 'Gras'
		else:
			msg = 'kein Gras'

		client.publish("general/ground", msg)
		client.loop_stop()
