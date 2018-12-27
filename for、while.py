# 计算1+2+3+...+10的方法，当计算较多数字时，用range()很方便
# 使用for n in x:来计算
sum1 = 0
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum1 = sum1+n
    print(sum1)
print('最后总和：', sum1)

sum2 = 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in num:
    sum2 = sum2+n
print('总和：', sum2)

sum3 = 0
# range(start, stop[, step])生成[start,stop)之间的整数序列，并以step为递增，
# start省略时默认为0、step省略时默认为1，stop为必选参数
# 使用list(range(start, stop[, step]))可以查看到这个整数序列的所有元素
for n in range(11):
    sum3 = sum3+n
print('总和：', sum3)

# 计算1+2+3+...+1000
sum4 = 0
for n in range(1001):
    sum4 = sum4+n
print('总和：', sum4)

# 使用while 条件判断: 来计算
sum5 = 0
n = 1000
while n > 0:
    sum5 = sum5+n
    n = n-1
print('总和：', sum5)

sum6 = 0
n = 1
while n <= 1000:
    sum6 = sum6+n
    n = n+1
print(sum6)

# break语句：提前结束循环
sum7 = 0
for n in range(1001):
    if n == 1000:  # 当n = 1000时，条件满足，执行break语句
        break      # break语句会结束当前循环
    sum7 = sum7+n
print('总和：', sum7)

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break   # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue语句：跳过当前的这次循环，直接开始下一次循环
sum8 = 0
for n in range(1001):
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue
    sum8 = sum8+n
print('总和：', sum8)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
