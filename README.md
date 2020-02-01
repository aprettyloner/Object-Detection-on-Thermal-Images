### Object-Detection-on-Thermal-Images
Robust Object Classification of Occluded Objects in Forward Looking Infrared (FLIR) Cameras using Ultralytics YOLOv3 and Dark Chocolate. <strong><em>Medium Article that compliments code repo:</em></strong> [Article on Medium](https://medium.com/@joehoeller/object-detection-on-thermal-images-f9526237686a)

#### Downloads needed to run codebase
  
   1. Download pre-trained weights here: [link](https://drive.google.com/drive/folders/1dV0OmvG4eZFtnh5WF0mby-jhkVy-HVco?usp=sharing)
   
   2. FLIR Thermal Images Dataset: [Download]https://www.flir.com/oem/adas/adas-dataset-form/

   3. Go into ```/data``` folder and unzip ```labels.zip```
   
   4. Addt'l instructions on how to run [Ultralytics Yolov3](https://github.com/ultralytics/yolov3)

#### Instructions

- Must have NVIDIA GPUs with CUDA X installed.

- The data provided by FLIR is included in the folder ```/coco/FLIR_Dataset```. 

- Place the custom pre-trained weights you downloaded from above into: ```/weights/*.pt``` 

- Converted labels from the [Dark Chocolate](https://github.com/joehoeller/Dark-Chocolate) repo are located in data/labels.

- The custom *.cfg with modified hyperparams is located in ```/cfg/yolov3-spp-r.cfg```.

- Class names and custom data is in ```/data/custom.names``` and ```custom.data```.


#### Install & Run Code:

After download is complete run pip install requirements, or click into the requriements.txt file for the Anaconda commands.
Install COCO: ``` bash yolov3/data/get_coco_dataset.sh```, then add FLIR images to: ```/coco/images/FLIR_Dataset```. Select any random grouping of non-annotated images, (ctrl-click any random sample of 5 to 10, or 20 if you like), copy them, and them paste them into data/samples folder.

- Go back to the root of the project where the requirements.txt file is and open a command prompt, run the following:

$  ```python3 detect.py --data data/custom.data --cfg cfg/yolov3-spp-r.cfg --weights weights/custom.pt```

- At the root of the project, you will then see a folder named output get generated with annotated images and bounding boxes around the objects within the images you chose for the ``data/samples`` folder.

- To get metrics, go back into command line at root of project and run: 

  $ ```python (python cmd prompt)```
  
  $ ```from utils import utils```
  
  $ ```utils.plot_results()```
  

You will then see an image of charts get generated at root of project called results.png

- To get class-wise scores run ( * Note that ```-r``` /yolov3-spp-r.cfg is the altered CNN architecture):

$ ```python3 test.py --cfg cfg/yolov3-spp-r.cfg --weights weights/custom.pt --data data/custom.data```


#### Need consulting to better understand computer vision implmentation for better business outcomes?
If Artifical Intelligence Applications are important to you or your business, please get in [touch](https://www.linkedin.com/in/computer-vision-engineer/) or email ```joehoeller@gmail.com```.

#### Consulting ideas on which this project could be forked to for real-word use cases:

- Object Classification in Thermal Images using Convolutional Neural Networks for Search and Rescue Missions with Unmanned Aerial Systems

- Defense and Aerospace: Detecting IDEs in live combat war zones

- Autonmous Cars or Drones

- Electrical grid monitoring


