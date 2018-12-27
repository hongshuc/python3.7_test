# print打印字符串
# 单引号
print('I "said" do not touch this.')
# 双引号
print("Hello World!")
# 字符串拼接，+号、逗号或不用逗号都可以，但字符串与其他数据类型拼接，则必须用逗号拼接
print("My name is:""chlone")
print("The quick brown fox", "jumps over", "the lazy dog")

# print与运算
print("I will now count my chickens:")
print("Hens", 25+30/6)
print("Roosters", 100-25*3 % 4)
print("Now I will count the eggs:")
print("7/3 =", 7 / 3)     # 除，并以浮点类型返回
print("7//3 =", 7 // 3)   # 取整数
print("7%3 =", 7 % 3)     # 取余
print("1/4 =", 1/4)
print("1//4 =", 1//4)
print(3+2+1-5+4 % 2-1/4+6)
print("Is it true that 3+2<5-7?")
print(3+2 < 5-7)
print("What is 3+2?", 3+2)
print("What is 5-7?", 5-7)
print("Oh,that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
print('5**2=', 5**2)   # **计算幂

# 输入input()然后再输出
name = input('Please enter your name:')
print('Hello', name)
print('1024*768=', 1024*768)
