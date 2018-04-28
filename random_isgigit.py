# 针对小甲鱼提到的小漏洞，再次改进游戏：当用户输入错误类型的时候，提醒用户重新输入，避免程序崩溃。
import random
times = 3
secret = random.randint(1,10)
print('-------------我爱鱼C工作室--------------')
guess = 0
print("不妨猜猜小甲鱼现在心里想的是哪个数字：",end = '')

while (guess != secret) and (times > 0):
    temp = input()
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:  
            print("我操，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜对了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~~~")
            else:
                print("嘿，小了小了~~~~")
            if times > 1:
                print("再试一次吧：",end = '')
            else:
                print("机会用光咯")
    else:
        print("抱歉，您输入的有误，请输入一个整数：",end = '')
    times = times - 1 #用户每输入一次，可用机会就-1
print("游戏结束，不玩啦！")
