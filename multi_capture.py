import cv2
import pdb

CAM_IDS = [1, 2]

def process_image(frame):
    return frame

def record(cam_ids):
    frames = cam_ids[:]
    vcs = cam_ids[:]
    for idx, cam_id in enumerate(cam_ids):
        cv2.namedWindow("preview" + str(idx))    
        vcs[idx] = cv2.VideoCapture(cam_id)
        if vcs[idx].isOpened(): # try to get the first frame
            rval, frames[idx] = vcs[idx].read()
        else:
            rval = False


    while rval:
        for idx, cam_id in enumerate(cam_ids):
            cv2.imshow("preview" + str(idx), process_image(frames[idx]))
            rval, frames[idx] = vcs[idx].read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    for idx, cam_id in enumerate(cam_ids):
        cv2.destroyWindow("preview" + str(idx))
        vcs[idx].release()
        

def test_cam():
    cams_test = 10
    for i in range(0, cams_test):
        cap = cv2.VideoCapture(i)
        test, frame = cap.read()
        print("i : "+str(i)+" /// result: "+str(test))

if __name__ == '__main__':
    record(CAM_IDS)