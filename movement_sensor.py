from gpiozero import MotionSensor
from signal import pause


pir = MotionSensor(2)

pir.wait_for_motion()
print("Motion Detected")

