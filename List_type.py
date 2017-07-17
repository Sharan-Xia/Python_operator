#Python中有数字、字符串、列表、元祖、集合、字典，其中列表和元祖是最常用的
#列表都可以进行的操作包括索引、切片、加、乘、检查成员。列表中内置了确定列表长度、最大和最小元素的方法
#列表中的数据项不需要具有相同的类型

#可以使用下标访问列表中的值，同样可以使用方括号的形式截取字符
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6]

print('list1[0]:', list1[0])
print('list2[1:5]:', list2[1:5])

#更新列表：可以对列表中的数据项进行修改或更新。也可以使用append（）方法来添加列表项
print('第三个元素为：', list1[2])
list1[2] = 2001
print('更新后第三个元素为：', list1[2])

#删除列表元素：可以使用del语句来删除列表中元素。remove()方法
list1 = ['Google', 'Runoob', 1997, 2000]
print(list1)
del list1[2]
print('删除第三个元素之后的列表：', list1)

#列表脚本操作符：列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
'''
len([1, 2, 3])	                        3	                                长度
[1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]	                组合
['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	    重复
3 in [1, 2, 3]	                        True	                            元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	                            迭代
'''

#列表嵌套
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])

#列表函数和方法
'''
len(list)   列表元素个数
max(list)   返回列表最大值
min(list)   返回列表最小值
list(seq)   将元祖转换为列表

list.append(obj)    在列表末尾添加新的对象
list.count(obj)     统计摸个元素在列表中出现的次数
list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)     将对象插入列表
list.pop(obj=list[-1])      移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)     移除列表中某个值的第一个匹配项
list.reverse()      反向列表中元素
list.sort([func])   对原列表进行排序
list.clear()        清空列表
list.copy()         赋值列表
'''

list_2d = [[0 for i in range(5)] for i in range(5)]
print(list_2d)
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
print(list_2d)

l = [i for i in range(0, 15)]
print(l[::2])
