# 创建一个元组
my_tuple = (1, 2, 3, 4, 5)

# 元组索引访问
first_element = my_tuple[0]
last_element = my_tuple[-1]
print(first_element)
print(last_element)

# 元组切片
subset = my_tuple[1:4]  # 从索引1到索引4（不包括4）
print(subset)

# 使用 for 循环遍历元组
for element in my_tuple:
    print(element)

# 使用 enumerate 获取元素索引
for index, element in enumerate(my_tuple):
    print(f"Index: {index}, Element: {element}")

# 使用 len 获取元组长度
length = len(my_tuple)
print(length)

# 元组合并
another_tuple = (6, 7, 8)
merged_tuple = my_tuple + another_tuple
print(merged_tuple)

# 元组重复
duplicated_tuple = my_tuple * 2
print(duplicated_tuple)

# 元组是否包含某个元素
contains_5 = 5 in my_tuple
print(contains_5)

# 元组转换为列表
tuple_to_list = list(my_tuple)
print(tuple_to_list)

# 元组解包
a, b, c, d, e = my_tuple
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

# 使用 zip 合并多个元组
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
combined_tuple = tuple(zip(tuple1, tuple2))
print(combined_tuple)
