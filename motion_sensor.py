from time import sleep
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
mac_address = "38:E1:3D:9F:2D:15"
#doesn't automatically disconnect after the block ends!
#async def find_device(mac_address):
#    try:
#        print(f"scanning for {mac_address}...")
#        devices = await BleakScanner.discover(timeout=10.0)
#        for d in devices:
#            if mac_address in str(d):
#                print(f"found{d}")
#                return safe
#    except Exception as e:
#        logging.error(f"unexpected happend i find_device: {e}")

async def manual_connect(mac_address):
    client = BleakClient(mac_address)
    try:
        await client.connect(timeout=10.0)
        if client.is_connected:
            print(f"Trusted device {mac_address} within range\n")
            return safe
    except Exception as e:
        logging.error(f"No trusted device discovered: {e}")
        return unsafe
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    if asyncio.run(manual_connect(mac_address)) == unsafe:
        print("k1 not found!")
        capture_vid.record()
    pir.wait_for_no_motion()
    print("No Motion")

    #except Exception as e:
    #    logging.error(f"unexptected error in motion loop: {e}")
