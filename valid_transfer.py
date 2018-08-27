import numpy
import matplotlib.pyplot as plt
import shutil
import os
from PIL import Image


#####create the valid images list

annotations = open('./wider_face_split/wider_face_val_bbx_gt.txt')
lines = annotations.readlines()
numOfLines = len(lines)

if not os.path.exists('valImgList.txt'):
	imgList = open('valImgList.txt', 'w')
	i = 0
	j = 0

	while i<numOfLines:
		numOfFace=lines[i+1]
		imgName=str(lines[i].rstrip('\n'))
		imgList.write(imgName)
		imgList.write('\n')
		i=i+int(numOfFace)+2
#####

#read the validation images
f1=open('./valImgList.txt')
lines_1=f1.readlines()

#read the obtained detection results
f2=open('./results/comp4_det_test_aeroplane.txt')
lines_2=f2.readlines()

i=0
j=0


#generate resulting labels for each image, the format is /widerface_results/sub_directory/labels
while i < len(lines_2):
	name=lines_1[j].strip()
	name=name.split('/')
	path='./widerface_result'
	if not os.path.exists(path):
		os.mkdir(path)
	path=os.path.join(path,name[0])
	if not os.path.exists(path):
		os.mkdir(path)#sub_directory		
	#print('path:',path)
	#print('name:',name[1])
	#name=lines_1[j].strip()
	#name=name.split('.')
	#name=name[0]
	#name=name+'.txt'
	#print(name)
	#f2.write(name+'\n')
	num_face = lines_2[i+1]
	filepath=path+'/'+name[1]
	print('filepath:',filepath)
	f3=open(filepath,'a')
	f3.write(str(lines_2[i]))
	f3.write(num_face)
	#name = lines_1[j]
	#img_name = lines[i].split('/')
	#img_name = img_name[1][:-5]
	#print(lines[i].rstrip('\n'))
	#print(num_face.rstrip('\n'))
	#strr=str(lines[i].rstrip('\n'))
	#toFile.write(strr)
	#toFile.write('\n')
	#s_s=imgSize_lines[j].split()
	#imgH=float(s_s[1])
	#imgW=float(s_s[0])
	#print('imgH',imgH)
	#print('imgW',imgW)
	#print('imgName', img_name[1][:-5])
	for numface in range(int(num_face)):
		#transfer the detection results to wider face style
		s=lines_2[i+2+numface].strip('\n')
		s=lines_2[i+2+numface].split()
		score=s[0]
		xmin=s[1]
		ymin=s[2]
		xmax=s[3]
		ymax=s[4]
		left_x=float(xmin)
		top_y=float(ymin)
		w=float(xmax)-float(xmin)
		h=float(ymax)-float(ymin)
		#write to the .txt file
		f3.write(str(left_x) + ' ')
		f3.write(str(top_y) + ' ')
		f3.write(str(w) + ' ')
		f3.write(str(h) + ' ')
		f3.write(str(score) + '\n')
	i=i+int(num_face)+2
	j=j+1
	

	
