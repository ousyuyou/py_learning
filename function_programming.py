#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
"""
#函数作为参数传入
def add(x,y,f):
    return f(x) + f(y)

print add(-5,6,abs)

"""
map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
"""
def square(x):
    return x * x

L = range(1,10)
#第一个参数为函数本身，第二个参数为list
print map(square,L)
#转换为字符串
print map(str,L)

"""
reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""

#将序列[1,3,5,7,9]变换成整数13579
def fn(x,y):
    return x * 10+ y
#print reduce(fn,[1,3,5,7,9])

#配合map()，完成一个str转换为int的函数
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print 'convert str to int',reduce(fn,map(char2num,'13579'))

#格式化英文输入,第一个字母为大写，以外为小写
def formatAlpha(s):
    return s[0:1].upper() + s[1:].lower()

names = ['adam','LISA','barT']
print map(formatAlpha,names)
#求乘积
def prod(x,y):
    return x * y

print reduce(prod,[1,2,3,4,5])
