<h1 align="center">Neom</h1>

## 1. Project Architecture

<p align="center">
  <img src="Data/Neom.png" />
</p>

# 2. Train the YoloV7 Object Detection Model

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


# 3. Getting Started With Car Dash Board Application

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
# 4. Working Samples 

- For Video Demostration refer to the YouTube link <a href="">here.</a>

## GUI INTERFACE SAMPLES

<p align="center">
    <img src="Data/Screenshots/1.png" width="400">
    <img src="Data/Screenshots/4.png" width="400">
</p>

## THEME 1 (Detection and evaluation of the following elements on street imagery taken from a moving vehicle) :camera_flash:

Since visual pollution is a relatively recent issue compared to other forms of environmental
contamination, study is needed to define, formalize, measure, and evaluate it from many angles.
This competition aims to establish a new field of automated visual pollution classification,
utilizing the technological prowess of the twenty-first century for environmental management
applications.
By training and testing approaches to convolutional neural networks we expect competitors to
simulate the human learning experience in the context of picture identification for the
classification of visual pollutants.
Additionally this will be useful for the development of a "visual pollution score/index" for urban
areas that might produce a new "metric" or "indicator" in the discipline of urban environmental
management.
In this competition, you will build and optimize algorithms based on a large-scale dataset. This
dataset features the raw sensor camera inputs as perceived by a fleet of multiple vehicles in a
restricted geographic area in KSA
If successful, you’ll make a significant contribution towards stimulating further development city
planning and empowering communities around the world.


Visual pollution types:


● GRAFFITI
● FADED SIGNAGE
● POTHOLES
● GARBAGE
● CONSTRUCTION ROAD
● BROKEN_SIGNAGE
● BAD STREETLIGHT
● BAD BILLBOARD
● SAND ON ROAD
● CLUTTER_SIDEWALK
● UNKEPT_FACADE


## THEME 2 (Pothole severity classification via computer vision) :camera_flash:

SThe majority of current pavement condition assessment techniques are labor-intensive and
manual. Existing techniques for identifying and evaluating potholes rely on 3D surface
reconstruction, which is expensive in terms of both hardware and compute, or on acceleration
data, which only yields preliminary results. We are looking for teams to propose a low-cost
method for automatically identifying potholes and judging their severity using vision-based data
for both 2D and 3D reconstruction.


Utilizing the visual and spatial qualities of potholes as well as the measurement parameters
(width, quantity, and depth) that are used to estimate pothole severity, we would like to
understand how both 2D and 3D reconstruction can be combined to improve recognition results.
While the width and depth of the potholes are determined using 3D reconstruction, the number
and location of potholes is determined using 2D recognition.


Data gathering, distress identification and classification, and distress evaluation are the three
steps in the pavement assessment process. Modern data collection techniques are being quickly
replaced by inspection vehicles. These inspection vehicles can gather data at speeds of up to 60
mph (96 km/h), thanks to their numerous sensors, which include cameras for surface imaging,
optical sensors for distance measurement, laser scanners for profiling, ultrasonic sensors for
rutting detection, and accelerometers for roughness measurements. The second and third
processes of distress classification and assessment are still mostly manual despite the
automation of the data collection procedure. Currently, technicians manually examine the
collected data to determine the existence of distresses and gauge their severity from the
computer screen. Such a labor-intensive manual method might become unsystematic due to the
volume of data that needs to be collected, which eventually lowers the assessment's quality.
Although there are clear rules for manual diagnosis and assessment of asphalt distress, the
technicians' experience affects the assessment's outcome. A hybrid imaging device that
combines digital cameras and infrared lasers to capture continuous images of lines projected by
infrared lasers is based on 3D surface profiles from time-of-flight laser scanners to classify and
quantify pavement deterioration. These commercial software programs do not, however, count
or identify all the potholes that have been spotted.






