# 字符串连接
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2  # 使用 + 运算符
print(result)

words = ["Hello", "World","!!"]
result = ",.".join(words)  # 使用 join 方法
print(result)

# 字符串长度
my_string = "Python"
length = len(my_string)
print(length)

# 字符串查找和替换
sentence = "Python is easy to learn. Python is powerful."
index = sentence.find("Python")  # 查找第一个匹配的索引
print(sentence[index])
print(index)

new_sentence = sentence.replace("Python", "Java")  # 替换所有匹配项
print(new_sentence)

# 大小写转换
my_string = "Hello, woRld!"
lower_case = my_string.lower()
upper_case = my_string.upper()
title_case = my_string.title()

print(lower_case)
print(upper_case)
print(title_case)

# 字符串切片

# 获取字符串的一部分
substring = my_string[7:12]  # 从索引7开始（包括7），到索引12结束（不包括12）
print(substring)  # 输出: World

# 也可以不指定开始或结束索引，从开头或到末尾
substring_start = my_string[:5]  # 从开头到索引5结束（不包括5）
substring_end = my_string[7:]    # 从索引7开始（包括7）到末尾
print(substring_start)  # 输出: Hello
print(substring_end)    # 输出: World!

# 使用负数索引从字符串末尾开始计数
last_three_chars = my_string[-3:]  # 获取最后三个字符 
print(last_three_chars)  # 输出: ld!

# 使用步长
every_second_char = my_string[::2]  # 从开头到末尾，每隔一个字符取一个
print(every_second_char)  # 输出: Hlo o!

# 反向获取字符串  使用步长来实现的
reverse_string = my_string[::-2] 
print(reverse_string)  # 输出: !dlroW ,olleH

# 字符串分割
my_string = "apple,orange,banana"
fruits = my_string.split(",")
print(fruits)

# 去除空白字符
my_string = "   Python   "
trimmed_string = my_string.strip()
print(trimmed_string)

# 字符串格式化
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old."  # 使用 f-strings
print(message)

# 字符串比较
str1 = "hello"
str2 = "world"
result = (str1 == str2)
print(result)

# 字符串是否包含子串
sentence = "Python is a powerful programming language."
contains_python = "Python" in sentence
print(contains_python)

# 字符串转换为列表和反之
my_string = "hello"
my_list = list(my_string)
print(my_list)

new_string = "".join(my_list)
print(new_string)

# 字符串是否以特定前缀或后缀开始或结束
file_name = "example.txt"
is_txt_file = file_name.endswith(".txt")
print(is_txt_file)

# 字符串转换为大写或小写
my_string = "Hello World"
upper_case = my_string.upper()
lower_case = my_string.lower()
print(upper_case)
print(lower_case)

# 字符串的字符替换
translation_table = str.maketrans("aeiou", "12345")
my_string = "hello world"
translated_string = my_string.translate(translation_table)
print(translated_string)
