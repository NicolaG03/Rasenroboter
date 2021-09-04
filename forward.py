import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

def forward():

    l = GPIO.PWM(11, 50)
    r = GPIO.PWM(7,50)

    l.start(0)
    r.start(0)
    print ("starting 0")
    time.sleep(3)

    l.ChangeDutyCycle(3)
    r.ChangeDutyCycle(3)
    print("start")
    time.sleep(5)



    while True:
        i = 6
        n = 6
        while i<10:
            r.ChangeDutyCycle(i)
            l.ChangeDutyCycle(n)
            time.sleep(.05)
               
GPIO.cleanup()