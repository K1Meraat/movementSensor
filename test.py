import time
from gpiozero import MotionSensor
from signal import pause
import asyncio
from bleak import BleakScanner
from gpiozero import MotionSensor
import capture_vid
import logging

#only include errors, write down the time, what kind of message, message content
logging.basicConfig(filename='errors.log', level=logging.ERROR,
                format='%(asctime)s - %(levelname)s - %(message)s')

#increas readability
safe = True
unsafe = False
capture_vid.record()
