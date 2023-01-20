<h1 align="center">Neom</h1>

## 1. Project Architecture

<p align="center">
  <img src="Data/Neom.png" />
</p>

# Train the YoloV7 Object Detection Model

## Open Image Labelling Tool

```commandline
labelImg
```

## Add more data from the already labelled images

```
git clone https://github.com/IntelegixLabs/smartathon-dataset
cd smartathon-dataset
Add train,val, and test data to Neom/yolov7-custom/data files 
```

## Train the custom Yolov7 Model

```commandline
git clone https://github.com/IntelegixLabs/Neom
cd Neom
cd yolov7-custom
pip install -r requirements.txt
pip intsall -r requirements_gpu.txt
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt

```


# Getting Started

- Clone the repo and cd into the directory
```sh
$ git clone https://github.com/raj713335/Neom.git
$ cd Neom
$ cd Neom_App
```
- Download the Trained Models and Test_Video Folder from google Drive link given below and extract it inside Neom_App Folder
- https://drive.google.com/file/d/1YXf8kMjowu28J5Z_ZPXoRIDABRKzmHis/view?usp=sharing

```sh
$ wget https://drive.google.com/file/d/1YXf8kMjowu28J5Z_ZPXoRIDABRKzmHis/view?usp=sharing
```

- Install Python 3.10 and its required Packages like PyTorch etc.

```sh
$ pip install -r requirements.txt
$ pip intsall -r requirements_gpu.txt
$ pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
```

- Run the app

```sh
$ python home.py
```


## Packaging the Application for Creating a Execulatle exe File that can run in Windows,Linus,or Mac OS

You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.
for reference read the pyinstaller documentation <a href="https://pyinstaller.readthedocs.io/en/stable/usage.html">here.</a>

```sh
$ pyinstaller -i "favicon.ico" --onefile -w --hiddenimport=EasyTkinter --hiddenimport=Pillow  --hiddenimport=opencv-python --hiddenimport=requests--hiddenimport=Configparser --hiddenimport=PyAutoGUI --hiddenimport=numpy --hiddenimport=pandas --hiddenimport=urllib3 --hiddenimport=tensorflow --hiddenimport=scikit-learn --hiddenimport=wget --hiddenimport=pygame --hiddenimport=dlib --hiddenimport=imutils --hiddenimport=deepface --hiddenimport=keras --hiddenimport=cvlib --name Neom home.py
```



