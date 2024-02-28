# 生成器基本概念
# 生成器是一种迭代器，可以按需生成值，而不是一次性生成所有值，从而节省内存空间。

# 创建生成器的方式：使用生成器表达式或定义带有 yield 关键字的函数。

# 生成器表达式示例
generator_expr = (x * 2 for x in range(5))
print(list(generator_expr))  # 输出: [0, 2, 4, 6, 8]


# 生成器函数示例
def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()
print(list(gen))  # 输出: [1, 2, 3]

# 生成器的惰性计算
# 生成器的值是按需生成的，只有在需要时才计算下一个值。
# 这种方式可以有效地处理大量数据，而无需一次性将所有数据加载到内存中。


# 无限序列生成器示例
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# 使用生成器遍历无限序列
gen_inf = infinite_sequence()
for i in range(5):
    print(next(gen_inf))  # 输出: 0, 1, 2, 3, 4


# 使用生成器实现惰性求和
def lazy_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total


numbers = [1, 2, 3, 4, 5]
sum_gen = lazy_sum(numbers)
print(list(sum_gen))  # 输出: [1, 3, 6, 10, 15]


# 使用生成器优化斐波那契数列计算
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci_generator(10)
print(list(fibonacci_gen))  # 输出: [0, 1, 1, 2, 3, 5, 8, 13]
