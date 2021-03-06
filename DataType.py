# 数据类型
# 整数运算永远是精确的（除法也是），而浮点数运算则可能会有四舍五入的误差。
# 整数
print('正数：', 100, '；负数：', -8, '；十六进制：0xff00=', 0xff00)
# 浮点数
# 1.23x10^9和12.3x10^8是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。
# 对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5
print("数学写法的浮点数：", 1.23, -9.01)
print("科学写法的浮点数：", 1.23e-2, 1.23e-1, 1.23, 1.23e0, 1.23e1, 1.23e2)
print('1.23e-2 =', 1.23e-2)
print('1.23e-1 =', 1.23e-1)
print('1.23e0 =', 1.23e0)
print('1.23e1 =', 1.23e1)
print('1.23e2 =', 1.23e2)

# 字符串
# 字符串可以用单引号''、双引号""来引起来，单双引号本身不是字符串的内容，若要字符串里含有引号，则需要用到再引号一次或转义
print("字符串内含有英文单引号时''，外面需要用双引号")
print('字符串内含有英文双引号时""，外面需要用单引号')
print('字符串内同时含有英文单引号\'\'、双引号时\"\"，需要用转义字符，如：\\\'、\\\"，最外面用单双引号都可以')
# 两个字符串进行拼接，可以用+号、逗号或省略逗号直接紧跟都可以；
# 字符串与字符串变量拼接，可以用+、逗号拼接；
# 字符串与其他类型（包括其他类型的变量）拼接，只能用逗号，若要用+号拼接，可以将其他类型进行转换；
# 两个字符串变量进行拼接，+号、逗号都可以；
# 用*号重复
print(3 * 'un' + '，用+号拼接没有空格，''不用逗号直接紧跟也不会有空格，', '用逗号拼接时会有空格。')
# 原始字符串内需要换行，可以用三对双引号或单引号括起来。字符串内换行后，输出也换行：
print("""输出将换行：第1行
第2行
第3行""")
# 续行符\，末尾加\表示字符串内换行后，输出不会换行
print("""输出不换行：第1行\
第2行\
第3行""")

# 转义字符：\'、\"、\n、\t、\\
print('单引号\'转义，在字符串里输入：\\\'')
print('双引号\"转义，在字符串里输入：\\\"')
print('换行符\n转义，在字符串里输入：\\n')
print('''换行除了可以用换行符转义来实现，还可以直接在字符串内用enter键换行，如：第1行
第2行
第3行''')
print('制表符\t转义，在字符串里输入：\\t')
print('输出转义符自己\\，在字符串里输入：\\\\')
print('组合使用：\\\n\t\\')
# 换行除了可以用换行符转义来实现，还可以用'''str'''三对引号中使用enter键换行
print('''换行除了可以用换行符转义来实现，还可以直接在字符串内用enter键换行，如：第1行
第2行
第3行''')
# 不转义：r''
print('字符串'r'\\\t\\''完整输出，不转义，在括号里输入：print(''r\'\\\\\\t\\\\\')')
# 三对引号'''str'''与r''组合使用
s1 = r'''Hello,\n
Lisa!'''
s2 = '''Hello,\n
Lisa!'''
print(s1)  # \n不转义，完整输出
print(s2)  # \n将被转义成换行
# 字符串检索
a = 'ABCDEFG'
print('字符串a的第1个字符'+a[0])
print('字符串a的最后1个字符', a[-1])
print('字符串a的倒数第2个字符', a[-2])
# 字符串切片
a = 'ABCDEFG'
print('a[n1:n2]为前闭后开，如a[0:3]输出为“ABCDEFG”的第[1,4)个字符：'+a[0:3])
print('a[2:8]输出为“ABCDEFG”的第[3,8)个字符：', a[2:8])
print('a[-3:6]输出从“ABCDEFG”倒数第3个开始，即第[5,7)个字符：', a[-3:6])
print('a[:2]第一个参数缺省时默认为0：' + a[:2])
print('a[2:]第二个参数缺省时默认为字符串大小：'+a[2:])
print('所以a[:2]+a[2:]=完整的a：', a[:2]+a[2:])
print('a[:]都缺省则输出全部：'+a[:])

# 布尔值，只有True、False两种值，可以用and、or和not运算。
print('True:', True)
print('False:', False)
print('3 > 2:', 3 > 2)
print('3 < 2:', 3 < 2)
print('True and True:', True and True)
print('True and False:', True and False)
print('False and False:', False and False)
print('5 > 3 and 3 > 1:', 5 > 3 and 3 > 1)
print('True or True:', True or True)
print('True or False:', True or False)
print('False or False:', False or False)
print('5 > 3 or 1 > 3:', 5 > 3 or 1 > 3)
print('not True:', not True)
print('not False:', not False)
print('not 1 > 2:', not 1 > 2)
# 布尔在条件判断中的使用
a = 100
if a > 0:
    print(a)
else:
    print(-a)

# 空值：none
# 其他：列表、字典、自定义数据类型
# 变量：大小写英文、数字和_的组合，不能用数字开头。
# 动态语言：同一个变量可以反复赋值，而且可以是不同类型的变量。
a = 123
print(a)
a = 'ABC'
print(a)
# 静态语言：在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
# 经实验，在python3.7中，定义变量类型后赋值其他类型，不会报错。
b: int
b = 123
b = 'ABC'
print(b)
# 变量互相赋值
c: int = 123
d = c
c = 'abcd'
print('c='+c, "d="+str(d))  # 因为d是int类型，所以需要转换类型为字符串，才能与其他字符串用+号拼接

# python中定义常量时，可以使用全部大写来表示该变量为常量，但python中常量变量的值仍然可以被修改
PI = 3.14159265359
PI = PI/3
print('PI=' + str(PI))
