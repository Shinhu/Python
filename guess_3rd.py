import random
times = 3
secret = random.randint(1,10)
print("---------------我爱鱼C工作室----------------")
#这里先给guess赋值（赋一个绝不等于secret的值）
#guess = int(temp)
guess = 0
#print()默认是打印完字符串会自动添加一个换行符，end=""参数告诉print()用空格代替换行
#恩，小甲鱼觉得富有创意的你应该会尝试用end="JJ"?
print("不妨猜一下小甲鱼现在心里想的是哪个数字：",end=" ")
while (guess != secret) and (times > 0):
        temp = input()
        guess = int(temp)
        times = times - 1 #用户每输入一次，可用机会就减1
        if guess == secret:
                print("卧槽，你是小甲鱼心里的蛔虫吗？！")
                print("哼，猜中也没有奖励哦")
        else:
                if guess > secret:
                        print("哥，大了大了~~~~~")
                else:
                        print("嘿，小了小了")
                if times > 0:
                        print("再试一次吧：",end=" ")
                else:
                        print("机会用光咯")
print("游戏结束啦，不玩了")
