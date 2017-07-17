#元组与列表类似，但元组中的数据不能修改。且元组使用小括号，列表使用中括号
tup1 = ()   #创建空元组
tup1 = (50, )   #元组中只包含一个元素时，需要在元素后面添加逗号

#访问元组：元组可以使用下标来访问元组中的值
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print('tup1[0]:', tup1[0])
print('tup2[1:5]:', tup2[1:5])

#修改元组：元组中的值不予许修改，但可以对元组进行连接组合
tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')
#tup1[0] = 100 #修改元组中值是非法的
tup3 = tup1 + tup2
print(tup3)

#删除元组：元组中的值不予许删除，但可以使用del删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
#print(tup)

#元组运算符：与字符串一样，元组之间可以使用‘+’好或‘*’号进行运算，运算后会产生一个新的元素
len((1, 2, 3))
tup = (1, 2, 3) + (4, 5, 6)
tup1 = ('Hi!', )*4
if (3 in (1, 2, 3)):
    print()
for x in (1, 2, 3):
    print(x)

#元组索引、截取：元组也是一个序列，可以访问指定的元素和截取其中的一段元素
L = ('Google', 'Taobao', 'Runoob')
print(L[2])
print(L[-2])
print(L[1:])

#元组内置函数：
tuple1 = (5, 4, 8)
list1 = ['Google', 'Taobao', 'Runoob']
print(len(tuple1))  #计算元组个数
print(max(tuple1))  #返回最大元素
print(min(tuple1))  #返回最小元素
tuple2 = tuple(list1)
print(tuple2)





