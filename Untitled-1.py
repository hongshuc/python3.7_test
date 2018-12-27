def f1(a, b, c=0, *args, **kw):  # 没有命名关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):  # 没有可变参数
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 调用
args = (1, 2, 3, 4, 5, 6)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  # a = 1 b = 2 c = 3 args = (4, 5, 6) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)  # 看不懂，没有可变参数，为什么调用时可以输入可变参数，且元素只能是2-3
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)  # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
