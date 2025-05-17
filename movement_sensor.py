from time import sleep
from gpiozero import MotionSensor
from signal import pause

sleep(61) # to calibrate the sensor
pir = MotionSensor(13) #4th pin from left bottom
while True:
    
    pir.wait_for_motion()
    print("Motion Detected")
    pir.wait_for_no_motion()
    print("No Motion")
