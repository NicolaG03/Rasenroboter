import os
from pathlib import Path
from typing import ForwardRef
import RPi.GPIO as GPIO
#import abstand_1
#import abstand_2
#import abstand_4
#import measure
import paho.mqtt.client as mqtt #import the client1
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def on_message(client, userdata, message):
    global ret_out 
    print("message received " ,str(message.payload.decode("utf-8")))
    ret_out = str(message.payload.decode("utf-8"))

def pub_sensors():
    while True:
        distL = round(abstand_2.auslesen(), 3)
        distR = round(abstand_1.auslesen(),3)
        distF = round(abstand_4.auslesen(),3)
        bat = measure.measure()

        client.publish("distSens/sensL", str(distL))
        client.publish("distSens/sensR", str(distR))
        client.publish("distSens/sensF", str(distF))
        client.publish("general/bat", str(bat))

        time.sleep(0.25)

class threadClass:   
    def __init__(self, execfunc):
        self._running = False
        self.func = execfunc
        self.resetGPIO = True

    def start(self):
        print('start thread')
        self._running = True

    def terminate(self):
        print('thread terminated')
        self._running = False
      
    def run(self):
        print('thread initialized')
        if(self.func == 'forward'):
            while True:
                time.sleep(0.25)
                if self._running:
                    print('start')
                    self.resetGPIO = True
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(11, GPIO.OUT)
                    GPIO.setup(7, GPIO.OUT)
                    fl = GPIO.PWM(11, 50)
                    fr = GPIO.PWM(7,50)

                    fl.start(0)
                    fr.start(0)
                    print ("starting 0")
                    time.sleep(1)
                    fl.ChangeDutyCycle(3)
                    fr.ChangeDutyCycle(3)
                    print("start")
                    time.sleep(2)

                while self._running:
                    fr.ChangeDutyCycle(6)
                    fl.ChangeDutyCycle(6)
                    time.sleep(0.05)
                if self.resetGPIO:
                    del fl
                    del fr
                    print('mrProper')
                    self.resetGPIO = False
        elif(self.func == 'mowing'):
            while True:
                time.sleep(0.25)
                if self._running:
                    self.resetGPIO = True
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(13, GPIO.OUT)
                    p = GPIO.PWM(13, 50)
                        
                    p.start(0)
                    print ("starting 0")
                    time.sleep(1)
                    p.ChangeDutyCycle(3)
                    time.sleep(2)
                    print("start")

                while self._running:
                    p.ChangeDutyCycle(6)
                    time.sleep(0.05)

                if self.resetGPIO:
                    del p
                    print('mrProper')
                    self.resetGPIO = False


        elif(self.func == 'left'):
            while True:
                time.sleep(0.25)
                if self._running:
                    self.resetGPIO = True
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(11, GPIO.OUT)                
                    l = GPIO.PWM(11,50)
                    l.start(0)
                    print ("starting 0")
                    time.sleep(1)
                    l.ChangeDutyCycle(3)
                    print("start")
                    time.sleep(2)
                while self._running: #(momentanwert != schlusswert)
                    l.ChangeDutyCycle(6)
                    time.sleep(0.05)
                if self.resetGPIO:
                    del l
                    self.resetGPIO = False
        elif(self.func == 'right'):
            while True:
                time.sleep(0.25)
                if self._running:
                    self.resetGPIO = True
                    GPIO.setmode(GPIO.BOARD)
                    GPIO.setup(7, GPIO.OUT)
                    r = GPIO.PWM(7, 50)
                    r.start(0)
                    print ("starting 0")
                    time.sleep(1)
                    r.ChangeDutyCycle(3)
                    print("start")
                    time.sleep(2)  
                while self._running: #(momentanwert != schlusswert)
                    r.ChangeDutyCycle(6)
                    time.sleep(0.05)
                if self.resetGPIO:
                    del r
                    print('mrProper')
                    self.resetGPIO = False
                #sGPIO.cleanup()  

if __name__ == '__main__':  
    #init()
    control_mow = threadClass('mowing')
    control_forward = threadClass('forward')
    control_left = threadClass('left')
    control_right = threadClass('right')
    
    thread_mow = threading.Thread(target=control_mow.run)
    thread_forward = threading.Thread(target=control_forward.run)
    thread_left = threading.Thread(target=control_left.run)
    thread_right = threading.Thread(target=control_right.run)

    ret_out = ''
    forwardState = False
    leftState = False
    rightState = False
    mowingState = False
    sensState = False

    execMow = True
    execForward = True
    execLeft = True
    execRight = True
    #thread_ground.start()
    broker_address="localhost"
    #broker_address="iot.eclipse.org"
    client = mqtt.Client("main") #create new instance
    print("new instance created")
    client.on_message=on_message #attach function to callback
    client.connect(broker_address) #conne
    print("connected to broker")
    client.subscribe("dart/drive")

    while True:
        client.loop_start()
        

        if ((ret_out == 'forward') and (not leftState) and (not rightState) and (not mowingState)):
            if not forwardState:
                forwardState = True
                control_forward.start()
                if execForward:
                    thread_forward.start()
                    execForward = False
                print('activate forward thread')
            else:
               # stpbl_forward.stop()
                forwardState = False
                control_forward.terminate()
                print('deactivate forward thread')

        if ((ret_out == 'left') and (not forwardState) and (not rightState) and (not mowingState)):
            if not leftState:
                leftState = True
                control_left.start()
                if execLeft:
                    thread_left.start()
                    execLeft = False
                print('activate left thread')
            else:
                leftState = False
                control_left.terminate()
                print('deactivate left thread')

        if ((ret_out == 'right') and (not forwardState) and (not leftState) and (not mowingState)):
            if not rightState:
                rightState = True
                control_right.start()
                if execRight:  
                    thread_right.start()
                    execRight = False
                print('activate right thread')
            else:
                rightState = False
                control_right.terminate()
                print('deactivate right thread')

        if ret_out == 'mowing':
            if not mowingState:
                control_mow.start()
                if execMow:
                    thread_mow.start()
                    execMow = False
                mowingState = True
                print('activate mowing thread')
            else:         
                mowingState = False
                control_mow.terminate()
                print('deactivate mowing thread')
        
        ret_out = ''
        client.loop_stop()
    #client.loop_stop() #stop the loop
