#!/usr/bin/python
# -*- coding: utf-8 -*-

##In this file, simple examples will be used to introduce all python functions:



Level=input('input level of the Hanno tower: ')
##Input parameters, it's always a string!

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
## 此处的args允许输入若干个变量，反而不允许输入list了，因为list不是数值型变量，无法用它执行加法运算。
# 但如果已有一个已保存想输入的数字的list或tuple，可以用*将list或tuple转化成变量列。例如_cus_sum(*list1)。


def learnPara(*vargs,**kwargs):
    print(vargs,kwargs)
## 其中 *vargs 表示若干个变量（可以为0个，变量允许是list或tuple等）。而**kwargs则是生成一个dict（可以为空），然后以a='b',c='d'的形式输入，生成{a:'b',c:'d'}形式的dict。
# 但注意，一旦开始了kwargs，就不允许再输入普通参数。
# 典型的输入方式如下：
learnPara(1,2,'M',4,[5,6],{1:2,3:4},a='b',c='d')
#返回值为：
#(1, 2, 'M', 4, [5, 6], {1: 2, 3: 4}) {'a': 'b', 'c': 'd'}
## 但是： learnPara(1,2,3,4,[5,6],{1:2,3:4},a='b',c='d','ef','ghi') 这种写法就是错的，因为在kwargs之后又开始输入普通参数了。


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
## while loops when the 'condition' is met.





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




## 定义模块: 写完函数最后需要再加一条:
## vim module.py
def function():
 pass

if __name__=='__main__':
 function()
## 其中function是子函数的名字。这样定义好的模块后可以这样引用:
## import module ##不会直接执行函数
## module.function() ##直接执行该函数。

##放置自定义模块的路径建议通过PYTHONPATH环境变量定义:
## export PYTHONPATH=/path/to/your/project:$PYTHONPATH

##导入子目录的模块可用import path.to.your.project.module
##文件夹之间用.分开
##每个文件夹下都必须有__init__.py文件




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





## 定义类:
class Student(object):      ##定义'类'，类名按惯例需要首字母大写，括号内写其父类的名字。object是所有类的始祖。
    def __init__(self,name,gender,*other):       
        ## 此处定义该类型!必须!包含的'属性'property。self是隐性属性，未来调用时不用写。以*开头的参数可以不包含因为它是可变参数，允许参数个数为0。
        ## 若没有__init__则没有必须属性，可以建立空实例。
        self.name=name      ##此处仍然允许有逻辑语句，例如：
        if gender == 'F' or gender == 'M':
            self.gender=gender
        else:
            self.gender='error'
        self.other=other
    __slots__=('name','gender','age','other')       
    ##__slots__用来限定允许赋值的属性。在这个列表之外的属性将不被允许。例如student.city='BeiJing'就将不再被接受。如果没有这一句意味着任何属性都可以赋值
    def print_profile(self):        ##此处定义一个或多个该类的'方法'method。注意括号里的self。它也一样是隐性属性。
        ## 此处还有一个值得注意的地方就是函数的入参类型，不仅可以是int、str、list等传统类型，还可以是某个类的实例！
        ## 但是因为这个函数是在类的内部定义的，所以只能用作类的方法。而不能直接用print_profile(student3)的方式调用。
        ## 如果该函数写在类的外面，就可以将某个类的实例作为入参传给它来执行了。
        if self.other != ():        ##*other参数是一个tuple。()就是空tuple
            addressFlag=False
            paraLength=len(self.other)
            for ii in range(paraLength):
                for key in self.other[ii].keys():
                    if key == 'addr':
                        addressFlag=True
            if addressFlag == True:
                print('%s%s%s%s%s%s' % ("Name:", self.name,"; Gender:", self.gender, "; Address:", self.other[0]['addr']))
            else:
                print('%s%s%s%s' % ("Name:", self.name,"; Gender:", self.gender))
        else:
            print('%s%s%s%s' % ("Name:", self.name,"; Gender:", self.gender))

## 定义子类：
class GoodStudent(Student):     ## 括号里写父类的名字
    pass

## 子类可以继承父类的所有属性和方法，并在其上添加自己的特殊属性和方法。
# 如果子类定义了和父类同名的属性或方法，在子类实例调用时，使用子类的属性或方法（向上覆盖）

class Person(object):
    pass

class Shanghai(object):
    pass

## 定义混合类：
class MixedStudents(Student,Person,Shanghai):
    pass
##一个类可以继承多个类的属性和方法（多个父类）


## 使用类赋值：
student1=Student('Albert','male')
student2=Student('Bill','M',{'addr':'BeiJing','hight':175,'score':80})
student3=Student('cinderella','F',{'hight':160})

## 输出属性：
## 调用方法：
student1.print_profile()
## 调用属性：
student1.gender

##在类外定义函数：
def get_student_gender(student):
    return student.gender

get_student_gender(student3)

## 允许输入没有在__init__里定义的属性，因为__init__里只定义!必须!属性。但是该属性可能与方法冲突，所以可能无法用标准方法处理：
student3.score=65
student3.score

## 类的一些特殊方法（系统默认自带方法）

class myObject(object):
    def __init__(self,name):        ##初始化属性
        self.__name__=name
    def __repr__(self):     ## 此方法的含义是，输入一个object实例名（不带括号），打印该方法返回值取代类似<__main__.myObject at 0x7fa66a8cb350>这样的不易读信息。
        return "the name of the object is %s" % self.__name__
    def __iter__(self):     ## 此方法用于迭代，返回自己
        return self
    def __next__():         ## 此方法就是迭代的next命令，返回想返回的值
        return 1
    def __getitem__(self,n):    ## 此方法用来将实例当作一个list，通过参数n获取第n项的值（调用方法也类似list）
        return n
    def __getattr__(self,attr):     ## 此方法本来就存在（事实上执行object.property就是执行object.__getattr__(property)），所以此处只是补充__getattr__方法，在正常的__getattr__无法工作时，执行这个。
        if attr == 'score':
            return 999
    def __call__(self,*args):   ## 输入一个object实例名（带括号，或者说，执行这个实例）时，执行__call__方法。这个方法在装饰类中尤其重要。
        print(args)


isinstance(Level,int)
aaa=[1,2,3]
isinstance(aaa,tuple)
isinstance(student3,Student)
##check parameter type. Type can be int, str, list, tuple, customized class etc... return value is bool: True or False.
##用子类创建的示例，isinstance检查既是父类又是子类。
##另外还有类似的函数type()，返回值不是布尔值，而是直接是类型名。例如：
type(aaa)
type(student2)

## 通过dir函数可以查看某个实例或变量包含哪些属性或方法：
dir('AAA')
dir(student2)

##也可以通过hasattr()函数判定某个实例或变量是否有某个属性（在dir列表里的就会返回True）。例如：
hasattr(student2,'name')




## 参数类型: 
## 蛇形命名的参数：普通参数
## 首字母大写驼峰命名： 普通类
## 首字母小写驼峰命名： 普通实体
## __xxx__: 特殊参数，一般是系统规定的，不要覆盖
## __xxx: 私有参数，在类之外无法访问（有强行访问的办法但是强烈不建议）
## XXXX (大写): 常量。也可以修改但约定俗成不要修改
## _xxx: 普通参数但不希望被外界访问，也就是说，虽然是普通参数，但是建议使用者视同私有参数。





## 闭包(closure)：
## 定义：
def outerFunc(outerPara):
    def innerFunc(innerPara):
        print(outerPara,innerPara)      
        ##这里是闭包的核心点之一。按理说外层函数执行完之后，外层的参数outerPara会被释放。但此处通过内层函数引用它把它封在了内层函数里，这个参数就不会释放，从而构成一个数据+函数的实例。
        ##这样的实例可以同时并存多个，封入不同的outerPara参数。
    return innerFunc
        ##这里是闭包的核心点之二。返回的是内层函数本身，而不是执行内层函数后的返回值（注意后面没有括号！）。
        ##如果这里后面带了括号，返回的就是innerFunc的执行结果了。因为调用outerFunc时没有输入innerPara的地方，这么改就会报错了。

##使用：
testFunc=outerFunc('test1')
testFunc
##这一句的返回是一个函数，就是innerFunc，同时将'test1'作为outerPara封在了里面。但是不执行innerFunc。输出结果类似于：
## <function __main__.outerFunc.<locals>.innerFunc(innerPara)>
testFunc('test2')
##因为testFunc实质上是封装了outerPara参数的innerFunc函数（不带括号！）所以这一句等效于innerFunc('test2')
##甚至更直接的用法可以这样:
outerFunc('test1')('test2')

##装饰(decorator):
## 简而言之，装饰是闭包调用的一种语法糖。格式如下：
## 首先定义装饰函数：
def testDeco(fn):
    print('the function name is',fn.__name__)   ##这句写法不合适（1），下面会解释
    def realDeco():
        print ('starting function',fn.__name__)
        fn()
        print (fn.__name__,'function finished')
    return realDeco     ##和闭包类似的，这里必须不带括号。

## 然后定义真实函数，注意在定义真实函数的前面一行加上@装饰函数的名字：
@testDeco
def realFunc():
    print ('hello world')

## 这种写法的实质就是执行如下语句：
## def realFunc():              ##先定义真实函数
##     print ('hello world')
## realFunc=testDeco(realFunc)  ##然后执行这个赋值语句。这里就可以看出来（1）不合适的原因。因为它并没有被封在子函数里面，所以它会被testDeco函数直接显式执行。

## 接下来可以执行realFunc和realFunc()检查结果。（其实realFunc已经变成了realDeco的闭包了。）
## realFunc
## <function __main__.testDeco.<locals>.realDeco()>
## 而realFunc()则是将reanFunc作为形参fn的实参传入然后执行realDeco()：
## realFunc()
## starting function realFunc
## hello world
## realFunc function finished

def decorator_one():
    pass
def decorator_two():
    pass

@decorator_one
@decorator_two
def func():
    pass
##等效于    func = decorator_one(decorator_two(func))

def decorator(arg1,arg2):
    pass

arg1=1
arg2=2
@decorator(arg1, arg2)
def func():
    pass
##等效于 func = decorator(arg1,arg2)(func)

## 上述例子中func函数都没有入参。而如果有入参，写法是这样的：
## func(funcPara)
## decorator_one(decorator_two(func))(funcPara)
## decorator(arg1,arg2)(func)(funcPara)
## 而不是 decorator_one(decorator_two(func(funcPara))) 或者
## decorator(arg1,arg2)(func(funcPara))

##带参数的decorator必须有多层内函数架构的原因：
##从上面的等效式就能看出来，func = decorator(arg1,arg2)(func)，而不是 func = decorator (arg1,arg2,func)。
# 定义decorator的时候必须得允许接受函数作为入参，所以要么无法接纳其他参数，成为decorator(func)的形式；要么并列接纳其他参数成为decorator(arg1,arg2,func)的形式。
# 而这两种形式都是不对的。后者使用func调用时，并没有接纳arg1和arg2的入口（他们是decorator的入参，而不是func的入参）。所以如果decorator本身需要带参数，只能定义两层或更多的内层函数。例如：

def directDeco(arg1):       ##最外层，直接装饰，此处带的是装饰函数自己的入参，它会通过闭包被保留。
    def realDeco(func):     ##中间层，这是真正的装饰函数，如果装饰函数没有入参就可以直接用它作为最外层。注意这个真正的装饰函数的入参是被包裹的函数名func。
        def returnDeco(funcPara):       ##最内层，和普通装饰函数的最内层类似。它的入参是被装饰的函数func的入参，不然后来执行func的时候获取不到正确的入参。当然，也可以任性点，这里的入参写*args，然后后面从*args中组合出最终func需要的入参并传给func。
            print(arg1)
            func(funcPara)
        return returnDeco   ##注意这里和闭包、普通装饰函数类似，必须不带括号
    return realDeco     ##必须不带括号

def directDeco(arg1):       ##同上，略
    def realDeco(func):     ##同上，略
        def returnDeco(*args):       ##最内层，和普通装饰函数的最内层类似。任性版入参写法：
            print(arg1)
            func(args[1])   ##如果这么写意味着执行func时至少需要2个入参。下面有分析：
        return returnDeco
    return realDeco


@directDeco("test deco para")
def func(funcPara):
    print(funcPara)

## 此时func被重新定义： func = directDeco("test deco para")(func)，
## 执行func命令可见它其实已经变成了returnDeco函数：<function __main__.directDeco.<locals>.realDeco.<locals>.returnDeco(*args)>
## 而执行func(*args)的逻辑链相当于：
## directDeco("test deco para")(func)(funcPara) -> realDeco(func)(funcPara) (其中realDeco将"test deco para"这个入参闭包了) -> returnDeco(funcPara)
## -> 所以funcPara实际上变成了returnDeco的入参！这个funcPara就是*args！ 
## 最后，在执行returnDeco时，内部的func(args[1])这一句意味着args[1]必须存在，也就是funcPara[1]必须存在，而如果func只有一个入参，就会报错。
## 事实也是如此：
## func(123,45)
##  test deco para
##  45  <<打印的是funcPara[1]


## 装饰器装饰类
## 示例1：装饰器本身无入参：

class decoObject(object):
    def __init__(self,func):    ##__init__()是在给某个函数decorator时（也就是下面的@语句时）被调用，用于初始化参数。如果装饰器本身不含参数则此处可以将被装饰的函数初始化。
        self._func=func
    def __call__(self,*args):   ##__call__()是在调用被decorator函数时被调用的。注意这种形式下，因为_func已经在__init__里定义了，所以这里只需要定义_func的入参args。
        print('test')
        self._func(args)

@decoObject
def testDecoObject(*args):
    print('this is the output:' , args)


##示例2：装饰器本身有入参：
class decoObject2(object):
    def __init__(self,*decoPara):   ## 装饰器本身有入参的init里只能定义它自己的入参，这里相当于带入参的函数式装饰器的最外层，它的入参除了self以外还有装饰器本身的入参。
        self._decoPara=decoPara
        ##  self._func=func         ## 和函数式装饰相同，因为被装饰函数和装饰函数自身的入参不能并列，所以此处不能先定义func，否则func就要出现在init的入参里和装饰器本身的入参并列。func的定义要放在call里面。
    def __call__(self,func):        ## 这里相当于带入参的函数式装饰器的中间层，它的入参除了self以外，只有被包裹的函数func。
        def actualDeco(*args):      ## 这里相当于带入参的函数式装饰器的最内层，它的入参是被包裹的函数func的入参。
            print('test')
            print(self._decoPara)   ## 可以通过类闭包把最外层装饰器的入参传递过来
            func(args)
        return actualDeco

@decoObject2('test',123)     ##调用方式也类似于带入参的函数式装饰器
def testDecoObject2(*args):
    print("this is the actual function:",args)

## 其逻辑链跟函数式装饰函数很像：
## testDecoObject2(args) -> decoObject2('test',123)(testDecoObject2)(args) -> __call__(testDecoObject2)(args) （通过闭包包含_decoPara入参） -> actualDeco(args)
## >>> testDecoObject2
## <function decoObject2.__call__.<locals>.actualDeco at 0x7f52d5d6a7a0>

## @property 装饰
## 该装饰（python自带，无需预先定义）的含义是将一个类的方法装饰成属性。

## good references:
#  https://zhuanlan.zhihu.com/p/27449649        <<<<best for closure
#  https://www.the5fire.com/closure-in-python.html
#  https://www.cnblogs.com/BlueSkyyj/p/8884236.html

#  https://www.cnblogs.com/zh605929205/p/7704902.html   <<<<best for decorator
#  https://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html    <<<<best for decorator




#### 错误和调试：
try:            ##此处开始需要测试的语句。其中任何一句碰到错误，则try程序段中在它后面的语句都不再执行，转而跳入相关的except语句段。
    print(1)    ##IDE比较智能，这里想写一个语法错误，就直接被提示了。如果没有IDE，可以故意写一些错误语句来测试
    print(2)
    print(3)
except SystemExit:      ##当遇到这种错误SystemExit时，执行这一段。except语句可以有一句或多句。但注意，一旦执行过一个except，就会跳过后续的其他except。
    print(4)
except ArithmeticError: ##遇到另一种错误ArithmeticError，执行这一段。注意，如果两种错误有父子关系，一定要把子写在前面。否则子错误永远无法捕获。
    print(5)
except BaseException as err:    ##遇到其他错误，执行这一段。BaseException是所有错误的父类所以一定能抓住。最后最好定义一下别名，然后打印，否则不知道到底错误是啥。
    print(err)
else:                   ##整个try代码段都没有遇到错误，执行这一段。注意：是没有遇到错误，而不是没有捕捉到错误。即使因为定义的except不合理而导致没有触发except，但有其他报错，仍然不会执行else语句段。
    print(6)
finally:                ##无论try代码段有没有遇到错误，最后都执行这一段。注意如果前面的except捕捉到了错误，则最后执行这一段；但如果前面的except语句写的不合理，没有捕捉到错误，则是先执行完这一段，再抛出报错。所以用BaseException作为最后的报错保护是很有必要的。
    print(7)


## 官方错误类型列表： https://docs.python.org/3/library/exceptions.html#exception-hierarchy