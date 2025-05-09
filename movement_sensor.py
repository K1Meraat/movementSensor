import RPi.GPIO as GPIO
import timer

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15, False)
print("15 False")
sleep(1)
GPIO.output(15, True)
print("15 True")
sleep(1)
GPIO.cleanup()
