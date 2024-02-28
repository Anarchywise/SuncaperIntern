"""'
字典（Dictionary）是一种无序的、可变的数据类型，用于存储键值对。每个键（key）必须是唯一的，
而值（value）则可以是任何数据类型，包括数字、字符串、列表、甚至是其他字典。字典使用花括号
{} 来定义，每个键值对之间用冒号 : 分隔。
"""

# 创建字典
my_dict = {"key1": "value1", "key2": "value2"}

# 访问字典元素
value = my_dict["key1"]
print(value)

# 修改和添加元素
my_dict["key1"] = "new_value1"
my_dict["key3"] = "value3"

# 删除元素
del my_dict["key2"]
value = my_dict.pop("key1")
print(value)

# 遍历字典
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")

# 检查键是否存在
if "key1" in my_dict:
    print("Key exists in the dictionary.")

# 字典长度
length = len(my_dict)
print(length)

# 字典的复制
copy_dict = my_dict.copy()

# 深拷贝需要导入 copy 模块
import copy

deep_copy_dict = copy.deepcopy(my_dict)
