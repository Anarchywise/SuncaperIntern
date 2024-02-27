文件操作
备注： os库提供了很多文件管理和操作
1 数据本地化和数据持久化
通过文件将数据存到硬盘中
数据库文件，txt、json、plist、xml、png、mp4
2 文件操作 - 文件内容操作
基本步骤： 打开文件 -- 操作文件（读/写） -- 关闭文件
open(file, mode ,encoding=None) ，以指定方式打开指定文件，并且返回被打开的文件对象
file -- 字符串 需要打开的文件的路径
        ./  -- 当前文件所在目录（./ 可以省略）
        ../ -- 当前文件所在目录的上层目录
mode -- 字符串 打开方式
        r -- 默认值，以读的方式打开文件（只能进行读操作）
        w -- 以写的方式打开文件（只能进行写的操作），覆盖
        a -- 以写的方式打开文件（只能进行写的操作），追加
        rb/br -- 以读的方式打开文件，读出来的内容是二进制数据
        wb/bw -- 以写的方式打开文件（只能进行写操作），将2进制数据写入文件
        + -- 以读写的方式打开（了解）

encoding -- 文本编码方式
        utf-8
        注意：文本编码只针对文件，二进制文件不能设置编码方式
2.1 文件读操作
···
文件对象.read() -- 从读写位置开始，读到文件结尾，并返回
（读写位置默认在文件开通）
文件对象.seek(字节数) -- 将读写位置移动到指定的地方

···

注意：打开文件的时候，如果以读的方式打开一个不存在的文件，会出现异常，会出现异常，报错
如果以写的方式打开一个不存在的文件，不会出现异常，并且会自动创建对应的文件再打开
def test_r():
    file = open('test.txt','r',encoding='utf-8')
    str1 = 'start'
    print(file.readlines())
    # while str1:
    #     str1 =file.readline()
    #     print(str1,end = '')

2.2 文件写操作
文件对象.write(写的内容）  - 将指定内容写入到指定文件中，返回被写入的内容的长度
def test_w():
    file = open('test.txt','w+',encoding='utf-8')
    file.write('柯基二哈，嗷嗷哦啊哦嗷嗷')
    file.seek(0)
    print(file.read())
    file.close() #关闭文件
3 二进制文件操作
rb -- 读的时候获取到的是二进制数据（bytes）
wb -- 写的时候希尔的内容要求类型是二进制
普通的文本文件可以通过二进制的形式打开，影响只是获取到的内容，和写进去的内容的数据类型
二进制文件只能以二进制的形式打开
3.1二进制数据
一般二进制数据都是通过网络请求获取道，或者通过读取本地的二进制文件来获取
1）将字符串转换二进制
bytes(str,encoding="utf-8")
str.encode(编码方式)
f1= open('test1.txt','wb+')
f1.write(bytes('阿米托福',encoding='utf-8'))
将二进制转换成字符串
str(二进制数据，编码方式）
二进制.decode('编码方式’）
4. 文件上下文
with open(文件路径，打开方式，编码方式） as 文件对象
    操作文件
文件操作完成后，会自动关闭   
with open('test1.txt','rb+') as f:
    print(f.read())
二. json
1. json数据
1.1 满足json格式的数据叫json数据
1.2 json格式：
一个json有且只有一个数据，这个数据必须是满足是json支持的数据类型

1.3 json 支持的数据类型：
数子（number） - 包含所有的数字（整数和小数）,支持科学计数法，例如：100，3.12
字符串（string）-用双引号括起来的字符串，字符也可以是转义字符和
编码字符例如："abc"，"\n", "\u4e01"
布尔（bool） true/false
数组（array） - 相当于Python中的列表，[100,200,"abx" ,[1,2,3]]
json对象/字典（dictionary） - 相当于Python中的字典
空值 - null ， 相当于None
2 使用json
解析json数据（获取到json数据后将json中想要的数据解析出来） -- 做前端开发人员的工作
在Python中有一个内置库，专门负责json数据处理，json库
2.1.将json数据转换为Python数据
json数据          Python数据
数字number        int/float
string            str，可能会出现将”变成'
bool              bool true->True false ->False  
array             list/set
dictionary        dict
null              None
import json

# ===================1.json转Python（json数据解析）
# json.loads(str,encoding='utf-8')  -- 解析json数据，返回json对应的Python数据
#  --字符串中的内容本身就是一个json数据（去掉引号后，本身就是就是一个接送数据）

# result = json.loads('"abc"',encoding='utf-8')
# print(result,type(result))
# result = json.loads('100.12',encoding='utf-8')
# print(result,type(result))
# result = json.loads('true',encoding='utf-8')
# print(result,type(result))
# result = json.loads('[10,23,"yuting",true]',encoding='utf-8')
# print(result,type(result))
# result = json.loads('{"a":100,"b":flase}',encoding='utf-8')
# print(result,type(result))

with open('33.json','r',encoding='utf-8') as f:
    test = json.loads(f.read(),encoding='utf-8')
# print(type(test))
2.2 python转json
Python数据        json数据
int/float          number 
bool            True - true.False->false
str             string,将单引号变成双引号
list、tuple      array
dict            dictionary
空值             None ->null
json.dumps(python数据) --》将Python数据转换成内容是对应的json数据的字符串
result = json.dumps([12,'abc',[1,2],True,('a',12,4)])
print(type(result),result)
3.json文件操作
json.load(文件对象） - 将文件对象中的文件的内容转换成Python数据
                    文件的内容只是json数据
with open('33.json','r',encoding='utf-8') as f:
    result = json.load(f)

json.dump(python数据，文件对象） - 将文件对象中的文件的内容转换成json数据
                    
with open('44.json','r',encoding='utf-8') as f:
    json.dump('abcd',f)
练习：找json文件中favourite最高的条目

with open('33.json','r',encoding='utf-8') as f:
    test = json.loads(f.read(),encoding='utf-8')
dict1 = test["data"]
dict2 = max(dict1,key= lambda x: int(x['favourite']))
print(dict2['name'], dict2['favourite'])