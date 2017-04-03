#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bag_over_calculate(size,alist,threshold):
    m = int(size + threshold + 0.5)
    array = [int(alist[i]) for i in range(len(alist))]
    #for i in range(len(alist)):
    #    array[i] = int(alist[i])
    
    #背包大小为(size+threshold)的情况下能放入的最大值
    c = [[0 for i in range(m)] for i in range(len(array))]
    #每个数是否放入的标志;1:放入,0:不放
    d = [[0 for i in range(m)] for i in range(len(array))]
    
    j = 1
    for j in range(m+1):
        for i in range(len(array)):
            y = (0 if i == 0 else c[i-1][j])
            
            if j < array[i]:
                c[i][j] = y;
            else:
                x = (array[0] if i ==0 else c[i-1][j-array[i]] + array[i])
                if x > y:
                    c[i][j] = x
                    d[i][j] = 1
                else:
                    c[i][j] = y
                    d[i][j] = 0
            #self.calculate_count = self.calculate_count + 1
            
        if c[len(array)-1][j] >= size:
            break
    
    print c[len(array)-1][j]
    print "j= "+str(j)
    
    s = c[len(array)-1][j]
    i = len(array)-1
    index = []
    while i >= 0:
        if d[i][s] == 1:
            index.insert(0,i)
            s = s - array[i];
        i = i - 1
    
    print index
    return c[len(array)-1][j],index

array = [9548,35120,6509,10090,32050,25160,45601,16500,9810,10000,55000,5082,2000]
bag_over_calculate(95000,array,10000)
        