# dict字典，使用键-值（key-value）存储
d1 = {'Michael': 97, 'Adam': 89, 'Bob': 67, 'Jerry': 73}
print(d1)
print(type(d1))  # <class 'dict'>
print(len(d1))   # 4
print(d1['Jerry'])  # 73

# 增加一个元素，不需要用add、append、insert等方法，直接赋值即可
d1['Merry'] = 81
# 替换或修改一个已存在元素的值
d1['Michael'] = 100
d1.pop('Jerry')
print(d1)  # {'Michael': 100, 'Adam': 89, 'Bob': 67, 'Merry': 81}

# 声明一个空的dict()
d2 = {}
print(type(d2))  # <class 'dict'>
print(len(d2))   # 0
# print(d2['Jerry'])  # key不存在，抛异常
d2['小明'] = '四川省'
d2['小辉'] = '江苏省'
print(d2)

# 判断key在dict()中是否存在的方法，有两种方法
d3 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
print('d3初始内容：', d3)
if 'A' in d3:  # 判断key是否已存在dict()中
    d3['A'] = 11111
else:
    d3['A'] = 11
print(d3)
# dict.get(key, default=None)返回指定键的值，如果值key不在字典中则返回default；
# 若未指定default的值则返回默认值none，已指定则返回指定值。
if d3.get('H'):  # 判断key是否已存在dict()中
    print(d3.get('H'))
    d3['H'] = 21111
else:
    print(d3.get('H'))
    d3['H'] = 21
print(d3)

if d3.get('I', 1) != 1:  # 判断key是否已存在dict()中
    print(d3.get('I'))
    d3['I'] = 22111
else:
    print(d3.get('I'))
    d3['I'] = 22
print(d3)


# dict的key必须是不可变对象，即便使用list()作为key值
# 一旦dict()被初始化之后，key值将直接指向最终的值，而不是指向这个list中的元素
# 因此此时再改变list()中元素并不会影响到dict()中的key


def dict_value(l, d):
    a = 1
    for n in l:
        d[n] = a
        a = a+1
        print(d)


l1 = ['A', 'B', 'C']
d3 = {}
# 第一次调用函数dict_value(l, d)，d3被初始化，执行结果如下：
# {'A': 1}
# {'A': 1, 'B': 2}
# {'A': 1, 'B': 2, 'C': 3}
dict_value(l1, d3)
l1.append('D')
# 第二次调用函数dict_value(l, d)，d3已被赋值的key-value不会被改变，前三次输出相同：
# {'A': 1, 'B': 2, 'C': 3}
# {'A': 1, 'B': 2, 'C': 3}
# {'A': 1, 'B': 2, 'C': 3}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dict_value(l1, d3)
l1[0] = 'AA'
# 第三次调用函数dict_value(l, d)，d3已被赋值的key-value不会被改变，四次输出均相同，第1个key并未因list()元素改变而改变：
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'AA': 1}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'AA': 1}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'AA': 1}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'AA': 1}
dict_value(l1, d3)

d4 = {}
a = ['a', 'b']
d4[a[0]] = 1
d4[a[1]] = 2
print('数组a=', a, '字典d4=', d4)  # 输出：数组a= ['a', 'b'] 字典d4= {'a': 1, 'b': 2}
a[0] = 'aa'
d4[a[0]] = 1
d4[a[1]] = 2
# 输出：数组a= ['aa', 'b'] 字典d4= {'a': 1, 'b': 2, 'aa': 1}，数组的元素指向被改变，但字典进行的增加，而不是修改
print('数组a=', a, '字典d4=', d4)

# set：一组key的集合，不含value，重复元素在set中将被自动过滤，因此不含重复key
# set的key也不可变，但是与dict似乎不太一样
# 要创建一个set，需要提供一个list作为输入集合：
s1 = set([5, 2, 2, 3, 5, 7, 6])
print(s1)  # 输出始终为：{2, 3, 5, 6, 7}，去重了
s2 = set(['A', 'C', 'B', 'E', 'F', 'D', 'd'])
# 顺序随机：{'C', 'A', 'E', 'd', 'F', 'D', 'B'}或{'F', 'A', 'd', 'E', 'C', 'D', 'B'}等
print(s2)

# set.add()添加
s1.add(9)
print(s1)  # 输出：{2, 3, 5, 6, 7, 9}

# set.remove()删除
s1.remove(5)
print(s1)  # 输出：{2, 3, 6, 7, 9}

# 交集、并集
s3 = set([1, 2, 3, 4])
s4 = set([2, 4, 5, 6])
print('两个set交集用&：', s3 & s4)  # 输出：{2, 4}
print('两个set并集用|：', s3 | s4)  # 输出：{1, 2, 3, 4, 5, 6}

# 使用list作为set的key，将能够达到改变set的效果
a = ['a', 'b']
s5 = set(a)
print(s5)  # {'a', 'b'}
a[0] = 'aa'
print(s5)  # {'a', 'b'}
s5 = set(a)
print(s5)  # {'aa', 'b'}，此时key被改变了


# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
# str、tuple、dict、set都是不可变，但是有些区别
# str可以通过重新赋值来改变，但不能通过replace方法来修改值，因为replace方法是创建一个新的字符串
# dict将直接指向最终的值，即便使用list、变量等作为dict的key值，变量本身发生变化，
# 因为dict的key值是指向之前的最终值，变量改变后再次赋值给dict，只能作为新的key值被添加，而不是修改dict原来的key
# tuple、set中元素的指向不变，但若指向的是一个变量，修改变量可以使得tuple、set呈现出来的key值被修改，与dict不同
