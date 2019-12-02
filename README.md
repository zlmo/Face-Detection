

#  Face detection based on Darknet and Wider Face dataset

This project aims to realise face detection based on darknet and Wider Face dataset,incluing:
	
- Modify the official methods yolov2, yolov3, yolov2-tiny and etc.,and train them on Wider Face training set.
- Training my own face detection method on Wider Face training set.
- Evaluating these methods on Wider Face validation set.
- Detecting faces by using these methods.

## 1. Clone the project.
First, clone this project using git:
		`git clone https://github.com/zlmo/Face-Detection.git`
modify Makefile accordding to your device and make.

## 2. Prepare Wider Face dataset.
Then, we need to prepare the training set first. This includes downloading the dataset and transferring it to darknet style.

### a. Download and extract Wider Face dataset
Download link can be found here: 									http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/
**WIDER_train.zip, WIDER_val.zip and wider_face_split.zip** are needed at least.

Once downloading completed, extract **WIDER_train.zip**, **WIDER_val.zip** and **wider_face_split.zip** to '/darknet'

	unzip WIDER_train.zip -d ./darknet 
	unzip WIDER_val.zip -d ./darknet 
	unzip wider_face_split.zip -d ./darknet

### b. Transfer Wider Face to darknet style
When we use Wider Face to train our networks, we need to transfer the dataset to darknet style. The official darknet project use Pascal VOC style, so we transfer Wider Face to Pascal VOC style.
I have write the python file to transfer, just run it!

`python widerface_label.py`

This file will do the following things:
 - **Make the directories:** /WIDER_FACE_VOC/VOC2007/VOCdevkit/JPEGImages
/ WIDER_FACE_VOC/VOC2007/VOCdevkit/Labels
 - **Generate training images.** . Copy the training images from each branch of WIDER_train and integrate them together in /JPEGImages
 - **Generate training labels.** 
The original format of the annotations of Wider Face is:
	      ... 
              < image name i >  
              < number of faces in this image = im > 
              < bounding box of face i1: left, top, width, height > 
              < bounding box of face i2: left, top, width, height > 
              ... 
              < bounding box of face im: left, top, width, height > 
              ... 
and darknet wants a .txt file as label for each image, each line for each ground truth object in the image looks like:
              <object-class> <x> <y> <width> <height>
Where x, y, width, and height are relative to the image's width and height. 
 - **Modify some valid labels.**
There are some valid images in Wider Face whose bounding box annotations has values less than 0. The annotation value of x, y, width and height must more than 0, a value less than zero will lead to 'segmentation fault'. So we need to check all the annotations to make sure all values are more than 0. Once a value is checked to less than 0, it will be forced to set to 0.001.
 - **Generate the training images list.** Generate the training list of the whole training dataset: train.txt.
  
## 2. Train with  yolov2, yolov3, yolov2-tiny-voc and etc.
Once the dataset has been prepared okay, we can start to train the network for face detection. 
When use the official yolo-like networks for face detection, we need to do some modifications:
  
 - Write widerface.data under '/cfg'.
 - Write widerface.names under '/data'
 - Set class numbers of these networks to 1.
 - Set filter numbters of the last conv layer to 30 for yolov2 and 18 for yolov3, which is the layer on top of 'region layer' and 'yolo layer'.
  After the above modifications, we can start to train:
  
`./darknet detector train cfg/widerface.data cfg/yolov2-tiny-voc.cfg darknet.conv.13`     

  This is trained use yolov2-tiny-voc.cfg, and the pre-trained weights darknet.con.13 can be found here in BaiduYun:
    	Link: https://pan.baidu.com/s/1QThdiQqAUFX6XYyFtTyF8Q Extraction code: j1fr 

  And some trained networks can be found here (These networks may have some little changes compare to original networks):
  face_small_3
  	Link: https://pan.baidu.com/s/1WrYsByjLbjT1B6B-H_Y8sg Extraction code: sa4h
  face_small_6
  	Link: https://pan.baidu.com/s/18a907k6z2ZqRofosgfB3lg Extraction code: q8d9
  face_v2
  	Link: https://pan.baidu.com/s/1vG1H_FoNNcRKqdlvpmV-Qw Extraction code: 5izm
     
## 3.My face detection method resface_slim:A fast and lightweight method with feature fusion and multi-context for face detection 
  The cfg file of this network is resface_slim.cfg. This network is a fast lightweight face detection network with feature fusion and context,its mainly architecture includes:(1)taking resnet18 as backbone;(2)feature fusion adopted from FPN;(3)multi-context,adding both local context and global context to the feature maps, and the local context is added by a depthwise separable convolution way to reduce computation.The architecture and the cnotext module is shown below:
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/resface/Figure3.png"/>
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/resface/Figure4.png"/>

    ./darknet detector train cfg/widerface.cfg cfg/resface_slim.cfg resnet18.conv.25
There's a little difference from the figure, I modified the local context to make it faster. And the pre-trained weights of resface_slim can be found here:
	链接: https://pan.baidu.com/s/1OUh8cJbRmEd1M3rvpph11Q 密码: f4r8
  
## 4. Evaluated on Wider Face validation set
We use toolkit from official website of Wider Face to evaluate the results, you need to install matlab and the Wider Face toolkit first.

 - Valid: 
`./darknet detector valid cfg/widerface.data cfg/face_small_context3.cfg ./backup/face_small_context3_final.weights` 
After validation, we will get a resulting .txt file under '/results': 
	comp4_det_test_aeroplane.txt
- Transfer the .txt file to WIDER FACE validation style
I have write the file to transfer, just run it:
`python valid_transfer.py`
This will produce the results needed by Wider Face (the result format could refer to 'widerface_result') and then
- Put the results under the dir of Wider Face validation tool.
- Do some changes and run in matlab and we will get the precison-recall curves on 'easy', 'medium' and 'hard' respectively.

## 5. And this is the qualitative result.
I write the paint.py to draw bounding boxes, red is the original annotations and green is the predicted bounding box.
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/00.png"/>
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/01.png"/>
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/02.png"/>
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/00.png"/>
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/01.png">
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/02.png">
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/000.png">
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/001.png">
<img width="400" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/002.png">


