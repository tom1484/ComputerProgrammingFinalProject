import RPi.GPIO as GPIO
import time
import threading

def runrunmotor(A) :
    LED_PIN = [23,24,25,5,6,26]
    PWM_FREQ = 100

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for i in range(len(LED_PIN)) :
        GPIO.setup(LED_PIN[i], GPIO.OUT)

    def runmotor(l,a) :
        pwm = GPIO.PWM(l, PWM_FREQ)
        pwm.start(0)
        pwm.ChangeDutyCycle(a*40)
        time.sleep(1)
        GPIO.output(l, False)

    threads = []
    for i in range(6) :
        threads.append(threading.Thread(target = runmotor, args = (LED_PIN[i], A[i],)))
        threads[i].start()

    pass

    for i in range(6) :
        threads[i].join()
