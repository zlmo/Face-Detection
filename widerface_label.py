import numpy as np
import matplotlib.pyplot as plt
import shutil
import os
from PIL import Image
import skimage.io as io

#make VOC-like directory

path1 = './WIDER_FACE_VOC'
path2 = './WIDER_FACE_VOC/VOCdevkit'
path3 = './WIDER_FACE_VOC/VOCdevkit/VOC2007'
imgPath = './WIDER_FACE_VOC/VOCdevkit/VOC2007/JPEGImages'
labelPath = './WIDER_FACE_VOC/VOCdevkit/VOC2007/labels'

if not os.path.exists(path1):
	os.mkdir(path1)
if not os.path.exists(path2):
	os.mkdir(path2)
if not os.path.exists(path3):
	os.mkdir(path3)
if not os.path.exists(imgPath):
	os.mkdir(imgPath)
if not os.path.exists(labelPath):
	os.mkdir(labelPath)

#create the image list

annotations = open('./wider_face_split/wider_face_train_bbx_gt.txt')
lines = annotations.readlines()
numOfLines = len(lines)

if not os.path.exists('imgList.txt'):
	imgList = open('imgList.txt', 'w')
	i = 0
	j = 0

	while i<numOfLines:
		numOfFace=lines[i+1]
		imgName=str(lines[i].rstrip('\n'))
		imgList.write(imgName)
		imgList.write('\n')
		i=i+int(numOfFace)+2

#copy images in WIDER_train dataset to dir 'JPEGImages'

imgList = open('imgList.txt', 'r')
linesOfImg=imgList.readlines()
info='./WIDER_train/images/'
"""
for line in linesOfImg:
	line=line.strip('\n')
	filepath=info+line
	shutil.copy(filepath,imgPath)
"""
# generate labels

# 1.obtain the width and height of all train images
if not os.path.exists('imgSize.txt'):
	#imgSize = open('imgSize.txt', 'w')
	i=0
	while i < len(linesOfImg):
		f=open('imgSize.txt','a')
		img_name=str(linesOfImg[i].rstrip('\n'))
		img_path=info+img_name
		print(img_path)
		nImg=np.array(Image.open(img_path))
		print('imgShape')
		print(nImg.shape)
		f.write(str(nImg.shape[1])+' ')#width
		f.write(str(nImg.shape[0])+'\n')#height
		i = i+1
# 2.generate the VOC-like labels

i=0
j=0
imgSize = open('./imgSize.txt')
imgSize_lines=imgSize.readlines()
while i < numOfLines:
	num_face=lines[i+1]
	img_name = lines[i].split('/')
	img_name = img_name[1][:-5]
	s_s=imgSize_lines[j].split()
	imgH=float(s_s[1])
	imgW=float(s_s[0])
	
	for numface in range(int(num_face)):
		f=open(labelPath+'/'+str(img_name)+'.txt','a')
		s=lines[i+2+numface].split()
		#print(s)
		#print(s[0])
		x=float(s[0])
		y=float(s[1])
		w=float(s[2])
		h=float(s[3])
		#检测坐标有错误的训练图片，如果某个坐标值小于或等于0，则将坐标值置为0.001
		if x <= 0.0:
			x = 0.001
		if y <= 0.0:
			y = 0.001
		if w <= 0.0:
			w = 0.001
		if h <= 0.0:
			h = 0.001
		#print(cx, cy, cw, ch)
		cx=x+0.5*w
		cy=y+0.5*h
		vocX=cx/imgW
		vocY=cy/imgH
		vocW=w/imgW
		vocH=h/imgH
		
		if vocX <= 0.0:
			print('x'+str(img_name))
		if vocY <= 0.0:
			print('y'+str(img_name))
		if vocW <= 0.0:
			print('w'+str(img_name))
		if vocH <= 0.0:
			print('h'+str(img_name))
		
		f.write('0'+' ')
		f.write(str(vocX)+' ')
		f.write(str(vocY)+' ')
		f.write(str(vocW)+' ')
		f.write(str(vocH)+' ')			
		f.write('\n')
	i=i+int(num_face)+2
	j=j+1

#generate train list
if not os.path.exists('./WIDER_FACE_VOC/train.txt'):
	trainFile=open('./WIDER_FACE_VOC/train.txt','a')
	for line in linesOfImg:
		#st=line.split()
		st = line.split('/')
		st = st[1]
		new_st = []
		new_st.append(st)
		#st=st.strip('\n')
		#st=''.join(st)
		new_st.insert(0,'/home/zlmo/darknet/WIDER_FACE_VOC/VOCdevkit/VOC2007/JPEGImages/')
		#print(new_st)
		#st.append('.jpg')
		s=''.join(new_st)
		print(s)
		s=str(s)
		#f1.write(s+'\n')
		trainFile.write(s)

