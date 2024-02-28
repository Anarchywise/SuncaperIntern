# 高阶函数
# 把函数当成变量来用，一个函数接收另外一个函数作为参数，这样的函数叫做高阶函数（Higher-order Functions）
def func(f, arr):
    return [f(x) for x in arr]


def square(x):
    return x * x


print(func(square, [1, 3, 5, 9]))


def square(x):
    return x * x


# 高阶函数 - map
# 对于每个值，map将其从一个值map成另外一个值
# map 是惰性函数， 需使用list()来使其打印
results = list(map(square, [1, 3, 5, 9]))

print(results)


# 使用内置的str函数
def square(x):
    return x * x


results = list(map(str, [1, 3, 5, 9]))

print(results)


def square(x):
    return x * x


def double(x):
    return x + x


funcs = [square, double]
results = list(map(lambda f: f(10), funcs))
print(results)

# Reducer 示例

# 假设有一组键值对表示单词计数，我们希望将相同键的值相加以得到总计数。

# 初始数据
word_counts = [
    ("apple", 1),
    ("orange", 3),
    ("apple", 2),
    ("banana", 1),
    ("orange", 2),
]


# 使用 Reducer 聚合数据
def reducer(data):
    result = {}  # 集合
    for key, value in data:
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# 执行 Reducer
result = reducer(word_counts)

# 输出结果
print(result)
# 输出:
# {'apple': 3, 'orange': 5, 'banana': 1}

# 上述示例中，我们使用 Reducer 将相同键的值相加，得到每个键的总计数。
# 在实际应用中，Reducer 可以用于处理大规模分布式计算任务，如 MapReduce 框架中的 Reducer 阶段。

# 实际应用中，可能需要对键值对进行排序、过滤等操作，这取决于具体的需求。


from functools import reduce

# 高阶函数 - reducer
# reduce(f, itr)  reducer 先将itr（迭代器）里面的前两个值传递给函数f，
# 计算出结果，然后再同第三个值通过f计算出结果。一直迭代，直到没有其他值为止。

# 相当于 ((1* 2) * 3) * 4 = 24
results = reduce(lambda x, y: x * y, [1, 2, 3, 4])

print(results)

from functools import reduce

# 相当于 max(max(max(3, 4), 9), 4)
result = reduce(lambda a, b: max(a, b), [3, 4, 9, 4])
print(result)
