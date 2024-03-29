# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
gpio_pin = 11
GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.setwarnings(False)
servo1 = GPIO.PWM(gpio_pin, 50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #Ask user for angle and turn servo to it
        duty_cycle = float(input('Enter duty cycle: '))
        #duty_cycle = 13
        servo1.ChangeDutyCycle(9)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(4)

finally:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")
