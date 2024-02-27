day2复习
1.运算符
1) 数学运算符
print(2**3) #的立方
print(4*(1/2)) #4开平方
比较运算符(<,>,==,!=,>=,<=)
print(0<10<100)
逻辑运算符(and,or,not),
赋值运算符(=,+=,-=,=,/= ...)
运算顺序 数学->比较->逻辑->赋值

2)数字类型
int, float(2e4支持科学计数法),bool
isinstance(数据,类型)
数据转换: 类型名(数据)
input('请输入') 输入的都是str

3.分支结构:if
语法结构

if 条件语句:
     语句块
if 条件语句
    语句块1
else:
    语句块2
if 条件语句1
    语句块1
elif 条件语句2
    语句块2
elif 条件语句3
    语句块3
else
    语句块n    
所有为0为空的都会转换为False,其它都是true

python中的循环结构有两种: for循环,while循环
1.for循环
a.语法
for 变量名 in 序列:
    循环体1
    循环体2
b.说明
for     -  关键值,固定的
变量名  - 和声明变量的时候的变量名要求一样
in      - 关键字,固定写法
序列  - Python中的序列有:字符串,列表,元组,字典,集合,range,生成器和迭代器等
:       - 固定写法
循环体  - 和for保持一个缩进的一条或者多条语句
c.执行过程
当程序执行到for循环的时候:让变量去序列中取值,一个一个的取,取完为止.每取一个值,执行一次循环体.

for date in 'abc':
    print('====',date)

date = 'a' print('====',date)
date = 'b' print('====',date)
date = 'c' print('====',date)
==== a
==== b
==== c
range函数
range(n) - n是正整数,产生0~n-1的所有整数语法,python3.x是无效的

for num in range(10):
    print(num)
range(m,n)      #- m,n都是整数,并且n>m,产生m~n-1的所有整数
for num in range(100,1000):
    print(num)
range(m,n,s)        #- m,n,s都是整数,并且n>m,产生m~n-1,每次加s
for num in range(0,101,2):
    print('===:',num)
注意:xrange是python2.x的,python3.x是无效的

练习:

计数1+2+3...+100的和

sum1 = 0
for num in range(1,101):
    sum1 += num
print(sum1) 
sum1 = 0 代码解析
num = (1,2,3,4)
num =1 sum1 += num , sum = sum1 + num , sum1 = 0 + 1 =1
num =2 sum1 += num , sum = sum1 + num , sum1 = 1 + 2
num =3 sum1 += num , sum = sum1 + num , sum1 = 1 + 2 + 3
num =4 sum1 += num , sum = sum1 + num , sum1 = 1 + 2 + 3 + 4 = 10
print(sum1) #10

2.while循环
a.语法
while 条件语句:
    循环体//print sum
b.说明:
while       - 关键字,固定写法
条件语句    - 可以是数据,变量,运算表达式等.不能是赋值运算
:           - 固定写法
循环体         - 和while保持一个缩进的一条或者多条语句(会被重复执行)
c.执行过程:
先判断条件语句是否为True,为True就执行一次循环体
执行完循环体再判断条件语句是否为True,为True就再执行一次循环体
执行完循环体再判断条件语句是否为True,为True就再执行一次循环体
以此类推,直到判断条件语句的结果为false,整个循环直接结束

两个极端: 1.当条件语句永远为True,会造成死循环的现象
2.一开始条件语句的结果就是False,那么循环一次都不会执行

count = 0
、、、
while count < 4://当count=>4 false
    print ('======',count)
    count = count+1
、、、、
print(count)    
count = 0
count < 4 0<4 True print('======',count) count += 1 count = count + 1 = 0+1 =1
count < 4 1<4 True print('======',count) count += 1 count = count + 1 = 1+1 =2
count < 4 2<4 True print('======',count) count += 1 count = count + 1 = 2+1 =3
count < 4 3<4 True print('======',count) count += 1 count = count + 1 = 3+1 =4
count < 4 4<4 False
print(count) print(4)

python循环中的continue,break,else
1.continue
用法:
continue 是关键字,只能出现在循环体中

功能:
执行循环体的时候,如果遇到continue,就直接结束当次循环,直接进入下次循环判断

for x in range(10):
    if x % 3 == 0:
        continue
    print(x)    
    print('======')
2.break
用法:
break 是关键字,只能出现在循环体中

功能:
执行循环体的时候,如果遇到break,整个循环直接结束

for x in range(10):
    print(x)
    break
    print('!!!!!!!!!!')
练习:

从0+1+2+....求看到的时候和超过10000000,求出这个数

x = 0
sum1 = 0
while  1 :
    x += 1
    sum1 += x 
    if sum1 >1000000 :
        print(x , sum1)
        break
sum1 = 0
for x in range(1000000):
    sum1 += x       
    if sum1 >1000000 :
        print(x , sum1)
        break
3.else
a.语法
for 变量 in 序列:
    循环体
else:
    语句块 

while 条件语句:
    循环体
else:
    语句块 
b. 执行过程:
如果循环自然结束,else对应的语句块会执行:
如果循环因为遇到break而结束,else对应的语句块不执行

for x in range(5)
    print(x)
eles:
    print('循环结束,没有遇到break') 

for x in range(5)
    print(x)
    break
else:
    print('循环结束')
补充:循环嵌套
循环嵌套:
在循环体中又有循环结构

执行过程:
外循环执行一次,内循环执行完

for x in range(5):
    for y in range(4):
        print(x)
        print(y)
    
x = (0,1,2,3,4) 原理解读
x= 0 y= (0,1,2,3)
y= 0 print(x) print(y)
y= 1 print(x) print(y)
y= 2 print(x) print(y)
y= 3 print(x) print(y)
x= 1 y= (0,1,2,3)
y= 0 print(x) print(y)
y= 1 print(x) print(y)
y= 2 print(x) print(y)
y= 3 print(x) print(y)
num = 12345
num %= 10
print (num)