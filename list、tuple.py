# list()，创建变量时可以同时声明数据类型，也可以不声明
# list()中的元素可以是不同的数据类型
# list()中包含另一个list叫二维数组，还可以有三维、思维等
# list()可以为空，此时长度为0
classmates1: list = ['姚明', '小米',  123, True, '朔朔', 'tiger']
classmates2 = ['Michael', 'Bob', 'dora', 'Tracy']
classmates3 = ['python', 'java', ['asp', 'php'], 'scheme']
classmates4 = []
print(type(classmates1), classmates1, len(classmates1))  # 两种声明方式，类型都为list()
print(type(classmates2), classmates2, len(classmates2))
print('classmates3[2]也是一个list：', classmates3[2],
      '，这个list中的元素为：', classmates3[2][0], classmates3[2][1])
print('空数组的长度=', len(classmates4))  # 此时用classmates4[0]或classmates4[1]均会报异常
print(classmates1[0], classmates1[1])  # 索引从0开始，超出范围会报错
print(classmates2[2], classmates2[3])
# 输出最后一个元素的方法，用负数超出范围时也会报错
print(classmates1[-1], classmates2[len(classmates2)-1])
# 添加、插入：末尾添加用append、指定位置插入用户insert
classmates1.append('Adam')
classmates1.insert(0, '红米')
classmates1.insert(10, '炒鸡蛋米')  # 若指定位置不存在，则在最后一个位置后面插入
classmates1.insert(-110, '炒鸡蛋米')  # 若指定位置不存在，则在第一个位置前面插入
classmates4.insert(4, 'dajkkdjj')
print('增加元素后的classmates1：', classmates1)
print('增加元素后的classmates4：', classmates4)
# 删除指定位置的元素
classmates1.pop(0)
print('删除第1个元素后：', classmates1)
classmates1.pop(-1)
print('删除最后1个元素后：', classmates1)
classmates1.pop(len(classmates1)-1)
print('再次删除最后1个元素后：', classmates1)
# 替换指定位置的元素
classmates1[0] = 'Sarah'

# tuple():元组，一旦初始化后则不能再被修改，因此不能被添加、插入，但可以删除元素
t1 = (1, True, 'Michael', 'Bob', 'Tracy')
t2: tuple = ()  # 空的tuple()
t3 = ('一个元素',)  # 若tuple()中只含有一个元素，必须加逗号，以便与数学计算的小括号进行区分
t4 = ('一个元素')   # 只有一个元素时若不加逗号，则为str
print(type(t1), t1)  # <class 'tuple'> (1, True, 'Michael', 'Bob', 'Tracy')
print('t2是空的tuple()：', t2)
print('t3的类型：', type(t3))  # t3的类型： <class 'tuple'>
print('t3的内容：', t3)        # t3的内容： ('一个元素',)，注意：显示时也加了逗号的
print('t4的类型：', type(t4), ',t4的内容：' + t4)  # t4的类型： <class 'str'> t4的内容： 一个元素

# 若typle()中含有list元素，则可以实现元素可变，但个数始终不变
t5 = (1, True, 'Michael', 'Bob', 'Tracy', [
      2, False, 'L-Michael', 'L-Bob', 'L-Tracy'])
print(t5[0], t5[5][1])
# 通过修改list()中元素的值来达到修改tuple()元组的值，修改的是tuple中list元素内的指向地址，tuple本身的元素指向没有被修改
t5[5].insert(1, True)
t5[5].pop(-1)
print(t5)

# 将tuple()中的元素为其他变量赋值
t = (1, 2, 3, 4)
a = t[0]
print(a)  # 1
a, b, c, d = t  # 同时赋值多个变量时，变量数必须正好=所有元素数量，否则会抛异常
print(a, b, c, d)  # 1 2 3 4

# 所谓的不能修改，是指tuple()中每个元素的指向不能被修改，但若指向的是可变（如list），则修改可变可以得到tuple被修改的效果
# 如下，t中每个元素的指向不变
# t[0]指向'a'、t[1]指向'b'、t[2]指向数组['A', 'B']
# 修改这个数组内每个元素的指向，使得t[2]指向的内容变化，最终得到t被修改的效果
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # 输出：('a', 'b', ['X', 'Y'])
