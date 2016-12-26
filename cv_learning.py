#coding=utf-8  
import cv2
import numpy
import os
import os.path

def erode_dilate():  
    image = cv2.imread("pic/code_lu.gif",0);  
    #构造一个3×3的结构元素   
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))  
    dilate = cv2.dilate(image, element) 
    cv2.imshow("dilate",dilate);   
    erode = cv2.erode(image, element)  
    cv2.imshow("erode",erode);   
      
    #将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像  
    result = cv2.absdiff(dilate,erode);  
      
    #上面得到的结果是灰度图，将其二值化以便更清楚的观察结果  
    retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY);   
    #反色，即对二值图每个像素取反 
    result = cv2.bitwise_not(result);
    #显示图像
    cv2.imshow("result",result);
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def splitChan():    
    img = cv2.imread("pic/face2.jpg")  
    b, g, r = cv2.split(img)
    #print img.shape[0]
    #print img.shape[1]
    cv2.imshow("Blue", r)  
    cv2.imshow("Red", g)  
    cv2.imshow("Green", b)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

def sobel():    
    img = cv2.imread("pic/code_lu.gif", 0)  
      
    x = cv2.Sobel(img,cv2.CV_16S,1,0)  
    y = cv2.Sobel(img,cv2.CV_16S,0,1)  
      
    absX = cv2.convertScaleAbs(x)   # 转回uint8  
    absY = cv2.convertScaleAbs(y)  
      
    dst = cv2.addWeighted(absX,0.5,absY,0.5,0)  
      
    cv2.imshow("absX", absX)  
    cv2.imshow("absY", absY)  
      
    cv2.imshow("Result", dst)  
      
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

def cv2MorphologyEx():     
    img = cv2.imread('pic/code_lu6.gif',0) 
    cv2.imshow("origin",img);  
     
    #定义结构元素  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))  
      
    #闭运算  
    closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  
    #显示腐蚀后的图像  
    cv2.imshow("Close",closed);  
      
    #开运算  
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  
    #显示腐蚀后的图像  
    cv2.imshow("Open", opened);  
      
    cv2.waitKey(0)  
    cv2.destroyAllWindows()      
    
def cv2CutImage():    
    image = cv2.imread("pic/code_lu2.gif",0) 
    cv2.imshow("origin",image)
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

    width = result.shape[1]
    height = result.shape[0]
    pairsx = {}
    pairsy = {}
    count = 1
    maxWidth = 0;
    maxWidthIndex = 0;
    
    print width
    print height
    
    xstart = -1
    xend = -1
    ystart = -1
    yend = -1
    
    cutSize = {}
    
    for i in range(width):
        hasblack = False
        for j in range(height):
            color1 = result[j,i]
            if color1 == 0 and xstart == -1:#start
                xstart = i
            if  color1 == 0 and xstart != -1:
                hasblack = True
                break
        if hasblack == False and xstart != -1:#all color is white
            xend = i
            pairsx[str(xstart)] = xend

            cv2.imwrite("pic/code_lu_cut"+str(count)+".jpg",result[0:110,xstart:xend])
            cutSize[str(count)] = xend - xstart
            if xend - xstart > maxWidth:
                maxWidthIndex = count
                maxWidth = xend - xstart
            count = count + 1
            xstart = -1 #re initliaze
            xend = -1
    if xstart != -1 and xend == -1:
        #last x is black
        xend = width-1
        cv2.imwrite("pic/code_lu_cut"+str(count)+".jpg",result[0:110,xstart:xend])
        cutSize[str(count)] = xend - xstart
        if xend - xstart > maxWidth:
            maxWidthIndex = count       
            maxWidth = xend - xstart
        count = count + 1
        
    print pairsx
    print count
    print maxWidthIndex
    print maxWidth
    if count == 4:#3 pictures
        imageMaxWidth = cv2.imread("pic/code_lu_cut"+str(maxWidthIndex)+".jpg",0)
        cv2.imwrite("pic/code_lu_cut"+str(count)+".jpg",imageMaxWidth[0:110,0:maxWidth/2])
        count = count + 1
        cv2.imwrite("pic/code_lu_cut"+str(count)+".jpg",imageMaxWidth[0:110,maxWidth/2:maxWidth])
        count = count + 1
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows() 

def getColor():
    image = cv2.imread("pic/code_lu1.gif",cv2.IMREAD_COLOR) 
    cv2.imshow("origin",image)
    width = image.shape[1]
    height = image.shape[0]
    print str(width) + " " + str(height)
    colors = set([])
    count = 0
    for i in range(width):
        for j in range(height):
            count = count +1
            color1 = image[j,i][0]
            color2 = image[j,i][1]
            color3 = image[j,i][2]
            if str(color1)+str(color2)+str(color3) not in colors:
                colors.add(str(color1)+str(color2)+str(color3))
            #if image[j,i] not in colors:
            #    colors.put(image[j,i])
    print count
    print colors
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

def outputContour(origin_image,out_image_name):    
    image = cv2.imread(origin_image,0)
    #cv2.imshow("origin",image)

    #构造一个5x5,or 7×7的结构元素   
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))  
    dilate = cv2.dilate(image, element) 
    #cv2.imshow("first dilate",dilate)  
    
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 7))  
    erode = cv2.erode(dilate, element2)
    #cv2.imshow("next erode",erode)
    retval, result = cv2.threshold(erode, 180, 255, cv2.THRESH_BINARY);   
    #反色，即对二值图每个像素取反
    #result = cv2.bitwise_not(result);
    #显示图像
    cv2.imshow("threshold",result);
    #CHAIN_APPROX_NONE,CV_CHAIN_APPROX_SIMPLE,CV_CHAIN_APPROX_TC89_L1
    image2, contours, hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    count = 0;
    #remove file
    if os.path.exists(out_image_name):
        os.remove(out_image_name)
        
    for contour in contours:
        if count != 0:#the total layout,skip
            y = contour.reshape(len(contour),2)
            with open(out_image_name, 'a') as f:
                for i in range(0,len(contour)):
                    if i%2 == 0:
                        f.write(str(y[i,0])+','+str(110-y[i,1])+'\n')
        count = count + 1
        
    img = cv2.drawContours(dilate, contours, -1, (0,255,0), 3)
    cv2.imshow("img", img)
    
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    
outputContour('pic/code_lu_cut0.jpg','target_n_contours.dat')
#outputContour('pic/standard/N.jpg','standard_n_contours.dat')
