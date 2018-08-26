# 1. Data preparation
Prepare training data. As we use WIDER FACE for training, we need to download the dataset first.
## a. Download WIDER FACE dataset from official website
Official website of WIDER FACE:http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/.
Wider Face Training Images, Wider Face Validation Images, Face annotations are needed at least.


## b. Extract the downloaded dataset
Extract the WIDER_train and wider_face_split under /darknet

## c. Transfer the training data and annotations to PASCAL VOC style
I have write the python file to transfer, just run it!

python widerface_label.py

This file will create the directories, copy the images and generate labels. The original format of the annotations
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
  
# 2. Train with official yolov2 or yolov3
When use the official yolo to realise face detection, you need to do some modifications:
  a.Change class number
  b.Change filter numbters on the last conv layer, which is the layer on top of 'Region layer'
  After the above modifications, you can start to train:
  
  ./darknet detector train cfg/widerface.data cfg/yolov2-tiny-voc.cfg darknet.conv.13
  
  The pre-trained weights file darknet.con.13 can be found here in BaiduYun:
    链接: https://pan.baidu.com/s/1TAq925irdympMnwPNPP4kw 密码: vew1
  
  
# 3. Train with my face detection method
  face_small_context3.cfg is my face detection network, which is a fast lightweight face detection network with feature fusion and context.
  Or you can just use the official yolov2 and yolov3 with some modifications. 

# 4. Evaluated on Wider Face validation set
We use toolkit from official website of Wider Face to evaluate the results, you need to install matlab first.
a.Valid: ./darknet detector valid cfg/widerface.data cfg/face_small_context3.cfg ./backup/face_small_context3_final.weights
After the command, we will get a result file under '/results': comp4_det_test_aeroplane.txt
b. Transfer the txt file to WIDER FACE validation style
I have write the file to transfer, just run it:
  python valid_transfer.py
c. Put the generated files under the dir of Wider Face validation tool.
d. Run in matlab and we will get the precison-recall curves on 'easy', 'medium' and 'hard' respectively.

# 5. And this is the qulitative result.

  Detections
<img width="150" height="150" src="https://raw.github.com/zlmo/face_detection/master/data/001.png"/>
![Image text](https://raw.github.com/zlmo/face_detection/master/data/001.png)
