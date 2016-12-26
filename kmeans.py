#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

def drawOneFeature():
    x = np.random.randint(25,100,25)
    y = np.random.randint(175,255,25)
    z = np.hstack((x,y))
    z = z.reshape((50,1))
    z = np.float32(z)
    plt.hist(z,256,[0,256]),plt.show()

    # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # Set flags (Just to avoid line break in the code)
    flags = cv2.KMEANS_RANDOM_CENTERS

    # Apply KMeans
    compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)

    A = z[labels==0]
    B = z[labels==1]

    # Now plot 'A' in red, 'B' in blue, 'centers' in yellow
    plt.hist(A,256,[0,256],color = 'r')
    plt.hist(B,256,[0,256],color = 'b')
    plt.hist(centers,32,[0,256],color = 'y')
    plt.show()

def colorQuantization():
    img = cv2.imread('pic/code_lu2.gif')
    cv2.imshow("origin",img)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    #cv2.imshow("image_lab2",image_lab2)
    
    Z = img.reshape((-1,3))
    
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 6
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    
    length = img.shape[0]*img.shape[1]
    for i in range(K):
        #print center[i]
        h,s,v = rgb2hsv(center[i][2],center[i][1],center[i][0])

        if v >= 0.54 and v < 0.6:
            print 'index = '+str(i) + ' h: '+str(h) + " s: "+str(s) + " v: "+str(v)
            '''
            Y = center[i][2]*0.299 + center[i][1]*0.587 +  center[i][0]*0.114
            print 'Y: '+str(Y)
            I = center[i][2]*0.596 - center[i][1]*0.275 -  center[i][0]*0.321
            print 'I: '+str(I)
            Q = center[i][2]*0.212 - center[i][1]*0.523 +  center[i][0]*0.311
            print 'Q: '+str(Q)
            '''
            x = np.zeros((length,3),dtype=np.uint8)
            x[:,:] = 255
            x[np.where(label==i)[0],:] = center[i]
            res = x.reshape((img.shape))
            cv2.imshow('res'+str(i),res)
            cv2.imwrite("pic/code_lu_cut"+str(i)+".jpg",res)
    # Now convert back into uint8, and make original image
    res = center[label.flatten()]
    resKmeans = res.reshape((img.shape))

    cv2.imshow('resKmeans',resKmeans)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

colorQuantization()