# 使用def定义函数
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
# 因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

# 参数：必选参数（位置参数？）、默认参数、可变参数（*参数名）、命名关键字参数（*,参数名1,参数名2）、关键字参数（**参数名）
# 默认参数的坑，见下面的例子
# 原因：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())  # ['END']
print(add_end([1, 2]))  # [1, 2, 'END']
print(add_end())  # ['END', 'END']，输出了两个'END'

# 可以修改如下：


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())  # ['END']
print(add_end())  # ['END']

# 可变参数，定义方法：*参数名。调用时若传递list、tuple类型的参数时可以省略[]、()，如下
# 可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple


def calc(number):  # 定义成必选参数
    print(type(number))  # list调用则类型为list，tuple调用则类型为tuple
    return


calc([1, 2, 3])  # 调用函数时，若参数为list，[]不能省略，否则抛异常
calc(('a', 'b', 'c'))  # 调用函数时，若参数为tuple，()不能省略，否则抛异常


def calc_1(*number1):  # 定义成可变参数
    print(type(number1))  # 无论list、tuple调用，number1的类型均为tuple
    return


# 各种调用方法
calc_1()
calc_1(1, 2, 3)  # 调用函数时，若参数为list，[]能省略
calc_1('a', 'b', 'c')  # 调用函数时，若参数为tuple，()能省略
num1 = [1, 2, 3]
calc_1(num1[0], num1[1], num1[2])
num2 = (4, 5, 6)
calc_1(num2[0], num2[1], num2[2])
num3 = [7, 8, 9]
calc_1(*num3)  # 注意：这种调用方法最简单，*num3表示把num3这个list或tuple或set的所有元素作为可变参数传进去

# 关键字参数，定义方法：**参数名
# 关键字参数允许传入0个或任意个含参数名的参数，并在函数内部自动组装为一个dict
# 关键字参数的作用：可以扩展函数的功能，
# 比如：做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
# 利用关键字参数来定义这个函数，可以将剩余的可选项全部接受，从而满足注册的需求。


def person(name, age, **kw):  # 定义关键字参数方法1
    print('name:', name, 'age:', age, 'other:', kw)
    return


# 各种调用方法
# 关键字参数传入0个
# name: Michael age: 30 other: {}
person('Michael', 30)
# 关键字参数传入1个
# name: Bob age: 35 other: {'city': 'Beijing'}
person('Bob', 35, city='Beijing')
# 关键字参数传入多个
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
person('Adam', 45, gender='M', job='Engineer')
# 使用变量名进行调用
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数，两种定义方法：
# 1、*,参数名1,参数名2,参数名3...（表示只能传入固定的参数数量）
# 2、已经有可变参数时，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *, city, job):  # 定义关键字参数方法2
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
    return


# 调用时，关键字参数的数量必须一致，不能多或少，否则异常
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
person('Adam', 45, city='M', job='Engineer')
# 使用变量名进行调用
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


def person(name, age, *args, city, job):    # 定义关键字参数方法3，可变参数后的city、job是关键字参数
    print('name:', name, 'age:', age, 'args:',
          args, 'city:', city, 'job:', job)
    return


# 调用时必须同时传入关键字参数名字（顺序可以不一致），且数量须一致
# 调用时若不传关键字参数名，解释器会把所有参数均视为位置参数，使得位置参数数量超过定义的数量，因此报错
# name: Jack age: 24 args: () city: Beijing job: Engineer
person('Jack', 24, city='Beijing', job='Engineer')
# name: Jack age: 24 args: (3,) city: Beijing job: Engineer
person('Jack', 24, 3, job='Engineer', city='Beijing')


# 参数组合，以上参数可以同时使用，顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):  # 没有命名关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):  # 没有可变参数
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 调用
f1(1, 2)  # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)  # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
args = (1, 2, 3, 4, 5, 6)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  # a = 1 b = 2 c = 3 args = (4, 5, 6) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)  # 看不懂，没有可变参数，为什么调用时可以输入可变参数，且元素只能是2-3
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)  # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
