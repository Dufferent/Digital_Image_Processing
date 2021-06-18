#!/usr/bin/python3.5
# coding=utf-8

import cv2 as cv
import matplotlib as plt
from matplotlib.pyplot import imshow
import numpy as np
import os
import math

def panding(src,dx,dy):
    h,w,c = src.shape
    rate_x = dx/w
    rate_y = dy/h

    print (h,w,c)
    print (rate_x,rate_y)

    img = []
    for axis_y in range(0,int(dy)):
        line = []
        for axis_x in range(0,int(dx)):
            tmps = []
            for ch in range(0,3):
                tmps.append(0)
            line.append(tmps)
        img.append(line)
    img = np.array(img,dtype=np.float32)
    for axis_y in range(0,int(dy)):
        for axis_x in range(0,int(dx)):
            img[axis_y][axis_x] = src[axis_y/rate_y][axis_x/rate_x]

    return img

def panding_linear(src,dx,dy):
    h,w,c = src.shape
    rate_x = dx/w
    rate_y = dy/h

    print (h,w,c)
    print (rate_x,rate_y)

    img = []
    for axis_y in range(0,int(dy)):
        line = []
        for axis_x in range(0,int(dx)):
            tmps = []
            for ch in range(0,3):
                tmps.append(0)
            line.append(tmps)
        img.append(line)
    img = np.array(img,dtype=np.float32)
    for axis_y in range(1,int(dy)):
        for axis_x in range(1,int(dx)):
            # img[axis_y][axis_x] = src[axis_y/rate_y][axis_x/rate_x]
            n1 = [int(axis_x/rate_x),int(axis_y/rate_y)]
            n2 = [int(axis_x/rate_x)+1,int(axis_y/rate_y)]
            n3 = [int(axis_x/rate_x),int(axis_y/rate_y)+1]
            n4 = [int(axis_x/rate_x)+1,int(axis_y/rate_y)+1]
            n1[0] = min(w-1,n1[0])
            n1[1] = min(h-1,n1[1])
            n2[0] = min(w-1,n2[0])
            n2[1] = min(h-1,n2[1])
            n3[0] = min(w-1,n3[0])
            n3[1] = min(h-1,n3[1])
            n4[0] = min(w-1,n4[0])
            n4[1] = min(h-1,n4[1])

            rate_w_x = (axis_x/rate_x - axis_x//rate_x)
            rate_w_y = (axis_y/rate_y - axis_y//rate_y)
            color = [ src[ n1[1],n1[0] ][0]*rate_w_x*rate_w_y + src[ n2[1],n2[0] ][0]*(1-rate_w_x)*rate_w_y + src[ n3[1],n3[0] ][0]*rate_w_x*(1-rate_w_y) + src[ n4[1],n4[0] ][0]*(1-rate_w_x)*(1-rate_w_y), \
                      src[ n1[1],n1[0] ][1]*rate_w_x*rate_w_y + src[ n2[1],n2[0] ][1]*(1-rate_w_x)*rate_w_y + src[ n3[1],n3[0] ][1]*rate_w_x*(1-rate_w_y) + src[ n4[1],n4[0] ][1]*(1-rate_w_x)*(1-rate_w_y), \
                      src[ n1[1],n1[0] ][2]*rate_w_x*rate_w_y + src[ n2[1],n2[0] ][2]*(1-rate_w_x)*rate_w_y + src[ n3[1],n3[0] ][2]*rate_w_x*(1-rate_w_y) + src[ n4[1],n4[0] ][2]*(1-rate_w_x)*(1-rate_w_y), \
            ]
            img[axis_y][axis_x][0] = color[0]
            img[axis_y][axis_x][1] = color[1]
            img[axis_y][axis_x][2] = color[2]

    return img


if __name__ == "__main__":
    A = cv.imread("./animal.jpg")
    A = cv.resize(A,(600,600),interpolation=cv.INTER_AREA)
    A = np.array(A,dtype=np.float32)
    B = panding(A,800.0,640.0)
    C = panding_linear(A,800.0,640.0)
    D = np.hstack([B,C])
    imshow(D.astype(np.uint8))
    plt.pyplot.show()
