#!/usr/bin/python3.5
# coding=utf-8

from numpy.core.fromnumeric import sort
import cv2 as cv
import matplotlib as plt
from matplotlib.pyplot import imshow
import numpy as np
import os
import math

def avr_filter(src,k_sz):
    h,w,c = src.shape
    ret = []
    for axis_y in range(0,int(h)):
        line = []
        for axis_x in range(0,int(w)):
            tmps = []
            for ch in range(0,3):
                tmps.append(0)
            line.append(tmps)
        ret.append(line)
    ret = np.array(ret,dtype=np.float32)

    for axis_y in range(0,h-k_sz):
        for axis_x in range(0,w-k_sz):
            tmps_scalar = [0,0,0]
            for dy in range(0,k_sz):
                for dx in range(0,k_sz):
                    tmps_scalar[0] += src[axis_y+dy,axis_x+dx][0]
                    tmps_scalar[1] += src[axis_y+dy,axis_x+dx][1]
                    tmps_scalar[2] += src[axis_y+dy,axis_x+dx][2]
            tmps_scalar = np.array(tmps_scalar,dtype=np.float32)
            tmps_scalar /= k_sz*k_sz
            # print (tmps_scalar)
            ret[axis_y,axis_x] = tmps_scalar
    return ret

def midl_filter(src,k_sz):
    h,w,c = src.shape
    ret = []
    for axis_y in range(0,int(h)):
        line = []
        for axis_x in range(0,int(w)):
            tmps = []
            for ch in range(0,3):
                tmps.append(0)
            line.append(tmps)
        ret.append(line)
    ret = np.array(ret,dtype=np.float32)

    for axis_y in range(0,h-k_sz):
        for axis_x in range(0,w-k_sz):
            b_list = []
            g_list = []
            r_list = []
            for dy in range(0,k_sz):
                for dx in range(0,k_sz):
                    b_list.append(src[axis_y+dy,axis_x+dx][0])
                    g_list.append(src[axis_y+dy,axis_x+dx][1])
                    r_list.append(src[axis_y+dy,axis_x+dx][2])
            sort(b_list)
            sort(g_list)
            sort(r_list)
            # print (b_list)
            cur_scalar = [ b_list[k_sz*k_sz/2+1], g_list[k_sz*k_sz/2+1], r_list[k_sz*k_sz/2+1] ]
            # print (tmps_scalar)
            cur_scalar = np.array(cur_scalar,dtype=np.float32)
            ret[axis_y,axis_x] = cur_scalar
    return ret

if __name__ == "__main__":
    A = cv.imread("./animal.jpg")
    A = cv.resize(A,(600,600),interpolation=cv.INTER_AREA)
    A = np.array(A,dtype=np.float32)
    B = avr_filter(A,3)
    C = midl_filter(A,3)

    D = cv.cvtColor(B,cv.COLOR_RGB2BGR)
    E = cv.cvtColor(C,cv.COLOR_RGB2BGR)
    F = np.hstack([D,E])
    imshow(F.astype(np.uint8))
    plt.pyplot.show()
