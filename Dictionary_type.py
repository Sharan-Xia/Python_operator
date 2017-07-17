#字典是一种可变容器模型，可以存储任意类型的对象。键值对使用冒号（:）分割，每个对之间使用逗号（,）分割，字典存储在花括号{}中。
#字典中的键必须是唯一的，但值侧不必。值可以取任何数据类型，键的类型是不可变的

#访问字典中的值：
dict = {'Name':'Runoob', 'Age':7, 'Class':'First'}
print("dict['Name']:", dict['Name'])
print("dict['Age']", dict['Age'])

#修改字典：添加、删除、修改键值对
dict['Age'] = 8 #更新age
dict['School'] = 'SIAS' #添加信息

print("dict['Age']", dict['Age'])
print("dict['School']:", dict['School'])

del dict['Name'] #删除键‘Name’
# dict.clear()    #删除字典
# del dict    #删除字典

#字典键的特性：
#1）不予许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#2）键必须不可变，所以可以用数字、字符串、或元组充当，而用列表不行
dict1 = {'Name':'Runoob', 'Age':7, 'Name':'菜鸟'}
print("dict1['Name']:", dict1['Name'])

#字典内置函数：
#len（dict）计算元素个数，即键的总数
#str（dict）输出字典，以打印字符串表示
#type（variable）返回变量类型