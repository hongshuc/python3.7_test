age = int(input('请输入年龄:'))  # input()函数返回的数据为str，因此此处必须转换成int
if age < 18:
    print('未成年人')
elif age < 60:
    print('成年人')
else:
    print('老年人')
print('年龄是：', age)

# 当条件判断中的参数为非零数值、非空字符串、非空list等，就判断为True，否则为False
l1 = []
if 0 or '' or l1:
    print('True')
else:
    print('False')

l2 = [1, 2]
if 1 and '非空字符串' and l2:
    print('True')
else:
    print('False')


# 体质指数（BMI）=体重（kg）÷身高^2（m）
# from decimal import Decimal  # 计算BMI并使用Decimal保留两位小数时需要用到
stature = float(input('计算BMI，请输入你的身高(cm)：'))
weight = float(input('请输入你的体重(kg)：'))
# 对计算结果四舍五入并保留两位小数的方法
# %f转换后的值是str，因此需要外面在float格式化一次
BMI = float('%.2f' % (weight/(stature*stature)*10000))
# BMI = Decimal(weight/(stature*stature)*10000).quantize(Decimal('0.00'))
# BMI = round(weight/(stature*stature)*10000, 2)
print(BMI)
if BMI < 18.5:
    print('您的BMI是：%s,体重过轻' % (BMI))
elif BMI < 25:
    print('您的BMI是：%s,体重正常' % (BMI))
elif BMI < 28:
    print('您的BMI是：%s,体重过重' % (BMI))
elif BMI < 32:
    print('您的BMI是：%s,体重肥胖' % (BMI))
else:
    print('您的BMI是：%s,体重严重肥胖' % (BMI))
