# 1.算术运算符
'''
+ 加，两个对象相加
- 减，得到负数或者一个数减去另一个数
* 乘，两个数相乘或者返回一个重复若干次的字符串
/ 除，x除以y
% 取模，返回除法的余数
** 幂，返回x的y次幂
// 取整除，返回商的整数部分
'''

a = 21
b = 10
c = 0

c = a + b
print("c的值为：", c)

c = a - b
print("c的值为：", c)

c = a * b
print("c的值为：", c)

c = a / b
print("c的值是：", c)

c = a % b
print("a的值是：", c)

a = 2
b = 3
c = a ** b
print("a的值是：", c)

a = 11
b = 5
c = a // b
print("c的值是：", c)

print("\n")
# 2.比较运算符 (Command+Option+L整理代码)
'''
==  等于，比较对象是否相等
!=  不等于，比较两个对象是否不相等
>   大于，返回x是否大于y
<   小于，返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别于特殊的变量True和False等价。注意，这些变量名的大写
>=  大于等于，返回x是否大于等于y。
<=  小于等于，返回x是否小于等于y。
'''
a = 21
b = 10
c = 0
if (a == b):
    print("a等于b")
else:
    print("a不等于b")

if (a != b):
    print("a不等于b")
else:
    print("a等于b")

if (a < b):
    print("a小于b")
else:
    print("a大于大于b")

if (a > b):
    print("a大于b")
else:
    print("a小于等于b")

a = 5
b = 20
if (a <= b):
    print("a小于等于b")
else:
    print("a大于b")

if (b >= a):
    print("b大于等于a")
else:
    print("b小于a")

print("\n")
# 3.赋值运算符
'''
=   简单的赋值，
+=  加法赋值，
-=  减法赋值，
*=  乘法赋值，
/=  除法赋值，
%=  取摸赋值
**= 幂赋值，
//= 取整除赋值
'''
a = 21
b = 10
c = 0

c = a + b   #c = 31
print("c的值是：", c)

c += a  #c = c + a
print("c的值是：", c)   #c = 52

c *= a  #c = c * a
print("c的值是：", c)   #c = 1092

c /= a  #c = c / a
print("c的值是：", c)   #c = 52.0

c = 2
c %= a  #c = c % a
print("c的值是：", c)   #c = 2

c **= a #c = c ** a(2**21)
print("c的值是：", c)   #c = 2097152

c //= a #c = c // a
print("c的值是：", c)   #c = 99864

print('\n')
# 4.位运算符
'''
&   按位与，相应位 同1异0
|   按位或，相应位 有1为1，无1为0
^   按位异或，相应位相异时，结果为1
~   按位取反，1变0，0变1
<<  左移位，高位丢弃，地位补0
>>  
'''
a = 60  #60 = 0011 1100
b = 13  #13 = 0000 1101
c = 0

c = a & b   #12 = 0000 1100
print("c的值是：", c)

c = a | b   #61 = 0011 1101
print("c的值是：", c)

c = a ^ b   #49 = 0011 0001
print("c的值是：", c)

c = ~a  #-61 = 1100 0011
print("c的值是：", c)

c = a << 2  #240 = 1111 0000
print("c的值是：", c)

c = a >> 2  #15 = 0000 1111
print("c的值是：", c)


print('\n')
# 5.逻辑运算符
'''
and , 布尔"与" -- 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
or  , 布尔"或" -- 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值
not , 布尔"非" -- 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''
a = 10
b = 20

if (a and b):
    print("变量a和变量b都为true")
else:
    print("变量a和变量b有一个不为true")

if (a or b):
    print("变量a和变量b都为true, 或其中一个变量为true")
else:
    print("变量a和变量b都不为true")

a = 0
if (a and b):
    print("变量a和变量b都为true")
else:
    print("变量a和变量b有一个不为true")

if (a or b):
    print("变量a和变量b都为true, 或其中一个变量为true")
else:
    print("变量a和变量b都不为true")

if not(a and b):
    print("变量a和变量b都为false, 或其中一个变量为false")
else:
    print("变量a和变量b都不为true")

print('\n')
# 6.成员运算符
'''
in  如果指定的序列中找到值返回True，否则返回False。
not in  与in相反
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

print('\n')
# 7.身份运算符
'''
is  判断两个标识符是不是引用自一个对象，是返回True，不是返回False
is not  判断两个标识符是不是引用自不同的对象，
'''
a = 20
b = 20
if (a is b):
    print('a和b有相同的标识符')
else:
    print('a和b有不相同的标识符')

if (id(a) == id(b)):
    print('a和b有相同的标识符')
else:
    print('a和b有不相同的标识符')

b = 30
if (a is b):
    print('a和b有相同的标识符')
else:
    print('a和b有不相同的标识符')

if (id(a) == id(b)):
    print('a和b有相同的标识符')
else:
    print('a和b有不相同的标识符')
'''
is与==的区别
is判断两个变量引用对象是否为同一个，==判断引用变量的值是否相等
'''


print('\n')
# 8.运算符优先级
