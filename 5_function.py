# 函数：函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
def area(width, height):
    return  width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Sharan")
w = 4
h = 5
print(area(w, h))

#参数传递：传递不可变对象和传递可变对象。
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
'''
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
'''
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)    #结果是2

def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return

mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值：", mylist)

#参数：必须参数、关键字参数、默认参数、不定长参数
# 必须参数须以正确的顺序传入函数。调用时的数量和声明时的一样

#关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。关键字参数允许函数调用时的
#顺序与声明时不一致，Python解释器能够用参数名匹配参数值。
def printInfo(name, age):
    print("名字：", name)
    print("年龄：", age)
    return

printInfo(age=50, name="sharan")

#默认参数：调用函数时，如果没有传递参数，则会使用默认参数。
def printInfo1(name, age = 35):
    print("名字：", name)
    print("年龄：", age)
    return

printInfo1(name="sharan")
print('\n')

#不定长参数：如果需要一个函数能处理比当初声明时更多的参数。加了*号的变量名会存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数。它就是一个空元组，也可以不想函数传递未命名的变量
def printInfo2(arg1, *vartuple):
    print("输出：", arg1)
    for var in vartuple:
        print(var)
    return

printInfo2(10)
printInfo2(70, 60, 50)


#匿名函数：Python使用lambda创建匿名函数，（即不再使用def这样的标准形式定义一个函数）
#lambda只是一个表达式，函数体比def简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
#lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
sum1 = lambda arg1, arg2 : arg1 + arg2
print("相加后的值为：", sum1(10, 20))


#return语句：
#return[表达式]语句用于退出函数，选择性地向调用者返回一个表达式。
def sum2(arg1, arg2):
    total = arg1 + arg2
    print("函数内：", total)
    return  total
total = sum2(10, 20)
print("函数外：", total)


#变量作用域：
#L(Local)局部变量
#E(Enclaosing）闭包函数外的函数中
#G(Global)全局作用域
#B(Built-in)内建作用域
#以L->E->G->B的规则查找，即在局部找不到，则去局部外的局部找（闭包），再者去全局找，再者去内建找
x = int(2.9)    #内建作用域
g_count = 0     #全局作用域
def outer():
    o_count = 1 #闭包函数外的函数中
    def inner():
        i_count = 2 #局部作用域

#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句如 if/elif/else/、try/except、for/while等）内定义的变量，外部也可以访问


#全局变量和局部变量：
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
#调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
total1 = 0  #这是一个全局变量
def sum3(arg1, arg2):
    total1 = arg1 + arg2    #total在这里是局部变量
    print("函数内是局部变量：", total1) #total1 = 30
    return  total1

sum3(10, 20)
print ("函数外是全局变量 : ", total1)   #total1 = 0


#global和nonlocal关键字
#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)  #num = 1
    num = 123
    print(num)  #num = 123
fun1()
#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()