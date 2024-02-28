"""
1、创建一个文本文件test.txt 并添加任意多行内容，实现功能：读取test.txt并生成文件newtest.txt ，
其中的内容与test.txt一致 ，但是在每行的首部添加当前行号，行尾添加当前行内容长度；
2、a.声明一个人的类和一个狗的类:
狗的属性:名字、颜⾊、年龄
狗的方法:叫唤
人的属性:名字、年龄、狗
人的方法:遛狗
b.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄
3、创建一个学生类:
属性:姓名，年龄，学号
方法:答到（self.name + ' 到'），打印学生信息
创建一个班级类:
属性:学生，班级名
方法:添加学生，删除学生，点名, 计算班上学生的平均年龄
4、 定义一个函数，要用到异常捕获 输入年龄并且将年龄值转换为整数,范围是1-100，
要使输入错误程序不能崩溃让其重新输入,直到输入无误为止
"""

import os

now_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(now_directory)


def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def append_to_file(file_path, content):
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content)
            print(f"Content successfully appended to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def change_file(file_path):
    try:
        # 读取 test.txt 中的内容，生成 newtest.txt
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # 处理每一行内容，添加行号和长度信息
        processed_lines = []
        for i, line in enumerate(lines, 1):
            line = f"{i}: {line} Length: {len(line)}"
            processed_lines.append(line)

        # 将处理后的内容写入 newtest.txt
        with open("new" + file_path, "w", encoding="utf-8") as new_file:
            new_file.write("\n".join(processed_lines))
    except Exception as e:
        print(e)


# 写入文件
new_content = "This is a new content for the file.\n"
write_file("test.txt", new_content)
append_to_file("test.txt", new_content)
append_to_file("test.txt", new_content)
append_to_file("test.txt", new_content)
append_to_file("test.txt", new_content)
append_to_file("test.txt", new_content)
change_file("test.txt")
###############################################################################################
# a. 声明一个人的类和一个狗的类


class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        return "Woof! Woof!"


class Person:
    def __init__(self, name, age, dog=None):
        self.name = name
        self.age = age
        self.dog = dog

    def walk_dog(self):
        if self.dog:
            return f"{self.name} is walking {self.dog.name}."
        else:
            return f"{self.name} doesn't have a dog to walk."


# b. 创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄

# 创建狗对象
dog_yellow = Dog(name="大黄", color="yellow", age=3)

# 创建人对象
xiaoming = Person(name="小明", age=25, dog=dog_yellow)

# 让小明遛大黄
result = xiaoming.walk_dog()
print(result)


#############################################################################################
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def answer(self):
        return self.name + " 到"

    def print_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}")


class Classroom:
    def __init__(self, class_name):
        self.students = []
        self.class_name = class_name

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def roll_call(self):
        for student in self.students:
            print(student.answer())

    def average_age(self):
        if not self.students:
            return 0
        total_age = sum(student.age for student in self.students)
        return total_age / len(self.students)


# 创建学生和班级对象
student1 = Student("张三", 18, "S001")
student2 = Student("李四", 19, "S002")
student3 = Student("麻子", 20, "S003")
classroom = Classroom("ClassA")
# 添加学生到班级
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
# 打印学生信息
for student in classroom.students:
    student.print_info()
# 点名
classroom.roll_call()
# 计算平均年龄
avg_age = classroom.average_age()
print(f"班上学生的平均年龄: {avg_age}")


######################################################################################
def get_valid_age():
    while True:
        try:
            age = int(input("请输入年龄（1-100）: "))
            if 1 <= age <= 100:
                return age
            else:
                print("年龄超出范围，请重新输入。")
        except ValueError:
            print("输入无效，请输入一个整数。")


age = get_valid_age()
print(f"有效年龄: {age}")
