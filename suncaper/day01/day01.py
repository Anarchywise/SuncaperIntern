# 这是一个输出语句
print("123")
import_val = 1
print(import_val)
# result = input('请输入账号:')
#
# password = input('请输入密码:')
#
# print('账号:',result,'密码:',password)
"""
note1
"""

"""
note2
"""
import datetime

# 获取当前日期
current_date = datetime.date.today()

# 打印年、月、日
print(current_date)

str = "abcdef"
str = "012345"

str1 = "python"  # 'p' : 0/-6  'y' : 1/-5
result = "python"[3]
print(result)  ## >>h
print(str1[0], str1[-6], str1[-1], str1[4])
# print(str1[100])#IndexError: string index out of range

str2 = "abcdefg123456"
print(str2[0:4:1])
# print(str2[0:4:-1]) #下标错误取到的是空串
print(str2[4:0:-1])
print(str2[-2:-3:-1])
print(str2[0:1000:1])  # 下标可以越界.'abcdefg123456'
print("hello python"[1:-2:3])  #'eoy'
print("#############")

str2 = "abcdefg123456"
print(str2[:3:1])  # abc
print(str2[:3:-1])  # 654321gfe

print(str2[2:])  # cdefg123456
print(str2[2::-1])  # cba
print(str2[::-1])  # 倒叙

# 1234 - 4321
num = 1234
# num = int (str(num)[::-1])
print(num)
print(len(str2))
print("--------------")
numbers1 = [1, 20, 100, 200]
num = int(input("请输入数字:"))
for index in range(len(numbers1)):
    if numbers1[index] >= num:
        numbers1.insert(index, num)
        break
else:
    numbers1.append(num)
print(numbers1)
dict1 = {"a": 100, "b": "abc", "c": [1, 2]}

for x in dict1:
    print(x, dict1[x])

for i in range(1, 10):
    for ii in range(1, 10):
        print(f"{ii}*{i}={i*ii} ", end="")
    print()
