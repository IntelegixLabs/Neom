
from pathlib import Path
import os
from scipy.spatial import distance
import numpy as np
import time
import cv2
from datetime import datetime
import torch
import torch.backends.cudnn as cudnn
from numpy import random


from ..models.experimental import attempt_load
from ..utils.datasets import LoadStreams, LoadImages
from ..utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from ..utils.plots import plot_one_box
from ..utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

def AI_POT_HOLES_DETECTION():


    # #Initialize Pygame and load music
    # pygame.mixer.init()
    # pygame.mixer.music.load('Data/Models/audio/alert.wav')

    #Minimum threshold of eye aspect ratio below which alarm is triggerd
    EYE_ASPECT_RATIO_THRESHOLD = 0.3

    #Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
    EYE_ASPECT_RATIO_CONSEC_FRAMES = 50

    #COunts no. of consecutuve frames below threshold value
    COUNTER = 0


    net=cv2.dnn.readNet("best.pt")

    # labelsPath = "Data/Models/class.names"
    # classes = open(labelsPath).read().strip().split("\n")

    classes=["Potholes"]
    # maskNet = load_model(model_store_dir)

    #Start webcam video capture
    video_capture = cv2.VideoCapture("sections.mov")



    font = cv2.FONT_HERSHEY_SIMPLEX


    while(True):
        #Read each frame and flip it, and convert to grayscale
        ret, frame = video_capture.read()
        frame = cv2.flip(frame,1)
        (H, W) = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



        cv2.putText(frame, "INTELEGIX (Driver Monitoring System)", (110, 40),
                    font, 0.7*2, (255, 255, 255), 2)
        cv2.rectangle(frame, (20, 50), (W - 20, 15), (255, 255, 255), 2)
        # cv2.putText(img, "RISK ANALYSIS", (30, 85),
        #             font, 0.5, (255, 255, 0), 1)
        # cv2.putText(img, "-- GREEN : SAFE", (H-100, 85),
        #             font, 0.5, (0, 255, 0), 1)
        # cv2.putText(img, "-- RED: UNSAFE", (H-200, 85),
        #             font, 0.5, (0, 0, 255), 1)




        sub_img = frame[H - 100: H, 0:260]
        black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

        res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

        frame[H - 100:H+40, 0:260] = res

        cv2.putText(frame, (10, H - 80),
                    font, 0.5*2, (255, 255, 255), 1)
        cv2.putText(frame, (10, H - 55),
                    font, 0.5*2, (0, 255, 0), 1)
        cv2.putText(frame, (10, H - 30),
                    font, 0.5*2, (0, 120, 255), 1)
        cv2.putText(frame, (10, H - 5),
                    font, 0.5*2, (0, 0, 150), 1)

        now = datetime.now()
        # cv2.imwrite(str("Data/Saved_Images/CLASS_ENVIRONMENT/") + str(now.strftime("%Y%m%d%H%M%S") + str(".jpg")), img)

        # cv2.putText(img, str(now.strftime("%d-%m-%Y% %H:%M:%S")), (W-10, H - 5),
        #             font, 0.5, (0, 0, 150), 1)
        timex = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        cv2.putText(frame, timex, (W - 200, H - 10),
                    font, 0.5*2, (255, 255, 255), 1)

        ln=net.getLayerNames()


        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (224, 224), swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()
        # print("Frame Prediction Time : {:.6f} seconds".format(end - start))
        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > 0.1 and classID == 0:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)










        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        #print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[classIDs[i]])
                color = (0,0,255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y + 30), font, 3, color, 2)
                print(label)
                if str(label)==str("Cigarette"):
                    Cigarette="True"
                if str(label)==str("Mobile"):
                    Mobile="True"






        #Show video feed
        cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Output", frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    #Finally when video capture is over, release the video capture and destroyAllWindows
    video_capture.release()
    cv2.destroyAllWindows()

AI_DRIVER_MONITORING()
