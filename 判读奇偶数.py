temp = input("请输入一个数：")

while not temp.isdigit():
    temp = input("抱歉，您的输入有误，请输入一个整数：")

num = int(temp)
if num%2 == 0:
    print(temp + '是偶数')
else:
    print(temp + '是奇数')
