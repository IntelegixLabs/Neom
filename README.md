# Neom Application

### 1. Project Architecture

<p align="center">
  <img src="DATA/Neom.png" />
</p>


## Open Image Labelling Tool

```commandline
labelImg
```

## Train the custom Yolov7 Model

```commandline
python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt

```
