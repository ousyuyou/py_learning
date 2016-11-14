#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_min_group(start,array,value):
    global count
    count = count + 1
    min_sum = sys.maxint
    min_index = []
    for index,curr_val in enumerate(array[start:]):
        if curr_val > value and curr_val < min_sum:
            min_sum = curr_val
            min_index = [start+index]
        else:
            if sum_array(start+index,array) > value-curr_val:
                min_sum_rt,min_index_rt = find_min_group(start+index+1,array,value-curr_val)
                if min_sum_rt != sys.maxint and min_sum_rt!= 0:
                    if curr_val + min_sum_rt > value and curr_val + min_sum_rt < min_sum:
                        min_sum = curr_val + min_sum_rt
                        min_index = []
                        min_index.append(start+index)
                        for i in min_index_rt:
                            min_index.append(i)
    return min_sum,min_index

def sum_array(start,array):
    sum = 0
    for val in array[start:]:
        sum = sum + val
    return sum

arr = [50100,6485.67,28828.692,22957.416,34786.278,17114.157,30036.915,17297.244,6485.679,4373.19,16215.858,8333.298,34786.278,17511.237,16567.254,8333.28,6247.386,6485.661,6722.298,8557.083,8557.083]
print sorted(arr,reverse=True)
'''
for index,curr_val in enumerate(arr[2:]):
    print index
    print curr_val
'''
count = 0
min_sum,min_index = find_min_group(0,sorted(arr,reverse=True),350000.25)
print 'count: '+str(count)
print min_sum
print min_index
