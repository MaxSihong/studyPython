mark = 80
if mark >= 80:
    print('优秀')
elif mark >= 60:
    print('还行，继续努力')
else:
    print('不太行哦，加油加油！')

# ------------------------------------

i = 0
while i < 3:
    print(f"当前i：{i}")
    i += 1

print(f'最终i：{i}')

for i in range(1, 6, 2):  # start stop step
    print(i)

add = 0
for i in range(1, 101):  # 1+2+3+...+100 包前不包后
    add += i
print(add)

letterStr = 'abcdefghijklmnopqrstuvwxyz'
for i in letterStr:
    if i == 'e':
        continue
    if i == 's':
        break
    print(i)


# ------------------------------------
# 编码
a = 'hello'
encodeA = a.encode()
print(a, encodeA)  # hello b'hello'
print(type(encodeA))  # <class 'bytes'> bytes, 以字节为单位进行处理
print(encodeA.decode())  # 解码 hello
print(a.encode('UTF-8'))

# ------------------------------------
# 字符串拼接
print(10 + 10, '10' + '10')
# 重复
print("加油\n" * 3)
print("加油\t" * 3)

# 成员运算符
name = 'MaxSihong'
print('max' in name)  # 区分大小写
print('max' not in name)
print('Si' in name)

# 下标 0开始 从左往右
print(name[2])
# 从右往左
print(name[-2])

# 切片 [开始:结束:步长] 包前不包后
print(name[0:3])  # Max
print(name[3:])  # Sihong

