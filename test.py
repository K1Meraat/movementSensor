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
async def find_device(mac_address):
        print(f"scanning for {mac_address}...")
        devices = await BleakScanner.discover(timeout=10.0)
        for d in devices:
            print(d)


asyncio.run(find_device(address))
