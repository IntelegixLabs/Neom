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


from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

def AI_IMAGE_CLASSIFICATION(source="0"):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(device)
    weights = "visual_pollution-e6e.pt"
    print(weights)
    img_size = 640
    iou_thres = 0.4
    conf_thres = 0.4

    image_class = {'GRAFFITI': 0, 'FADED_SIGNAGE': 1, 'POTHOLES': 2, 'GARBAGE': 3,
                   'CONSTRUCTION_ROAD': 4, 'BROKEN_SIGNAGE': 5, 'BAD_STREETLIGHT': 6,
                   'BAD_BILLBOARD': 7, 'SAND_ON_ROAD': 8, 'CLUTTER_SIDEWALK': 9,
                   'UNKEPT_FACADE': 10}

    res = []
    confidence = 0

    webcam = source.isnumeric()

    # Initialize
    set_logging()
    device = select_device(device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(img_size, s=stride)  # check img_size

    if half:
        model.half()  # to FP16

    # Set Dataloader
    if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    old_img_w = old_img_h = imgsz
    old_img_b = 1

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Warmup
        if device.type != 'cpu' and (
                old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
            old_img_b = img.shape[0]
            old_img_h = img.shape[2]
            old_img_w = img.shape[3]

        with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
            pred = model(img)[0]

        # Apply NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres)

        # Process detections
        for i, det in enumerate(pred):  # detections per image

            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)


            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    label = f'{names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

                    label = f'{names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)
                    print(names[int(cls)], xyxy)
                    print((int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])))
                    name = names[int(cls)].replace(" ","_")
                    if confidence < conf:
                        res = [[image_class[name], source.split("/")[1], name, (int(xyxy[2]))//2,
                                (int(xyxy[0]))//2, (int(xyxy[3]))//2, (int(xyxy[1]))//2 ]]
                        confidence = conf


            # Print time (inference + NMS)





            # cv2.imshow("Output", im0)
            # cv2.waitKey(1)

            return res


            # if (cv2.waitKey(1) & 0xFF == ord('q')):
            #     break

if __name__ == '__main__':
    import csv
    with torch.no_grad():
        i = 0

        with open('test.csv', mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            for lines in csvFile:
                i += 1
                if i == 1:
                    continue
                # if i == 10:
                #     exit(0)

                res = (AI_IMAGE_CLASSIFICATION("Test_Dataset/"+lines[0]))
                print(i, res, "res")

                if len(res) == 0:
                    res = [[0,lines[0],"GRAFFITI",0,0,0,0]]
                with open(r'../Neom_App/ENGINES/sample_submission.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    for each in res:
                        writer.writerow(each)