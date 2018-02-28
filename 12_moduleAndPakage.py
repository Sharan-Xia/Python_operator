#模块：包含了python定义和声明的文件，文件名就是模块名字加上.py的后缀
'''
模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，它们只在模块名第一次遇到导入import语句时才执行
sys.module中找到当前已经加载的模块，sys.module是一个字典，内部包含模块名与模块对象的映射，该字典决定了导入模块时是否需要重新导入
如果改变了模块的内容必须重启程序，Python不支持重新加载或删除之前导入的模块
'''


import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')
