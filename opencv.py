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

def cv2CannyFace():
    image=cv2.imread('face.jpg')
    #res=cv2.resize(image,(480,200),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('iker',image)
    #cv2.imshow('image',image)
    
    img = cv2.GaussianBlur(image,(5,5),0)
    '''边缘化处理'''
    canny = cv2.Canny(img, 50, 150)  
    cv2.imshow('Canny', canny)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
'''添加干扰点，椒盐处理'''    
def salt(img, n):    
    for k in range(n):    
        i = int(np.random.random() * img.shape[1]);    
        j = int(np.random.random() * img.shape[0]);    
        if img.ndim == 2:     
            img[j,i] = 255    
        elif img.ndim == 3:     
            img[j,i,0]= 255    
            img[j,i,1]= 255    
            img[j,i,2]= 255    
    return img
    
def cv2Blur():
    image=cv2.imread('pic/face3.jpg')
    cv2.imshow('image',image)
    
    #img1 = cv2.GaussianBlur(image,(5,5),0)
    #cv2.imshow('GaussianBlur', img1)
    
    #result = salt(image,500)
    #cv2.imshow('salt',result)

    #img2 = cv2.medianBlur(result,5)
    #img2 = cv2.bilateralFilter(image,9,75,75)
    img2 = cv2.bilateralFilter(image,9, 60,2.5)
    cv2.imshow('bilateralFilter', img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#腐蚀操作
def cv2Erode():
    img = cv2.imread('pic/code_lu.gif')  
    cv2.imshow('image',img)
    #OpenCV定义的结构元素  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))  
      
    #腐蚀图像  
    eroded = cv2.erode(img,kernel)  
    #显示腐蚀后的图像  
    cv2.imshow("Eroded Image",eroded);  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
def cv2ErodeCanny():    
    image = cv2.imread("pic/code_lu4.gif",0) 
    image3 = cv2.imread("pic/code_lu4.gif",1) 
    cv2.imshow("origin",image)
    print image.shape
    '''
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))  
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)  
    #显示腐蚀后的图像  
    cv2.imshow("Close",closed);
    #开运算  
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)  
    #显示腐蚀后的图像  
    cv2.imshow("Open", opened);  
    retval, result = cv2.threshold(opened, 180, 255, cv2.THRESH_BINARY);   
    '''
    #构造一个5x5,or 7×7的结构元素   
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))  
    dilate = cv2.dilate(image, element) 
    cv2.imshow("first dilate",dilate)  

    erode = cv2.erode(dilate, element)  
    cv2.imshow("next erode",erode) 
    retval, result = cv2.threshold(erode, 180, 255, cv2.THRESH_BINARY);   
    #反色，即对二值图每个像素取反  
    #result = cv2.bitwise_not(result);   
    #显示图像  
    cv2.imshow("result",result); 
    
    '''边缘化处理'''
    '''
    canny = cv2.Canny(result, 50, 150)  
    cv2.imshow('Canny', canny)
    '''
    '''提取轮廓'''
    image2, contours, hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    #contours = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    #print contours
    #print (type(contours))  
    #print (type(contours[0]))  
    #print (len(contours[0]))
    #print contours[0].tolist()
    #print contours[0].ndim
    #print contours[0].shape
    #y=contours[0].reshape(len(contours[0]),2)
    #print y
    #print y[2,1]
    count = 0;
    for contour in contours:
        y = contour.reshape(len(contour),2)
        with open('contours'+str(count)+'.dat', 'wb') as f:
            for i in range(0,len(contour)):
                if i%2 == 0:
                    f.write(str(y[i,0])+','+str(110-y[i,1])+'\n')
        count = count + 1
        
    img = cv2.drawContours(image3, contours, -1, (0,255,0), 3)
    #cv2.drawContours(image,contours,1,(0,255,0),3)
    #cv2.drawContours(image,contours,2,(255,0,0),3)
    cv2.imshow("img", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def colorKMean():
    image = cv2.imread("pic/code_lu1.gif",1)
    cv2.imshow("origin",image)
    
    image_lab = cv2.cvtColor(image,cv2.COLOR_RGB2LAB)
    cv2.imshow("lab1",image_lab)
    print image_lab
    
    image_lab2 = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    cv2.imshow("lab2",image_lab2)
    print image_lab2
    
    image_lab3 = cv2.cvtColor(image,cv2.COLOR_BGR2Lab)
    cv2.imshow("lab3",image_lab3)
    
    image_lab4 = cv2.cvtColor(image,cv2.COLOR_RGB2Lab)
    cv2.imshow("lab4",image_lab4)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
colorKMean()