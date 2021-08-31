#!/usr/bin/python
# -*- coding: utf-8 -*-

##In this file, simple examples will be used to introduce all python functions:



Level=input('input level of the Hanno tower: ')
##Input parameters, it's always a string!

isinstance(Level,int)
##check if var Level is an integer or not

def Hanno(n,a,b,c):
	## define functions
	n=int(n)
	if n==1:
		print('disk',n,':',a,'->',c)
	else:
		Hanno(n-1,a,c,b)
		print('disk',n,':',a,'->',c)
		Hanno(n-1,b,a,c)
	return

Hanno(Level,'A','B','C')
## use functions

def _cus_sum(*args):
    result=0
    for ii in args:
        result=result+ii
    return result
## *args means the number of args is not defined. it works like a list/tuple.

list_add=[1,2,3,4]
res1=_cus_sum(*list_add)
res2=_cus_sum(1,2,3,4,5,6)
print(res1, res2)
## keyword type parameter may be added later

## default parameter:
def func(x,y=2):
    result=1
    while ii<=y:
        result=result*x
        ii=ii+1
    return result

## in this function, if y is not input, its default value is 2





## the difference between for loop and while loop:
## for xx in list:
## while yy<=100:
## for loop in a list/tuple/dict etc.
## while 'condition'





## anonymous function (lambda)

_square=lambda x: x*x
_square(5)

## equals:

def _square(x):
    return x*x
_square(5)

## lambda function can only return 1 simple equation, the biggest advantages are: 1, it doesn't need a function name, so won't cause any conflict; 2, convenient in some scenarios.
_square_list=list(map(lambda x:x*x, range(5)))
print (_square_list)




## List, tuple and dict:
list1=['a','b',123,[1,2,4]]
## list/tuple can be element of another list/tuple
list1.append('test')  ## add an element to the last
print(list1)
list1.insert(1,'2nd')  ## insert an element to index
print(list1)
list1.pop(2)  ## delete an element at index (last element by default)
print(list1)

tuple1=(1,2,3,'abc')
print('print format %2s %2d' % (tuple1[1],tuple1[2]))

dict1={'mich':50,'dean':45,'loren':'score'}
##format is dict_name={key1:value1,key2:value2......}
dict1['ida']=550  ## add elements like this
print(dict1['loren'])
##dict_name[key_n]=value_n






##slice for list/tuple/string:
list2=list(range(100))
list2[2:90:5]
##from 2nd element to 90th element, pick with gap 5.
##default value is [0:len(list2):1]
## backward slice:
list2[-10:] ## last 10 elements of list2
list2[-10:-1] ## last 9 elements, the last element EXCLUDED
list2[-1] ## last element
list2[-5] ## 5th element from backward
(1,2,34,5,56,7)[::3]  ## directly slice on a tuple
'ABCDE'[1:3] ## slice on a string






##Iteration:
from collections.abc import Iterable 
## upper/lower case sensitive.
var='abcde'
isinstance(var,Iterable)
## confirm if a variable (including int/str/list/tuple...) is iterable or not.

dict1={1:2,3:4,5:6}
for k in dict1: ## for keys. or: for k in dict1.keys():
    print (k)
for v in dict1.values():    ## for values
    print (v)
for k,v in dict1.items():    ## for key-value pairs
    print (k,v)

## multi-var iteration:
for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)

## list with for and if:
list3=[ x*x for x in range(1,20) if x%2 ==0 ]
print('list3=',list3)
list4=[ m+n for m in 'abc' for n in 'wxyz' ]
print('list4=',list4)
## string1 + string2 = string1string2
## str1 * 2 = str1str1





## generator: 
## generator：为了节约内存，而保存一个“算法”，并不直接生成list。典型的例子：
aa=[ x*x for x in range (100) ]
bb=( x*x for x in range (100) )
## 此处的bb不是list，因为是小括号；也不是tuple，因为括号里是公式，而非元素的列举。
## 这两条命令执行完，aa会立即申请100个元素的list，而bb只是一个“100以内的完全平方数”的算法，不占内存。
## 另一个典型的例子：
def _odd_num():
    n=1
    yield n
    while True:
        n=n+2
        yield n
##这个函数用的不是return，而是yield，它就不再是函数，而是generator。generator不能用return返回值（只能用return中止执行）。这个generator代表的就是全部奇数，它是无限集合，所以不可能放在内存里。
##它的运行逻辑是，每次运行到yield时，返回yield后跟的变量，且保存当前状态作为断点。执行next（）命令后从这个断点继续执行，直到下次yield。

##调用方法，包括两种：
## 1，
for nn in _odd_num():
  if nn<=20:
   print(nn)
  else:
   break

##2，
od=_odd_num()        
##注意这里必须先把_odd_num()赋值到generator 实例 aa，否则后面next(_odd_num())并不会迭代。因为_odd_num()是一个定义，而非一个实例。
nn=1
while nn<=20:
 xx=next(od)
 ## 这里必须赋值，因为next函数只在交互式界面会返回值，在脚本中就不显示了。
 ## od.next()的写法是不对的。
 print(xx)
 nn=nn+1




## function can also be assigned to var:
f=abs
print(f(-1))   ##=abs(-1)=1
## function can also be re-assigned (DANGER)
## abs=10
## abs(-1)   will return error, because this will be transfered to 10(-1), which is wrong.
def absAdd (x,y,f):
    return f(x)+f(y)

print(absAdd(-5,6,abs))




## map-reduce and filter

list1=[1,-2,3,-4]
def f1(in1):
    in1=int(in1)
    return abs(in1)

list2=list(map(f1,list1))
## logic of map:
## list1=[a,b,c,d]
## list2=[f(a),f(b),f(c),f(d)]
## Notice, the result of map is a list. so you must use list().
print(list2)

def f2(in1,in2):
    in1=int(in1)
    in2=int(in2)
    return in1*10+in2

from functools import reduce
result3=reduce(f2,list1)
## import reduce first!!
## logic of reduce:
## the function for reduce MUST accept 2 inputs
## list1=[a,b,c,d]
## result=f(f(f(a,b),c),d)
## result of reduce is a variable, not a list.
print(result3)


## filter is a tool to filter a list with a function, keep the true item and delete the false item.

def is_odd(n):
    n=int(n)
    return n%2==1
    ## if n is odd, then return True, if n is even, return False.

list4=list(filter(is_odd,[1,2,3,4,5]))
## the structure of filter is nearly the same with map.
print (list4)





## sort:
example_list=[1,2,35,25,4]
## sort(example_list) <<<< this is WRONG
example_list.sort()     ## this is right
example_list.sort(reverse=True)

## sorted: this function is an enhanced function for sort, it can define extra functions for sort.
## sorted(listA,keys=func[,reverse=True]) , by default reverse=False

score_list=[('Adam',65),('Jack',70),('Beth',80),('Dante',62)]

def _rank_on_score(n):
    return n[1]

ranking=sorted(score_list,key=_rank_on_score,reverse=True)

print(ranking)

## the difference between sort and sorted:
## 1, gramma:
## list1.sort()         sorted(list1)
## 2, sorted WON'T change original list, but sort will permanantly change original list!








## to apply shell script:
import subprocess as sp
Command="sh /home/guchong/script.sh"
## Command here can be a command or a shell script
sp.call(Command,shell=True)

### 3 types of import files:
## import subprocess as sp 		## the string after 'as' is like the alias of the module
## import math	
## from math import *			##like 'import math'
## from support import print_func 	## just import a part of the module
