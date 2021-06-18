#!/usr/bin/python3.5
# coding=utf-8

import cv2 as cv
import matplotlib as plt
from matplotlib.pyplot import imshow
import numpy as np
import os
import math

'''
src
    [121,421]
    [235,435]
    [88,276]
    [288,330]

dst
    [121,421]
    [290,421]
    [121,276]
    [290,276]
'''

if __name__ == "__main__":
    A = cv.imread("./animal.jpg")
    A = cv.resize(A,(600,600),interpolation=cv.INTER_AREA)
    A = np.array(A,dtype=np.float32)
    # imshow(A.astype(np.uint8))
    # plt.pyplot.show()
    src = np.array(
        [ 
          [121,421],
          [235,435],
          [88,276],
          [288,330],
        ],dtype=np.float32
    )

    dst = np.array(
        [ 
          [121,421],
          [290,421],
          [121,276],
          [290,276],
        ],dtype=np.float32
    )

    rect = cv.getPerspectiveTransform(src,dst)
    print (rect)
    C = cv.warpPerspective(A,rect,(600,600))
    imshow(C.astype(np.uint8))
    plt.pyplot.show()