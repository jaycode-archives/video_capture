import cv2
import pdb
import os
from datetime import datetime

CAM_IDS = [1, 2]

# width x height
# default resolution is [640, 480]
RESOLUTION = (640/4, 480/4)

FPS = 5

STORAGE_PATH = "./storage"

def process_image(frame):
    return frame

def record(cam_ids, resolution):
    frames = cam_ids[:]
    vcs = cam_ids[:]
    out = cam_ids[:]

    filename_base = datetime.now().strftime("%Y%m%d_%H%M%S")

    counter = 0

    print("Start time: " + datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    for idx, cam_id in enumerate(cam_ids):
        dirname = filename_base + "-" + str(idx)
        fullpath = os.path.join(STORAGE_PATH, dirname)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)
        print("Save images to " + fullpath)
        out[idx] = fullpath
        cv2.namedWindow("preview" + str(idx))    
        vcs[idx] = cv2.VideoCapture(cam_id)
        vcs[idx].set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        vcs[idx].set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

        # Auto FPS doesn't work
        # vcs[idx].set(cv2.cv.CV_CAP_PROP_FPS, FPS)
        
        if vcs[idx].isOpened(): # try to get the first frame
            rval, frames[idx] = vcs[idx].read()
        else:
            rval = False


    start_time = datetime.now()
    while rval:
        cur_time = datetime.now()
        time_diff = (cur_time - start_time).total_seconds()
        if time_diff >= (1.0/FPS):
            start_time = cur_time
            for idx, cam_id in enumerate(cam_ids):
                # out[idx].write(process_image(frames[idx]))
                cv2.imwrite(os.path.join(out[idx], str(counter) + ".jpg"), frames[idx])
                cv2.imshow("preview" + str(idx), process_image(frames[idx]))
                rval, frames[idx] = vcs[idx].read()
            counter+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for idx, cam_id in enumerate(cam_ids):
        cv2.destroyWindow("preview" + str(idx))
        vcs[idx].release()
    print("End time: " + datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
        

def test_cam():
    cams_test = 10
    for i in range(0, cams_test):
        cap = cv2.VideoCapture(i)
        test, frame = cap.read()
        print("i : "+str(i)+" /// result: "+str(test))

if __name__ == '__main__':
    record(CAM_IDS, RESOLUTION)