import time
import cv2
import datetime

capture_duration = 300
capture = cv2.VideoCapture(0)
start_time = time.time()
file_name = datetime.datetime.now.strftime("%Y-%m-%d_%H-%M-%S")+".mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(datetime.datetime.now()'mp4', fourcc, 15.0, (640,480))

while(int(time.time()-start_time) < capture_duration:
        ret, frame = cap_read()
        if ret:
            out.write(frame)
        else:
            print("Error with ret")
            break


capture.release()
out.release()
cv2.destroyAllWindows()
