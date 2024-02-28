for num in range(10):
    print(num)
for num in range(0, 10):
    print(num)
for num in range(0, 10, 2):
    print(num)
for x in range(10):
    if x % 3 == 0:
        continue
    print(x)
    print("======")


def yt_sum1(*num):
    print(num)
    print(type(num))


yt_sum1(1, 2)  # (1, )
