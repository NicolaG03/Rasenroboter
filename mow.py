import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

def mow():
    p = GPIO.PWM(13, 50)

    p.start(0)
    print ("starting 0")
    time.sleep(3)

    p.ChangeDutyCycle(3)
    print("start")
    time.sleep(5)

    while True:
        i = 6
        while i<10:
            p.ChangeDutyCycle(i)
            time.sleep(.05)
               
    GPIO.cleanup()
