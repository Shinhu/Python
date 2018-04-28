while guess != 8:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
   if guess == 8:
        print("哎呀，你是小甲鱼肚里的蛔虫吗！")
        print("猜对了也没有奖励")
    else:
        if guess > 8:
            print("哥，大了大了。。。")
        else:
           print("嘿，小了小了。。。")
