import time
import cv2
import datetime
import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s')
capture_duration = 300
def record():
    capture = cv2.VideoCapture(0)
    if not caputre.isOpened():
        logging.error("Webcam is not accessible")
        capture = cv2.VideoCapture(1)
        if not caputre.isOpened():
            logging.error("Backup camera is also not accessible")
            return
    start_time = time.time()
    file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(datetime.datetime.now()'mp4', fourcc, 15.0, (640,480))
    while(int(time.time()-start_time) < capture_duration:
            ret, frame = cap_read()
            if ret:
                out.write(frame)
                cv2.imshow("recording", frame)
            else:
                logging.error("Error reading frame from camera")
                break


    capture.release()
    out.release()
    cv2.destroyAllWindows()
