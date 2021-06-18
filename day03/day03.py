#!/usr/bin/python3.5
# coding=utf-8

import cv2 as cv
import matplotlib as plt
from matplotlib.pyplot import imshow
import numpy as np
import os
import math

if __name__ == "__main__":
    A = cv.imread("./animal.jpg")
    A = cv.resize(A,(600,600),interpolation=cv.INTER_AREA)
    A = np.array(A,dtype=np.float32)
    # imshow(A)
    # plt.pyplot.show()
    B = np.array([
        [1,0.2,0],
        [0,1,0]
        ],
        dtype=np.float32
    )
    C = []
    for axis_y in range(0,600):
        line = []
        for axis_x in range(0,600):
            rgb = []
            for c in range(0,3):
                rgb.append(0)
            line.append(rgb)
        C.append(line)
    C = np.array(C,dtype=np.float32)
    for axis_y in range(0,600):
        for axis_x in range(0,600):
            tmps = np.array([axis_x,axis_y,1],dtype=np.float32)
            dpos = B.dot(tmps)
            # print (dpos)
            dx = dpos[0]
            dy = dpos[1]
            if dx < 600 and dy <600:
                C[dy,dx] = A[axis_y,axis_x]
    imshow(C.astype(np.uint8))
    plt.pyplot.show()
