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

## list generator:
list3=[ x*x for x in range(1,20) if x%2 ==0 ]
print('list3=',list3)
list4=[m+n for m in 'abc' for n in 'wxyz']
print('list4=',list4)
## string1 + string2 = string1string2
## str1 * 2 = str1str1







## generator: 








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
