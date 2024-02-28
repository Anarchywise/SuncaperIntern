# 返回多个值
# Python 只能返回一个值，可通过返回tuple来实现多个值返回


def return_multi():
    return 3, 4


print(return_multi())


# 返回Hint
# 尽管你在函数定义中声明了返回类型为布尔值，
# 但Python解释器并不会强制检查返回值的类型是否与声明一致。
# 因此，虽然声明是 -> bool，但实际上函数返回了整数值。
# 这种情况下，Python并不会报错，而是会执行并返回实际的结果。
def func_sum(a, b) -> bool:
    return a + b


print(func_sum(1, 2))
