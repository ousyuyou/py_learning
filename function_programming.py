#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import functools
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

print '\n'
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
print '\n'
'''
filter()函数用于过滤序列
和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n % 2 == 1
#只保留奇数
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

#删除序列中的空字符串
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print '\n'

'''
sorted()函数就可以对list进行排序
sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
'''
print sorted([36, 5, 12, 9, 21])
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
#实现倒序排序
print sorted([36, 5, 12, 9, 21],reversed_cmp)
print '\n'
'''
函数作为返回值,包含一个内部函数
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
#f为函数
print f
#调用f时才实际的执行
print f()
print '\n'

'''
匿名函数,lambda
关键字lambda表示匿名函数，冒号前面的x表示函数参数
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
'''
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = lambda x: x * x
print f
print f(5)
print '\n'
'''
装饰器 Decorator
在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
#@log表示在调用now函数时执行log(now)
@log
def now():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    print time.strftime(ISOTIMEFORMAT, time.localtime())
	
"""
偏函数 functools.partial;等同于定义
def int2(x, base=2):
    return int(x, base)
"""
int2 = functools.partial(int, base=2)
print int2('1000000')