import RPi.GPIO as GPIO
import time
import threading


LED_PIN = [5, 25, 24, 23, 22, 27]
PWM_FREQ = 100

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pwms = []

for i in range(len(LED_PIN)) :
    GPIO.setup(LED_PIN[i], GPIO.OUT)
    pwm = GPIO.PWM(LED_PIN[i], PWM_FREQ)
    pwm.start(0)
    pwms.append(pwm)

def update_motor(strength) :
    for i, s in enumerate(strength):
        pwms[i].ChangeDutyCycle(s * 40)

