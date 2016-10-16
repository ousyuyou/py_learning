#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

"""
method my_abs
"""
def my_abs(x):
    if not isinstance(x,(int,float)):#类型检查
	    raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#空函数
def nop():
    pass #什么都不做,等同于java的;

print abs(10)
#print abs('a')

"""返回多个值"""
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi/6)
print x,y

#实质上返回的是tuple类型，只是允许直接用多个变量按照顺序接收
r = move(100,100,60,math.pi/6)
print r

"""默认参数,设置默认值可不需要传参数"""
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print 'power(5,3)',power(5,3)
print 'power(5)',power(5)
print '\n'

#多个默认参数时的指定方法
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Bob', 'M', 7)#按顺序指定
enroll('Adam', 'M', city='Tianjin')#指定city值
#默认值如果为list，初始化为Noe，否则多次调用时可能会出问题
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print '\n'

#计算a^2+b^2+c^2...
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#传递进来需要为list或者tuple
print calc([1, 2, 3])

#修改为可变参数，内部接受到的直接为tuple类型
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1,2,3,4]
print calc2(1,2,3)
print calc2(*nums)
print '\n'
"""关键字参数,kw可传入0个或任意个含参数名的参数，类型为dict"""
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)

"""参数组合,参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数"""
def func(a, b, c=0, *args, **kw):
    #for str in args:
	#    print str
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
#神奇的自动匹配
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)