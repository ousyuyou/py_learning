#!/usr/bin/env python
# -*- coding: utf-8 -*-

#standard input
"""
print u'标准化输入','please input your name:'
name = raw_input()
print 'hello',name
"""
print '\n'
#中文支持
#print u'测试中文输出',u'中文输出OK'
print u'中文utf-8 encode'
u'中文'.encode('utf-8')
#每个中文3字节
print u'中文utf-8 decode','\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#格式化输出
print u'格式化输出','Hi,%s, you have $%d.' %('michal',1000000)
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print u'格式化整数，可补充0','%2d-%02d' % (3, 1)
#格式化小数，指定小数位
print u'格式化小数，指定小数位','%.2f' % 3.1415926
#%s可格式化任何类型
print 'Age: %s. Gender: %s' % (25, True)
#list
print '\n'

#说明：list与tuple，list为可变数组[],tuple为不可变数组()
classmates = ['Michael','Bob','Tracy']
print u'初始化classmates',classmates
#'len()获得长度'
print 'classmates length',len(classmates)
#'索引访问,0开始,可以用负数作为索引,表示倒数第几个'
print 'classmates[0]',classmates[0]
print 'classmates[-1]',classmates[-1]
#追加元素,append为追加到末尾
classmates.append('Adam')
print 'classmates append Adam',classmates
#insert到指定位置
classmates.insert(1, 'Jack')
print 'classmates insert Jack to 1',classmates
#pop末尾元素
classmates.pop()
print 'classmates pop',classmates
#pop(1)
classmates.pop(1)
print 'classmates pop(1)',classmates
#赋值替换
classmates[1] = 'Sarah'
print 'replace 1 to Sarah',classmates
#list中类型可以不同，不做限制
L = ['Apple', 123, True]
print 'L',L
s = ['python', 'java', ['asp', 'php'], 'scheme']
print 's',s
print s[2][0]#get asp
print '\n'

#tuple tuple不能变，它也没有append()，insert()这样的方法.不能赋值成另外的元素
classmates = ('Michael', 'Bob', 'Tracy')
print 'classmates',classmates
#仅有一个元素时，末尾必须有逗号,以便和数字进行区别
t = (1,)
print 't',t
print '\n'

#条件判断和循环
age = int(raw_input('input your age:'))
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
#for 循环
names = ['Michael', 'Bob', 'Tracy']
print u'for循环输出names'
for name in names:
    print name
sum = 0
#range函数提供0开始到小于101的数
print u'1-100加和'
for x in range(101):
    sum = sum + x
print sum
#while循环
print u'计算100以内所有奇数之和，while循环实现'
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
print '\n'

#dict,set;dict为map
d = {'Michael':95,'Bob':75,'Tracy':85}
print 'dict',d
#通过赋值直接追加key,value
d['Adam'] = 67
print 'dict',d
#key不能重复，如果key相同则会覆盖前面的值
d['Jack'] = 90
print 'dict',d
d['Jack'] = 88
print 'dict',d
#查询key是否存在
print 'Michael' in d
#查询key是否存在,get方法
print d.get('Thomas')
print d.get('Thomas',-1)#找不到则返回-1
#pop方法删除
d.pop('Bob')
print 'dict',d
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print 'set',s
s = set([1, 1, 2, 2, 3, 3])
print 'set',s
#add方法添加,remove方法删除
s.add(4)
print 'set',s
s.remove(4)
print 'set',s
#set方法可以做集合的并集，交集运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print 's1&s2',s1 & s2
print 's1|s2',s1 | s2
