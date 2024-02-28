# 装饰器基本概念
# 装饰器是一种Python语法，用于动态修改函数或类的功能。
# 装饰器本质上是一个函数，它可以接受一个函数作为参数，并返回一个新的函数。
# 有点像AOP增强
# 简单的装饰器示例
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# 使用装饰器修饰函数
@my_decorator
def say_hello():
    print("Hello!")


say_hello()  # 输出:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# 装饰器的语法糖 @ 符号可以简化装饰器的使用，相当于 say_hello = my_decorator(say_hello)。


# 带参数的装饰器示例
def my_decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # *args 是一个元组，包含传递给 wrapper 函数的所有位置参数
            # **kwargs 是一个字典，包含传递给 wrapper 函数的所有关键字参数
            print(f"Something is happening before {arg} is called.")
            func(*args, **kwargs)
            print(f"Something is happening after {arg} is called.")

        return wrapper

    return decorator


# 使用带参数的装饰器修饰函数
@my_decorator_with_args("the function")
def say_hello_with_args(name):
    print(f"Hello, {name}!")


say_hello_with_args("Alice")  # 输出:
# Something is happening before the function is called.
# Hello, Alice!
# Something is happening after the function is called.

# 常见用途
# 1. 日志记录
# 2. 性能测试
# 3. 授权检查
# 4. 缓存


# 类装饰器示例
class MyDecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")


@MyDecoratorClass
def say_hi():
    print("Hi!")


say_hi()  # 输出:
# Something is happening before the function is called.
# Hi!
# Something is happening after the function is called.


"""
位置参数：

    位置参数是指在函数调用时，按照函数定义时的顺序传递的参数。
    这些参数的值是根据它们在函数调用中的位置来确定的。
    例如：

    python

    def add(a, b):
        return a + b

    result = add(3, 5)

    在这个例子中，3 和 5 就是位置参数，它们分别传递给了函数 add 的参数 a 和 b。

关键字参数：

    关键字参数是通过键值对的形式传递给函数的参数，可以在函数调用中指定参数的名字。
    通过使用关键字参数，你可以不必按照函数定义的顺序传递参数。
    例如：

    python

        def greet(name, age):
            print(f"Hello, {name}! You are {age} years old.")

        greet(name="Alice", age=25)

        在这个例子中，name="Alice" 和 age=25 就是关键字参数，它们显式地指定了参数的名字。

在函数定义中，可以同时使用位置参数和关键字参数。位置参数必须在关键字参数之前，
而且在函数调用时，位置参数必须按照函数定义的顺序传递，而关键字参数可以按照任意顺序传递。例如：

python

def example_func(a, b, c, d=0, e=1):
    print(a, b, c, d, e)

example_func(1, 2, 3, e=5, d=4)

在这个例子中，a、b、c 是位置参数，d、e 是关键字参数。函数调用时，1、2、3 是按照位置传递的位置参数，而 e=5 和 d=4 是关键字参数。
"""
