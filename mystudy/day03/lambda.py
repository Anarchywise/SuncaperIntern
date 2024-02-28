# Lambda表达式基本语法
from ast import Expression


lambda_function = lambda arguments: Expression

# Lambda表达式示例
add = lambda x, y: x + y
print(add(3, 5))  # 输出: 8

# Lambda表达式与高阶函数结合使用
numbers = [1, 2, 3, 4, 5]

# 使用map()对列表中的每个元素进行平方操作
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]

# 使用filter()筛选列表中的偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4]

# 使用sorted()按照元素的平方值进行排序
sorted_numbers = sorted(numbers, key=lambda x: x**2)
print(sorted_numbers)  # 输出: [1, 2, 3, 4, 5]

# Lambda表达式支持默认参数
power = lambda x, n=2: x**n
print(power(3))  # 输出: 9
print(power(3, 3))  # 输出: 27

# Lambda表达式也可以用于创建立即调用的匿名函数
result = (lambda x: x * 2)(5)
print(result)  # 输出: 10
