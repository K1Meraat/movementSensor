import time
from gpiozero import MotionSensor
from signal import pause
import asyncio
from bleak import BleakClient
from gpiozero import MotionSensor
import capture_vid
import logging

#only include errors, write down the time, what kind of message, message content
logging.basicConfig(filename='errors.log', level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s')

#increas readability
safe = True
unsafe = False
#sleep(61) # to calibrate the sensor
pir = MotionSensor(13) #4th pin from left bottom

#address of the trusted phone(bluetooth)
address = "38:E1:3D:9F:2D:15"
#doesn't automatically disconnect after the block ends!
async def manual_connect():
    client = BleakClient(address)
    try:
        #waits until timeout or connected
        await client.connect()
        if client.is_connected:
            print(f"trusted device {address} within the range" \n)
            return safe
    except Exception as e:
        logging.error("no trusted device is discovered")
        return unsafe
while True:
    try: 
        pir.wait_for_motion()
        print("Motion Detected")
        if asyncio.run(manual_connect()) == unsafe:
            capture_vid.record()
        pir.wait_for_no_motion()
        print("No Motion")

    except Exception as e:
        logging.error(f"unexptected error in motion loop: {e}")
