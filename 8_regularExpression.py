#re模块使Python语言拥有全部的正则表达式功能
#compile函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象，该对象拥有一系列方法用于正则表达式匹配和替换。
#re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

#re.match函数:
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#函数语法：re.match(pattern, string, flags=0)
#pattern:匹配的正则表达式
#String：要匹配的字符串
#flags：标志位，用于控制正则表达式的匹配方式。如区分大小写，多行匹配等等
#re.match方法返回一个匹配对象，可以使用group（num）或groups（）函数来获取匹配表达式

import re


print(re.match('www', 'www.baidu.com').span())  #
