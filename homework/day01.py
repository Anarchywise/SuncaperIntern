import random
options = ["石头","剪刀","布"]
#猜拳游戏
print("猜拳游戏")
isright = True
while isright:
    try:
        player_operation = int(input("请输入你的操作 0 - 石头 1 - 剪刀 2 - 布\n"))
        if(player_operation==0 or player_operation==1 or player_operation==2): 
            isright = False
        else:
            print('输入错误')
    except ValueError:
        print('输入错误')

computer = random.choice(options) 
pc_operation = options.index(computer) #0121
print("你的出拳是:"+options[player_operation]+",电脑的出拳是:"+options[pc_operation])
if(pc_operation==player_operation):
    print('平局')
elif(player_operation-pc_operation==-1 or player_operation-pc_operation== 2):
    print('你赢了')
else:
    print('你输了')

# 99乘法表
for i in range(1,10):
    for ii in range(1,10):
        if(ii<=i):
            print(f'{ii}*{i}={i*ii} ',end='')
    print()

