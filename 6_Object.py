#面向对象：
#类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
#数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
#方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
#实例变量：定义在方法中的变量，只作用于当前实例的类。
#继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待
#实例化：创建一个类的实例，类的具体对象。
#方法：类中定义的函数。
#对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

#类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
#对象可以包含任意数量和类型的数据。
#创建一个类之后，可以通过类名访问其属性

#类对象：
#类对象支持两种操作：属性引用和实例化。
#属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
class MyClass:
    i = 12345
    def f(self):
        return "Hello World!"

x = MyClass()   #实例化类
print("MyClass 类的属性 i 为：", x.i) #访问类的属性
print("MyClass 类的方法 f 输出为：", x.f()) #访问类的方法

#类的对象初始化函数（构造函数）
#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)


#类方法：在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，
# 类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
class people:
    name = ''
    age = 0
    __weight = 0    #定义私有属性,私有属性在类外部无法直接进行访问
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s说：我%d岁。"%(self.name, self.age))

p = people('runoob', 10, 30)
p.speak()


#继承：需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，
# python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
#BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。
# 除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
#类定义
class people1:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承
class student(people1):
    grade = ""
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = student('ken', 10, 60, 3)
s.speak()


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()