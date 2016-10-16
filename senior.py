#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable
import os

'''
切片，从数组中切出一段
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print 'L',L
print 'L[0:3]',L[0:3]
#索引为0情况下可以忽略
print 'L[:3]',L[:3]
#倒数切片，取出最后两个
print 'L[-2:]',L[-2:]

#范围切片
print '\n'
L = range(100)
print 'L',L
print 'L[10:20]',L[10:20]
#前10个数，每两个取一个：
print 'L[:10:2]',L[:10:2]
#所有数，每5个取一个
print 'L[::5]',L[::5]

#字符串切片,可用来对字符串进行分割
print '\'ABCDEFG\'[:3]','ABCDEFG'[:3]
print '\'ABCDEFG\'[::2]' , 'ABCDEFG'[::2]
print u'中文我是中国人[-3:]',u'中文我是中国人'[-3:]

'''
迭代
只要是可迭代对象，均可以使用for...in循环进行迭代
'''
#dict默认迭代key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
#只迭代value
for value in d.itervalues():
    print value
#同时迭代key,value
for key,value in d.iteritems():
    print key,value
#判断是否为可迭代对象
print 'str is iterable',isinstance('abc', Iterable)# str是否可迭代
print 'list is iterable',isinstance([1,2,3], Iterable) # list是否可迭代
print 'number is iterable',isinstance(123, Iterable) # 整数是否可迭代

#想要获得索引时，使用内置的enumerate函数
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
#for循环中引用多个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

print '\nfunction as iterator'
#函数返回值作为迭代器
def fab(max):
    n, a, b = 0, 0, 1 
    while n < max:
        yield b
        a, b = b,a + b
        n = n + 1

for n in fab(5):
    print n

'''
列表生成式
'''
#range指定范围
print u'\n列表生成式'
print range(1,11)
print [x * x for x in range(1,11)]
#使用if判断
print [x * x for x in range(1,11) if x%2 == 0]
#使用多层循环
print [m + n for m in 'ABC' for n in 'DEF']
#列出当前文件夹的文件
print [d for d in os.listdir('.')]
#迭代多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k ,v in d.iteritems()]
L = ['Hello', 'World', 'IBM', 'Apple',123]
#转换为小写字母
print [s.lower() for s in L if isinstance(s, str)]

print u'\迭代器'
'''
生成器，创建list时不需要事先全部创建并保存在内存中，
仅仅保存算法，通过迭代或者调用next方法去执行下一步；
每次在执行到yield时暂停，遇到next()时从yield处继续执行
'''
L = [x * x for x in range(10)]
print L
#迭代器使用()
g = (x * x for x in range(10))
print g
print g.next()

for n in g:
    print n

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
o.next()
o.next()
o.next()

#直接迭代
for g in odd():
    print g