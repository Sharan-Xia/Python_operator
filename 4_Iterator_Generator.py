import sys
#迭代器：迭代器是一个可以记住遍历位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完而结束。
# 迭代器只能往前不能后退。迭代器两个基本方法：iter（）和next（）
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))

for x in it:
    print(x, end=' ')

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


#生成器：在Python中使用了yield的函数被称之为生成器。
#生成器是一个返回迭代器的函数，只能用于迭代操作，（生成器就是一个迭代器）。
#在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下次执行next（）方法
#时从当前位置继续运行。

def fibonacci(n):   # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)   # f 是一个迭代器，有生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
