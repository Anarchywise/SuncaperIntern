'''
集合（Set）是一种无序且不重复的数据结构，用于存储多个唯一的元素。
集合是由花括号 {} 括起来的一组元素，每个元素之间用逗号分隔。
集合提供了一些非常有用的操作，使得处理唯一值的需求更加方便。
'''
# 创建集合
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 集合并集
union_set = set1.union(set2)
print(union_set)  # 输出: {1, 2, 3, 4, 5}

# 集合交集
intersection_set = set1.intersection(set2)
print(intersection_set)  # 输出: {3}

# 集合差集
difference_set = set1.difference(set2)
print(difference_set)  # 输出: {1, 2}

# 集合对称差集
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # 输出: {1, 2, 4, 5}

# 添加元素到集合
set1.add(4)
print(set1)  # 输出: {1, 2, 3, 4}

# 移除元素
set1.remove(2)
print(set1)  # 输出: {1, 3, 4}

# 判断元素是否在集合中
contains_3 = 3 in set1
print(contains_3)  # 输出: True

# 集合长度
length = len(set1)
print(length)  # 输出: 3

# 清空集合
set1.clear()
print(set1)  # 输出: set()

# 集合的迭代
for element in set2:
    print(element)

# 判断是否是子集或超集
subset_check = {1, 3}.issubset(set2)
print(subset_check)  # 输出: True

superset_check = set2.issuperset({1, 3})
print(superset_check)  # 输出: True
