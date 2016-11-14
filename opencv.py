#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def readImage():
    img = cv2.imread('logo_cbfea26.png',cv2.IMREAD_COLOR)
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('messigray.png',img)
        cv2.destroyAllWindows()

def readImageWithPlt():
    img = cv2.imread('opencv_screenshot.jpg',0)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
    
def readVideo():
    cap = cv2.VideoCapture('all_world.avi')
    if cap.isOpened() == False:
        cap.open('all_world.avi')
    print cap.isOpened()
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        print ret
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
def drawPic():    
    img = np.zeros((512,512,3), np.uint8)
    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

def cv2Canny():        
    img = cv2.imread("code_lu.gif", 0)  

    img = cv2.GaussianBlur(img,(3,3),0)  
    canny = cv2.Canny(img, 50, 150)  
      
    cv2.imshow('Canny', canny)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

def cv2Resize():
    image=cv2.imread('code_lu.gif')
    res=cv2.resize(image,(480,200),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('iker',res)
    #cv2.imshow('image',image)
    
    img = cv2.GaussianBlur(res,(3,3),0)  
    canny = cv2.Canny(img, 50, 150)  
    cv2.imshow('Canny', canny)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
cv2Resize()