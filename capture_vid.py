import time
import cv2
import datetime
import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s')
capture_duration = 30
def record():
    capture = cv2.VideoCapture(1)
    if not capture.isOpened():
        logging.error("Webcam is not accessible")
        capture = cv2.VideoCapture(0)
        if not capture.isOpened():
            logging.error("Backup camera is also not accessible")
            return
    print(capture)
    start_time = time.time()
    file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    _, frame = capture.read() 
    height, width = frame.shape[:2] #frame.shape->(height, width, channel) 
    out = cv2.VideoWriter(file_name, fourcc, 8.0, (width, height))
    while int(time.time()-start_time) < capture_duration:
            ret, frame = capture.read()
            if ret:
                out.write(frame)
                print("writing new fram")
                #cv2.imshow("recording", frame)
            else:
                logging.error("Error reading frame from camera")
                break


    capture.release()
    out.release()
    cv2.destroyAllWindows()


