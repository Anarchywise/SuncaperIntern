"""
在Python中，* 是一个解包运算符（unpacking operator），
用于解包可迭代对象（如列表、元组、集合等）。在函数调用时，
* 可以用来将可迭代对象中的元素拆分开，并作为独立的参数传递给函数。
在你提供的代码中，*numbers 就是将列表 numbers 中的元素解包成独立的参数，
然后传递给 print_vargs 函数。因此，print_vargs(*numbers) 
就相当于 print_vargs('hello', 'again')，这样就会将 'hello' 和 'again' 作为两个独立的参数传递给 print_vargs 函数。
"""


def print_vargs(*args):
    print(args)


numbers = ["hello", "again"]
print_vargs(numbers)


def log_console(message, **kwargs):
    print(message, kwargs)


log_console("RuntimeException: xxxx", level="Error", server="192.168.3.1")

# 参数List


def print_list(list):
    print(list)


print_list(["a", "b"])


# 防止修改list


def print_list(list):
    list[0] = "c"
    print(list)


list = ["a", "b"]
print_list(list)
print(list)


def print_list(list):
    list[0] = "c"
    print(list)


# 将list的copy传入
list = ["a", "b"]
print_list(list[:])
print(list)
