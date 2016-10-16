#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
类通过class关键字创建，所有属性可以动态绑定
'''
'''
变量类型，访问控制
双下划线开头的代表private变量，不能外部访问，例如__name,__score
__xxx__ 双下划线开头，双下划线结束的为特殊变量，特殊变量是可以直接访问的，不是private变量
_name，单下划线这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
'''
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
        
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name  

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
print lisa.get_grade()
#动态绑定属性
bart.age = 8
print bart.age
#NG
#lisa.age
'''
使用type()函数判断对象类型
使用isinstance()也可以判断对象类型
'''
print 'type(123)',type(123)
print 'type(\'str\')',type('str')
print 'type(abs)',type(abs)
print 'isinstance(bart,Student)',isinstance(bart,Student)
'''
dir()使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
'''
print dir('ABC')
'''
配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x')
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
print getattr(obj, 'y')
print hasattr(obj, 'power')
print getattr(obj, 'power')

'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
装饰器@score.setter，负责把一个setter方法变成属性赋值
'''
class StudentDecorator(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = StudentDecorator()
s.score = 60# OK，实际转化为s.set_score(60)
print s.score# OK，实际转化为s.get_score()
#NG,ValueError
#s.score = 9999
'''
定制类，通过复写特殊的方法，可以实现特定的功能
例如：
在class中重写__str__()方法，可以以字符串形式输出类的实例；
__repr__() 方法是调试服务输出的；
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值；
要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

'''
class StudentPrint(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print StudentPrint('Michael')