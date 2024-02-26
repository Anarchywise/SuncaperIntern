# 创建一个列表
my_list = [1, 2, 3, 4, 5]

# 列表长度
length = len(my_list)
print(length)

# 列表索引访问
first_element = my_list[0]
last_element = my_list[-1]
print(first_element)
print(last_element)

# 列表切片
subset = my_list[1:4]  # 从索引1到索引4（不包括4）
print(subset)

# 添加元素到列表末尾
my_list.append(6)
print(my_list)

# 插入元素到指定位置
my_list.insert(2, "dhuw")  # 在索引2处插入元素7
print(my_list)

# 移除列表中的元素
my_list.remove(3)  # 移除元素3
print(my_list)

# 弹出（删除并返回）指定索引处的元素
popped_element = my_list.pop(1)  # 弹出索引1的元素
print(popped_element)
print(my_list)

# 列表合并
another_list = [8, 9, 10]
merged_list = my_list + another_list
print(merged_list)

# 列表重复
duplicated_list = my_list * 2
print(duplicated_list)

# 列表是否包含某个元素
contains_5 = 5 in my_list
print(contains_5)

# 列表排序
my_list.sort()  # 默认升序排序
print(my_list)

# 列表反向排序
my_list.reverse()
print(my_list)

# 列表清空
my_list.clear()
print(my_list)
