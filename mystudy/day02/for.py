# coding: utf-8

# for 循环
print("for 循环:")
for i in range(5):
    print(i)

# while 循环
print("\nwhile 循环:")
count = 0
while count < 5:
    print(count)
    count += 1

# break 语句
print("\nbreak 语句:")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue 语句
print("\ncontinue 语句:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass 语句
print("\npass 语句:")
for i in range(3):
    if i == 1:
        pass
    else:
        print(i)

# for-else 语句
print("\nfor-else 语句:")
for i in range(3):
    if i == 1:
        break
else:
    print("循环正常结束")

# range() 函数
print("\nrange() 函数:")
for i in range(2, 7, 2):
    print(i)

# enumerate() 函数
print("\nenumerate() 函数:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
