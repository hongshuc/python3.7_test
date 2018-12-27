#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 声明文件为UTF-8编码，则在文件开头写以上两行：

# 1字节（byte）=8比特（bit），一字节能表示的最大整数为：二进制11111111=十进制255
#
# 编码发展简介
# 1、美国最先指定ASCII编码，只含有大小写英文字母、数字和一些符号，是1个字节；
# 2、各国各自制定编码，如：中国制定了GB2312编码，日本有Shift_JIS编码里，韩国有Euc-kr编码；多国语言混用时，容易乱码；
# 3、Unicode将所有语言统一进行编码，以解决乱码问题，引出新的问题：Unicode编码通常为2个字节，当使用文本以英文为主时，
# 也必须转换为2个字节，将造成存储空间、传输上的浪费（实际上1个字节就够了）；
# 4、UTF-8编码为“可变长编码”，会把英文字母编译成1个字节，汉字通常为3个字节，生僻字符被编译成4-6个字节，
# 若文本以英文字符为主，使用UTF-8编码可解决浪费问题；
# 总结
# 计算机系统通用的字符编码工作方式：
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件；
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器；
# python的字符串str在内存中以Unicode表示，一个字符对应若干个字节。

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
import math
print("使用ord()函数获取字符的整数表示，如：ord('a')=", ord('a'), ",ord('A')=", ord('A'))
print("使用chr()函数把编码转换为对应的字符，如：chr(66)=", chr(66), ",chr(20013)=", chr(20013),
      ",chr(25991)=", chr(25991))
print('\u4e2d\u6587')  # 4e2d为十六进制，转换为十进制为20013，6587转换为是兼职为25991，\u是什么意思不清楚
print('20013')

# 字节bytes的字符串
# 1、可以使用b''来直接声明单位为bytes的字符串
# 声明字节bytes为单位的字符串，表示每个字符只占用一个字节；普通str类型的字符串，表示每个字符占用多个字节；两种方式的内容是一样的。
b1 = b'abcd'
print(b1)
# 2、可以使用encode()方法可以将str转变为bytes，python使用的是Unicode，所以不能再转换成Unicode。
# 纯英文的str可以用ASCII编码为bytes，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为ASCII编码不含中文。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
print('ABC'.encode('ascii'))  # 输出：b'ABC'
print('ABC'.encode('UTF-8'))  # 输出：b'ABC'
print('中文'.encode('utf-8'))  # 输出：b'\xe4\xb8\xad\xe6\x96\x87'
# 3、使用decode()方法可以将bytes变为str，python使用的是Unicode，所以不能再转换成Unicode。
print(b'ABC'.decode('ascii'))  # 输出：ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 输出：中文
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# errors='ignore'忽略错误字节，但在python3.7中不管用

# len()函数计算str的字符数，bytes的字节数：
print(len(b'ABC'))  # 输出：3，3个字节
print(len('ABC'))  # 输出：3，3个字符
print(len('中文'))  # 输出：2，2个字符
print(len('中午'.encode('utf-8')))  # 输出：6，6个字节
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 输出：6，6个字节

# format()
print('{0}'.format(1))
print('{0:.2f}%'.format(2.1456))  # 2.15%
print('我是{0}的{1}'.format('小明', '老师'))

# 占位符：%d 整数，%f 浮点数，%s 字符串，%x 十六进制整数。如果只有一个%?，括号可以省略。
print('hello,%s' % 'word')
print('Hi %s,your score is %d.' % ('Bear', 59))
# 当有% 50的这个%时，前面字符串里的必须输入两个%号才能输出一个%号，否则将报错，后面字符串里一个%即可
print('数字后面跟%%，如：占比 %d %%' % 50, '%')
# 'growth rate: %d %%' % 7
print('%1d' % (3))          # 输出：3
print('%2d' % (3))          # 输出： 3
print('%3d' % (3))          # 输出：  3
print('%01d' % (3))         # 输出：3
print('%02d' % (3))         # 输出：03
print('%03d' % (3))         # 输出：003
print('%2d-%02d' % (3, 1))  # 输出：3-01
print('%.2f' % 3.1415926)    # 输出：3.14
print('%2.2f' % 3.1415926)   # 输出：3.14
print('%02.2f' % 3.1415926)  # 输出：3.14
print('%.10f' % 3.1415926)   # 输出：3.1415926000
print('%.20f' % 3.1415926)   # 输出：3.14159260000000006841，这是为什么？？？

# 占位符详解
# %s 字符串
string = "hello"
# %s打印时结果是hello
print("string=%s" % string)      # output: string=hello
# %2s意思是字符串长度为2，当原字符串的长度超过2时，按原长度打印，所以%2s的打印结果还是hello
print("string=%2s" % string)     # output: string=hello
# %7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串左侧补空格，
# 所以%7s的打印结果是  hello
print("string=%7s" % string)     # output: string=  hello
# %-7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串右侧补空格，
# 所以%-7s的打印结果是  hello
print("string=%-7s!" % string)     # output: string=hello  !
# %.2s意思是截取字符串的前2个字符，所以%.2s的打印结果是he
print("string=%.2s" % string)    # output: string=he
# %.7s意思是截取字符串的前7个字符，当原字符串长度小于7时，即是字符串本身，
# 所以%.7s的打印结果是hello
print("string=%.7s" % string)    # output: string=hello
# %a.bs这种格式是上面两种格式的综合，首先根据小数点后面的数b截取字符串，
# 当截取的字符串长度小于a时，还需要在其左侧补空格
print("string=%7.2s" % string)   # output: string=     he
print("string=%2.7s" % string)   # output: string=hello
print("string=%10.7s" % string)  # output: string=     hello
# 还可以用%*.*s来表示精度，两个*的值分别在后面小括号的前两位数值指定
print("string=%*.*s" % (7, 2, string))      # output: string=     he

# %d 整型
num = 14
# %d打印时结果是14
print("num=%d" % num)            # output: num=14
# %1d意思是打印结果为1位整数，当整数的位数超过1位时，按整数原值打印，所以%1d的打印结果还是14
print("num=%1d" % num)           # output: num=14
# %3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格，所以%3d的打印结果是 14
print("num=%3d" % num)           # output: num= 14
# %-3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数右侧补空格，所以%3d的打印结果是14_
print("num=%-3d" % num)          # output: num=14_
# %05d意思是打印结果为5位整数，当整数的位数不够5位时，在整数左侧补0，所以%05d的打印结果是00014
print("num=%05d" % num)          # output: num=00014
# %.3d小数点后面的3意思是打印结果为3位整数，
# 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果是014
print("num=%.3d" % num)          # output: num=014
# %.0003d小数点后面的0003和3一样，都表示3，意思是打印结果为3位整数，
# 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果还是014
print("num=%.0003d" % num)       # output: num=014
# %5.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，再在左侧补空格，
# 规则就是补0优先，最终的长度选数值较大的那个，所以%5.3d的打印结果还是  014
print("num=%5.3d" % num)         # output: num=  014
# %05.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，
# 由于是05，再在左侧补0，最终的长度选数值较大的那个，所以%05.3d的打印结果还是00014
print("num=%05.3d" % num)        # output: num=00014
# 还可以用%*.*d来表示精度，两个*的值分别在后面小括号的前两位数值指定
# 如下，不过这种方式04就失去补0的功能，只能补空格，只有小数点后面的3才能补0
print("num=%*.*d" % (4, 3, num))  # output: num= 014

# %f 浮点型
# import math  # 前面有一个了，所以这里注释掉
# %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度，最后一位小数四舍五入
# 只是%f时表示原值，默认是小数点后6位数
print("PI=%f" % math.pi)             # output: PI=3.141593
# 只是%9f时，表示打印长度9位数（小数点后仍然是6位，小数点前两位），小数点也占一位，不够左侧补空格
print("PI=%9f" % math.pi)            # output: PI=_3.141593
# 只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0
print("PI=%03.f" % math.pi)          # output: PI=003
# %6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格
print("PI=%6.3f" % math.pi)          # output: PI=_3.142
# %-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格
print("PI=%-6.3f" % math.pi)         # output: PI=3.142_
# 还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定
# 如下，不过这种方式06就失去补0的功能，只能补空格
print("PI=%*.*f" % (6, 3, math.pi))   # output: PI=_3.142
