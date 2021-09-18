#install library: sudo pip3 install pi-ina219
from ina219 import INA219
from ina219 import DeviceRangeError
import RPi.GPIO as GPIO

SHUNT_OHMS = 0.1
RELAIS_1_GPIO = 37 #GPIO ausfüllen

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

vtabel = [16.1,16.2,16.3,16.4,16.5,16.6,16.7,16.8,16.9,17,17.1,17.2,17.3,17.4,17.5,17.6,17.7,17.8,17.9,18,18.1,18.2,18.3,18.4,18.5,18.6,18.7,18.8,18.9,19,19.1,19.2,19.3,19.4,19.5,19.6,19.7,19.8,19.9,20,20.1,20.2,20.3,20.4,20.5,20.6,20.7,20.8,20.9,21]
ptabel = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100]

def measure():
    ina = INA219(SHUNT_OHMS)
    ina.configure()

    voltage = round(ina.voltage(),1)
    index = voltage.index(voltage)
    percent = ptabel(index)
    if voltage == 21:
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus   
    return percent

    