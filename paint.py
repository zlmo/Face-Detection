import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os

#362 0 0.40926498666666666 0.20952082444444442 0.3654380933333333 0.3600137911111111
#367 0 0.5622772861356932 0.37181002222222226 0.5612313805309734 0.6444444444444445
#398 0 0.4852866722408027 0.4893605412026726 0.6866706755852843 0.6892247661469934  
#362 450,300
#367 450,339
#398 449,299
img = Image.open('./illumination_1/61_Street_Battle_streetfight_61_767.jpg')
draw = ImageDraw.Draw(img)

f = open('./annotations/illumination_1/61_Street_Battle_streetfight_61_767.txt')
lines=f.readlines()

f_predict = open('./predict/illumination_1/61_Street_Battle_streetfight_61_767.txt')
lines_predict=f_predict.readlines()

for line in lines:
    line = line.strip()
    line = line.split()
    #print(line[1])

    
    H=577
    W=1024
    x=float(line[1])*W
    y=float(line[2])*H
    w=float(line[3])*W
    h=float(line[4])*H
    dMinX=x
    dMinY=y
    dMaxX=x+w
    dMaxY=y+h
    draw.line([dMinX,dMinY,dMinX,dMaxY],width=4,fill='red')
    draw.line([dMinX,dMinY,dMaxX,dMinY],width=4,fill='red')
    draw.line([dMinX,dMaxY,dMaxX,dMaxY],width=4,fill='red')
    draw.line([dMaxX,dMinY,dMaxX,dMaxY],width=4,fill='red')
    
for line in lines_predict:
    line = line.strip()
    line = line.split()
    print(len(line))
    
    if (len(line) > 1) and (float(line[4]) > 0.8):
        x_pred=float(line[0])
        y_pred=float(line[1])
        w_pred=float(line[2])
        h_pred=float(line[3])
        dMinX_pred=x_pred
        dMinY_pred=y_pred
        dMaxX_pred=x_pred+w_pred
        dMaxY_pred=y_pred+h_pred
        draw.line([dMinX_pred,dMinY_pred,dMinX_pred,dMaxY_pred],width=4,fill='green')
        draw.line([dMinX_pred,dMinY_pred,dMaxX_pred,dMinY_pred],width=4,fill='green')
        draw.line([dMinX_pred,dMaxY_pred,dMaxX_pred,dMaxY_pred],width=4,fill='green')
        draw.line([dMaxX_pred,dMinY_pred,dMaxX_pred,dMaxY_pred],width=4,fill='green')
    
    
plt.imshow(img)
plt.show()   
img.save('./004.png') 
"""
cx=0.4963*W
cy=0.4221*H
cw=0.6479*W
ch=0.7060*H

#lx=597
#ly=3
#rx=935
#ry=341
#dMinX=28.4538-37.1
dMinX=3
dMinY=37.6646-29
dMaxX=28.4538+37.1
dMaxY=37.6646+29

draw = ImageDraw.Draw(img)
"""

"""
draw.line([cx-0.5*cw,cy-0.5*ch,cx+0.5*cw,cy-0.5*ch],width=5,fill='green')
draw.line([cx-0.5*cw,cy-0.5*ch,cx-0.5*cw,cy+0.5*ch],width=5,fill='green')
draw.line([cx-0.5*cw,cy+0.5*ch,cx+0.5*cw,cy+0.5*ch],width=5,fill='green')
draw.line([cx+0.5*cw,cy-0.5*ch,cx+0.5*cw,cy+0.5*ch],width=5,fill='green')


draw.line([dMinX,dMinY,dMinX,dMaxY],width=5,fill='red')
draw.line([dMinX,dMinY,dMaxX,dMinY],width=5,fill='red')
draw.line([dMinX,dMaxY,dMaxX,dMaxY],width=5,fill='red')
draw.line([dMaxX,dMinY,dMaxX,dMaxY],width=5,fill='red')


for i in range(5):
    draw.ellipse([cx-0.5*cw,cy-0.5*ch,cx+0.5*cw,cy+0.5*ch],outline='green')


draw.line([lx,ly,lx,ry],width=5,fill='green')
draw.line([lx,ly,rx,ly],width=5,fill='green')
draw.line([rx,ly,rx,ry],width=5,fill='green')
draw.line([rx,ry,lx,ry],width=5,fill='green')

plt.imshow(img)
plt.show()
#img.save('00.jpg')
"""