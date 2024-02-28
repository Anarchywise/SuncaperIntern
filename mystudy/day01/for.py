# 创建一个列表
my_list = [1, 2, 3, 4, 5]

# 使用 for 循环遍历列表
for element in my_list:
    print(element)

# 使用 enumerate 获取元素索引
for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")

# 使用 range 和 len 遍历列表索引
for index in range(len(my_list)):
    print(my_list[index])

# 使用 while 循环和索引遍历列表
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# 使用 zip 遍历多个列表
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for item1, item2 in zip(list1, list2):
    print(f"List1: {item1}, List2: {item2}")

# 遍历字典的键和值
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 使用列表推导式进行遍历和筛选
even_numbers = [x for x in my_list if x % 2 == 0]
print(even_numbers)
