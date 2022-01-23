import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ServoPin = 4

GPIO.setup(ServoPin, GPIO.OUT)

p = GPIO.PWM(ServoPin, 50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5) #turn 90 degree
        print("90 deg")
        time.sleep(1)
        print("0 deg")
        p.ChangeDutyCycle(2.5) #turn 0 deg
        time.sleep(1)
        print("180 deg")
        p.ChangeDutyCycle(12.5) #turn 180 degrees
        time.sleep(1)
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
