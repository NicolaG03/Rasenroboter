import paho.mqtt.client as mqtt #import the client1
import time
import abstand_1
import abstand_2
import abstand_4
import measure

if __name__ == '__main__':
    broker_address="localhost"
    #broker_address="iot.eclipse.org"
    client = mqtt.Client("sensors") #create new instance
    print("new instance created")
    client.connect(broker_address) #conne
    print("connected to broker")

    while True:
        client.loop_start()
        distL = round(abstand_2.auslesen(), 3)
        distR = round(abstand_1.auslesen(),3)
        distF = round(abstand_4.auslesen(),3)
        bat = measure.measure()

        client.publish("distSens/sensL", str(distL))
        client.publish("distSens/sensR", str(distR))
        client.publish("distSens/sensF", str(distF))
        client.publish("general/bat", str(bat))

        time.sleep(0.25)

        client.loop_stop()