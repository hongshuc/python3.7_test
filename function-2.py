# 使用def定义函数
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
# 因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。


import math  # 函数move()、quadratic()要用


def my_abs(x):
    if not isinstance(x, (int, float)):  # 内置函数isinstance()用于数据类型检查
        raise TypeError('bad operand type,数据类型错误')  # 如果传入错误的参数类型，函数就可以抛出一个错误
    if x >= 0:
        return x
    else:
        return -x


print('请输入数字：')
num = input('')
print(my_abs(num))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs  # 将变量指向abs函数
print(a(-1))  # 所以也可以通过a调用abs函数
print(type(hex(17)))

# 空函数，当函数内代码未确定时，可以用pass占位


def nop():
    pass


# if语句也可以用pass来占位
age = 19
if age > 18:
    pass

# 返回多个值，如地图中的坐标。有多个返回值时，其实返回的是一个tuple类型


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)        # 151.96152422706632 70.0
print(type(r), r)  # <class 'tuple'> (151.96152422706632, 70.0)


# 计算一元二次方程的解


def quadratic(a, b, c):
    s = b*b-4*a*c
    if a == 0:
        x = -c/b
        return x
    elif s == 0:
        x = -b/2/a
        return x
    elif s > 0:
        x1 = (math.sqrt(s)-b)/2/a
        x2 = (-math.sqrt(s)-b)/2/a
        return(x1, x2)
    else:
        return '无解'


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(0, 2, 1) =', quadratic(0, 2, 1))
print('quadratic(10, 2, 10) =', quadratic(10, 2, 10))
