import random

# if语句
'''
Python中if语句的一般形式如下所示：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
'''
# '''
# age = int(input("请输入你家狗狗的年龄："))
# print('')
# if age < 0:
#     print("你是在逗我吧！")
# elif age == 1:
#     print("相当于14岁的人。")
# elif age == 2:
#     print("相当于22岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
# # 退出提示
# input('点击enter键退出')
# '''


# 数字猜谜游戏
number = 7
guess = -1
print('数字猜谜游戏！')
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


x = random.choice(range(100))   #0~99
y = random.choice(range(200))


print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print(" ")
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2)*5
            print("相当于人类：",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
input("点击 enter 键退出")