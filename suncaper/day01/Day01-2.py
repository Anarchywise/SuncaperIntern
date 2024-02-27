# 2.比较运算符：>、<、==、!=、>=、<=
# 所有的比较运算符的结果都是布尔值
#
# print(100>10)       #True
# print(100>1000)     #False
# print(100<10)       #False
# print(100<1000)     #True
# print(100==100)     #True
# print(100==10)      #False
# print(100!=100)     #False
# print(100!=10)      #True
# print(100>=100)     #True
# print(100>=1000)    #False
# print(100<=100)     #True
# print(100<=10)      #False
# 将运算结果赋值给变量
#
# result1 = 10 >= 1
# result2 = 100 + 100
# print(result1,result2)
# 3.逻辑运算符： and ,or ,not
# 所有逻辑运算符的结果都是布尔值，操作对象也是布尔值。
#
# a.逻辑与运算： and
# 运算规则：
#
# 两个都为True,结果才是True；只要有一个是False，结果就是False。（相当于并且）
#
#  True and True   = True
#  True and False  = False
#  False and True  = False
#  False and False = False
# 练习:
#
# 要求进入公司的条件：分数不低于90 并且年龄大于25岁
#
#  score = 90
#  age = 20
#  print(score >= 90 and age > 25)
# 判断num是否在0到100之间
#
# num = 10
# print(0 <= num <= 100)
# print(num >= 0 and num <= 100)
# b.逻辑或运算：or
# 运算规则：
#
# 两个都为False，结果才为False；只要有一个是True，结果就是True.(想当与或者)
#
# True or True   = True
# True or False  = True
# False or True  = True
# False or False = False
# 应用：
#
# 要求多个条件中至少有一个条件满
#
# 练习:
#
# 获取奖学金的条件：学习成绩大于90分或者操评分大于95分
#
# score1 = 80 #学习成绩
# score2 = 90 #操评分
# print('是否获得奖学金：',score1>90 or score2>95)
# c.逻辑非运算： not
# 运算规则：
#
# True变False，false变True
#
# not True  == False
# not False == True
# 应用：
#
# 对一个条件进行否定
#
# 练习：
#
# 进入网吧的条件：年龄不小于18
#
# age=9
# print('是否能进入网吧：',not age < 18)
# print('是否能进入网吧：',not age >= 18)
# 练习：获取奖学金的条件：学习成绩大于90分并且操评分不低于80分，或者操评分不低于95分并且学习成绩大于75分
#
# score1 = 90 #学习成绩
# score2 = 60 #操评分
# print('是否获得奖学金：',(score1 > 90 and score2 >= 80) or (score2 > 95 and score1 > 75))
# 4.赋值运算符： =, +=, -=, *=, /=, //=, %=, **=
# 所有的赋值运算符左边要求必须是变量，复合赋值运算符左边要求除了是变量意外，这个变量还必须赋过值。
#
# a. = : 直接将=右边的值赋给左边的变量
# #
# # num = 100
# num = 12*2
# b. +=, -=, *=, /=, //=, %=, \*\*=
# 变量 += 值 ---相当于 变量 = 变量+值
#
# 赋值过程：
#
# 将原变量中的数据取出来，和后边的值相加，然后将最新的结果重新赋给变量
#
# num2=10
# num2+=2
# print(num2)     #12
#
# num2=10
# num2*=2
# print(num2)     #20
#
# num2/=4
# print(num2)     #5.0
# 5.运算赋的优先级
# 数学运算符>比较运算赋>逻辑运算赋>赋值运算赋
# 先算优先级高的，再算优先级低的。如果有括号，先算括号里面的
#
# num =10
# num += 12*3     #先算12*3
# print(num)
# 注意：不要使用数字做逻辑运算，因为没有实际意义
#
# print(3 and 10)
# 二.数据类型
# python 中和数字相关的类型有4种： int，float，bool，complex
#
# 1. int（整型）
# 整型包含了数字数字种的所有整数，包括正整数和负整数。例如： 0 ，10，-100，+22
#
# print(10,-100,+200,0)
# 2.float(浮点型)
# 浮点型包含了数字中的所有小数：例如：0.0, 0.12,-3.14
# 支持科学计数法:2e3
#
#    print(0.0,0.13,-3.14)
#    print(2e3)   #2*10**3 =2000
#    print(2e-3)  #2*10**(-3) = 0.002
# 补充： 可以利用**来进行开方运算
#
#    print(3**2)
#    print(9**(1/2))  #9开平方
#    print(8**(1/3))  #8开立方
# 3.bool(布尔)
# 布尔只有True和False两个值；实质就是0和1，当布尔参与数字运算的是True就是1，False就是0
#
#    print(True == 1)
#    print(False == 0)
# 4.complex(复数)
# 复数是指包含实部和虚部的这种书：10+2j，19j，-10j
#
#    a=10+2j
#    b=19j
#    print(a+b)
#    print(a*b)
# 5.函数-type(): 获取数据类型
# type(数据)- 获取括号中执行的数据对应的类型
#
#    type1 = type(10+2j)
#    print(type1)
#    print(type(True))
#    num = 3e4
#    print(type(num))
# 6.函数-isinstance():判断是不是指定的类型
# isinstance(数据,类型) - 判断指定的数据是否是指定的类型，结果是布尔值
#
# result = isinstance(10,float)
#   print(result)
#   num = 3e4
#   result = isinstance(num,int)
#   print(result)
#   result = isinstance(num,float)
#   print(result)
# 7.类型转换：类型名()
# 类型名(数据) - 将指定的数据转换成指定的类型
#
#    num = 13.5
#    print(int(num))
#    print(float(100))
#    print(float(True)) #布尔转整型或者浮点型：True ->1/1.0 False ->0/0.0
#    print(bool(-10.12))  #数字转bool，除了0是False，其他非零都是True
#    price  = 100
#    new_num = float(price)
#    print(new_num)
#    price  = 123.7765
#    new_num = int(price)
#    print(new_num)
# 三.分支结构
# 分支结构：只有if语句
#
# 1.if语句
# a.语法
#
# if 条件语句 :
#    语句块
# b.说明
#
# if - 固定写法，是关键字
# 条件语句 - 可以是一个值，一个变量，一个运算表达式。不能是赋值语句
# ： - 固定写法（在python中有‘：’的地方一般都会产生缩进）
# 语句块 - 一行或者多行代码（必须和if保持一个缩进）
#
# c.执行过程：
#
# 先判断条件语句的结果是否为True（如果不是布尔值就看转换为布尔值后是否为True）
# 如果为True就执行语句块对应的代码，否者就不执行语句块对应的代码
#
# if 100:
#     print("if语句1")
#     print('if语句2')
# print('语句3')
# if 0:
#     print("if语句1")
#     print('if语句2')
# print('语句3')
# if 100 > 10:
#     print('100大于10')
# d.应用:
#
# 某个操作或者某段代码是在满足某个条件下才会执行，不满足条件就不执行。的时候就使用if条件语句
#
# 练习：
#
# 如果age的值大于等于18岁打印'成年'
#
# age = 16
# if age >=18 :
#     print('成年')
#
# 2.if - else结构
# a.语法：
#
# if 条件语句 :
#   语句块1
# else :
#   语句块2
# b.执行过程：
#
# 判断条件语句是否为True（如果不是布尔值就转换为布尔值再看是否为True），
# 如果为True就执行语句块1，否者就执行语句块2
#
# c.应用：
#
# 满足条件执行某个操作，不满足条件执行另外的操作，就使用if-else结构
#
# num = 10
# if num % 2 == 0 :
#     print('num是偶数')
# else:
#     print('num是奇数')
# if num % 2:
#     print('num是奇数')
# else:
#     print('num是偶数')
# 练习：
#
# 如果age的值大于等于18岁打印‘已成年’，否者打印‘未成年’
#
# age = 16
# if age >=18 :
#     print('已成年')
# else :
#     print('未成年')
#     print('不能进网吧、迪吧')
# age = 18
# if age >= 18:
#     print('已成年')
# else:
#     print('未成年')
# 3.if-elif-else结构
# a.语法：
#
# if 条件语句1：
#     代码块1
# elif 条件语句2：
#     代码块2
# elif 条件语句3
#     代码块3
# else：
#     代码块4
# 最终代码
# b.说明：
#
# 在if-elif-else结构中，elif可以根据情况有多高，else结构根据情况可以省略
#
# c.执行过程：
#
# 先判断条件语句1是否成立，成立执行代码块1，然后整个if语句结束
# 条件语句1不成立就判断条件语句2是否成立，成立执行代码块2，然后整个if语句结束
# 条件语句2不成立就判断条件语句3是否成立，成立执行代码块3，然后整个if语句结束
# 如果前面的所有的条件语句都不成立就执行else后面的代码块（这里是代码块4）
#
# 练习：
#
# score > 90      -->优秀
# 80<=score<=90   -->良好
# 60<=score<=79   -->及格
# sorce<60        -->不及格
# score = 55
# if score > 90:
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('不及格')
# 4.if 嵌套
# 在if、elif、else对应的语句块中，可以根据情况写一个或多个其他的if语句结构
#
# score = 100
# if score > 90:
#     if score == 100:
#         print('满分，干的漂亮')
#     print('优秀')
# elif score >= 80:
#     print('良好')
# elif score >= 60:
#     print('及格')
# else:
#     print('不及格')
# 练习:
#
# 判断一个数是否是偶数，如果是打印 偶数 否者打印奇数 ，如果这个数能被4整除打印 4的倍数
#
# num = int(input("请输入一个数字："))
# if num % 2:
#     print('奇数')
# else:
#     if num % 4 == 0:
#         print('4的倍数')
#     print('偶数')
# 补充 : str字符串
# print(100 + 34)
# print(100+'20')
# print(100>'80')
# 字符串没法直接和其他类型的数据做运算操作
# input函数不管输入的内容是什么,结果都是字符串类型
#
#
# str = input('随便输入:')
# print(type(str))
#
# #将输入的数据转换成整型数据,然后再赋值给变量
# age = int(input(' 年龄:')).
names = ['海蜇王', '火影', '死神', '犬夜叉', '妖精的尾巴', '熊出没', '一人之下']
print(names[-2])
import os

# 获取path及filename
path, filename = os.path.split('/home/patha/pathb/xxx.py')

print(path)
print(filename)

# 有的时候只想获取filename，可用"_"占位

_, filename = os.path.split('/home/patha/pathb/xxx.py')

print(filename)