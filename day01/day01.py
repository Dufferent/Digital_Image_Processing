#!/usr/bin/python3.5
# coding=utf-8

# from numpy.__config__ import show
import cv2 as cv
import matplotlib as plt
from matplotlib.pyplot import imshow
import numpy as np
import os

def gray_deal(img):
    for axis_y in range(0,600):
        for axis_x in range(0,600):
            gray = (int(img[axis_y,axis_x][0])+int(img[axis_y,axis_x][1])+int(img[axis_y,axis_x][2]))/3
            img[axis_y,axis_x][0] = gray
            img[axis_y,axis_x][1] = gray
            img[axis_y,axis_x][2] = gray

if __name__ == "__main__":
    animal = cv.imread("./animal.jpg")
    animal = cv.resize(animal,(600,600),interpolation=cv.INTER_AREA)
    flower = cv.imread("./flower.jpg")
    flower = cv.resize(flower,(600,600),interpolation=cv.INTER_AREA)

    cv.cvtColor(animal,cv.COLOR_RGB2BGR,animal)
    cv.cvtColor(flower,cv.COLOR_RGB2BGR,flower)
    # gray_deal(flower)
    img = []
    for axis_y in range(0,600):
        line = []
        for axis_x in range(0,600):
            rgb = []
            for c in range(0,3):
                rgb.append(0)
            line.append(rgb)
        img.append(line)
    img = np.array(img,dtype=np.uint8)
    cv.circle(img,(240,300),170,(255,255,255),cv.FILLED)

    capture = img/255
    process = animal * capture
    flower_process = flower * (1-capture)

    # process = np.array(process,dtype=np.float32)
    # flower_process = np.array(flower_process,dtype=np.float32)
    final_process = flower_process + process*0.7
    # combine = np.hstack([animal,flower,process,flower_process,final_process])
    combine = final_process
    # cv.imshow("process_img",combine)
    imshow(combine.astype(np.uint8))
    plt.pyplot.show()
    # cv.imshow("combine",combine)
    cv.imwrite("./bg.jpg",img)
    
    cv.cvtColor(final_process.astype(np.uint8),cv.COLOR_BGR2RGB,final_process)
    cv.imwrite("final.jpg",final_process)
    cv.waitKey(0)