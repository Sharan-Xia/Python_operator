#while循环
n = 100
sum = 0
counter = 1
while counter <= n: #当条件为永远不为false时，无限循环
    sum = sum + counter
    counter += 1

print('1到%d之和：%d' % (n, sum))

#while循环使用else语句：在while...else当条件语句为false时执行else的语句块
count = 0
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")

print('\n')
#for语句：for循环可以遍历任何序列的项目，如一个列表或者一个字符串
languages = ['C', 'C++', 'Perl', 'Python']
for x in languages:
    print(x)

print('\n')
#for循环中使用break语句，break语句用于跳出当前循环体
sites = ["baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程！")
        break   #跳出当前循环
    print("循环数据:" + site)
else:
    print("没有循环数据！")
print("完成循环！")

print('\n')
#range（）函数
for i in range(5):  #0~5 不包括5
    print(i)

for i in range(0, 10, 3):   #0~10 步长为3，0、3、6、9
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
     print(i, a[i])

print(list(range(5)))
print('\n')


#break和continue语句及循环中的else子句:
#break语句可以跳出for和while的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for letter in "Runoob":
    if letter == 'b':
        break
    print('当前字母为：', letter)

var = 10
while var > 0:
    print('当前变量值为：', var)
    var = var - 1
    if var == 5:
        break
print("Goodbye!")

#continue语句被用来告诉Python跳出当前循环块中剩余的语句，继续下一轮循环
for letter in 'Runoob':
    if letter == 'o':
        continue
    print("当前字母：", letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值：', var)
print('GoodBye')
#循环语句可以有else子句，他在穷尽列表或条件变为false导致循环终止时执行，但循环被break终止时不执行
for n in range(2, 10):
    for x in range (2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
        else:
            print(n, '是质数') #循环中没有找到
print('\n')

#使用内置enumerate函数进行遍历：下标和元素同时显示
sequence = [12, 34, 34, 45, 23, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)
