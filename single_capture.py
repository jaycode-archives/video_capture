import cv2
import pdb

def process_image(frame):
    return frame

def record():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(2)
    pdb.set_trace()
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", process_image(frame))
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

def test_cam():
    cams_test = 10
    for i in range(0, cams_test):
        cap = cv2.VideoCapture(i)
        test, frame = cap.read()
        print("i : "+str(i)+" /// result: "+str(test))

if __name__ == '__main__':
    record()