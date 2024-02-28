import copy

# 1. 复制列表
original_list = [1, 2, 3, 4, 5]
shallow_copy_list = original_list.copy()  # 浅拷贝
deep_copy_list = copy.deepcopy(original_list)  # 深拷贝

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy_list)
print("Deep Copy:", deep_copy_list)

# 修改原始列表
original_list[0] = 100

print("\nAfter modifying the original list:")
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy_list)
print("Deep Copy:", deep_copy_list)

# 2. 复制字典
original_dict = {"a": 1, "b": 2, "c": 3}
shallow_copy_dict = original_dict.copy()  # 浅拷贝
deep_copy_dict = copy.deepcopy(original_dict)  # 深拷贝

print("\nOriginal Dictionary:", original_dict)
print("Shallow Copy:", shallow_copy_dict)
print("Deep Copy:", deep_copy_dict)

# 修改原始字典
original_dict["a"] = 100

print("\nAfter modifying the original dictionary:")
print("Original Dictionary:", original_dict)
print("Shallow Copy:", shallow_copy_dict)
print("Deep Copy:", deep_copy_dict)

# 3. 复制字符串
original_string = "Hello, World!"
shallow_copy_string = original_string  # 字符串是不可变对象，直接赋值即为浅拷贝

print("\nOriginal String:", original_string)
print("Shallow Copy String:", shallow_copy_string)

# 修改原始字符串
# 字符串是不可变对象，修改会创建一个新的字符串
original_string = original_string + " How are you?"

print("\nAfter modifying the original string:")
print("Original String:", original_string)
print("Shallow Copy String:", shallow_copy_string)
