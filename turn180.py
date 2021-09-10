import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def turn180(direction):
    if direction == ("right"):
        #schlusswert = momentanwert + 180
        p = GPIO.PWM(11, 50)

    elif direction ==("left"):
        #schlusswert = momentanwert - 180
        p = GPIO.PWM(7,50)
        
    p.start(0)
    print ("starting 0")
    time.sleep(3)

    p.ChangeDutyCycle(3)
    print("start")
    time.sleep(5)



    while True: #(momentanwert != schlusswert)
        i = 6.5
        while i<10:
        
            print(i)
            p.ChangeDutyCycle(i)
            time.sleep(.05)