

#  Face detection based on Darknet and Wider Face dataset
This project aims to realise face detection based on darknet and Wider Face dataset,incluing:
	

- Face detection by using official yolov2, yolov3, yolov2-tiny and etc.
- Face detection by using my own network writed on darknet.
- The networks are trained on Wider Face training set
- The networks are evaluated on Wider Face validation set
## 1. Clone the project
First, clone this project using git:
		`git clone https://github.com/zlmo/Face-Detection.git`

## 2. Dataset preparation
Then, we need to prepare the training set first. This includes downloading the dataset and transfer it to darknet style.
### a. Download WIDER FACE
The official website of WIDER FACE is 									http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/. 
**WIDER_train.zip, WIDER_val.zip and wider_face_split.zip** are needed at least.


### b. Extract the downloaded dataset
Extract **WIDER_train.zip**, **WIDER_val.zip** and **wider_face_split.zip** to '/darknet'

	unzip WIDER_train.zip -d ./darknet 
	unzip WIDER_val.zip -d ./darknet 
	unzip wider_face_split.zip -d ./darknet

### c. Transfer the training data and annotations to PASCAL VOC style
When we use Wider Face to train our networks, we need to transfer the dataset to darknet style. The official darknet project use Pascal VOC style, so we transfer Wider Face to Pascal VOC style.
I have write the python file to transfer, just run it!

`python widerface_label.py`

This file will do the following things:
 - **Make the directories:** /WIDER_FACE_VOC/VOC2007/VOCdevkit/JPEGImages
/ WIDER_FACE_VOC/VOC2007/VOCdevkit/Labels
 - **Copy the images from each branch of WIDER_train and integrate them together in /JPEGImages** .
 - **Generate training labels.** 
The original format of the annotations
of Wider Face is:
... 
              < image name i >  
              < number of faces in this image = im > 
              < face i1 > 
              < face i2 > 
              ... 
              < face im > 
              ... 
and Darknet wants a .txt file for each image with a line for each ground truth object in the image that looks like:
              <object-class> <x> <y> <width> <height>
Where x, y, width, and height are relative to the image's width and height. 
 - **Modify some valid images.**
 There are some valid images in Wider Face training set whose annotations has values less than 0. The annotation value of x, y, width and height must more than 0, a value less than zero will lead to 'segmentation fault'. So we need to check all the annotations to make sure each value is more than 0, when a value is checked to less than 0, it will be forced to set to 0.001.
 - **Generate the training list:** train.txt.
  
## 2. Train with  yolov2, yolov3, yolov2-tiny-voc and etc.
Once the dataset has been prepared okay, we can start to train the network for face detection. 
When use the official yolo-like networks to achieve face detection, you need to do some modifications:
  
 - Set class numbers to 1.
  - Set filter numbters on the last conv layer to 30 for yolov2 and 128 for yolov3, which is the layer on top of 'Region layer'.
  After the above modifications, you can start to train:
  
`./darknet detector train cfg/widerface.data cfg/yolov2-tiny-voc.cfg darknet.conv.13`     

  This is trained use yolov2-tiny-voc.cfg, and the pre-trained weights  darknet.con.13 can be found here in BaiduYun:
    链接: https://pan.baidu.com/s/1TAq925irdympMnwPNPP4kw 密码: vew1
  
  
## 3. Train with my own face detection method
  I write a network based on darknet which is the face_small_context3.cfg. This network is a fast lightweight face detection network with feature fusion and context.
  

    ./darknet detector train cfg/widerface.cfg cfg/face_small_context3.cfg darknet.conv.13

  

## 4. Evaluated on Wider Face validation set
We use toolkit from official website of Wider Face to evaluate the results, you need to install matlab first.

 - Valid: 
`./darknet detector valid cfg/widerface.data cfg/face_small_context3.cfg ./backup/face_small_context3_final.weights` 
After validation, we will get a result file under '/results': 
comp4_det_test_aeroplane.txt
- Transfer the .txt file to WIDER FACE validation style
I have write the file to transfer, just run it:
`python valid_transfer.py`
- Put the generated files under the dir of Wider Face validation tool.
- Run in matlab and we will get the precison-recall curves on 'easy', 'medium' and 'hard' respectively.

## 5. And this is the qulitative result.
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/01.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/02.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/blur/03.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/01.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/02.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/expression/03.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/001.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/002.png"/>
<img width="300" height="300" src="https://raw.github.com/zlmo/face_detection/master/detections/small-faces/003.png"/>

