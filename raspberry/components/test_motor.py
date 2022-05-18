from gpiozero import Servo
from time import sleep

servo = Servo(11)

while (True):
    servo.mid()
    sleep(5)
    servo.min()
    sleep(5)
    servo.max()
    sleep(2)