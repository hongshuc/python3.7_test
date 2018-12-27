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
