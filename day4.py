# find 查找字符串内字符的下表，没有-1
name = 'namename'
print(name.find('a'))
print(name.find('x'))
print(name.find('n', 3))  # 3开始找
print(name.find('n', 3, 5))  # 3到5范围开始找

# index 同上，只是未找到会报错，而find会返回-1
# print(name.index('xx'))

# count 返回某个字符串出现的次数
print(name.count('n'))
# startswith 是否以某个字符开头
print(name.startswith('n'))
print(name.startswith('a'))
# endswith 是否以某个字符结尾
print(name.endswith('e'))
print(name.endswith('a'))

#  replace(旧内容, 新内容, 替换次数-默认全部替换)
name = name.replace('n', 'x')
print(name)
name = name.replace('x', 'n', 1)
print(name)

# split 分割
splStr = 'hello,max'
print(splStr.split(','))

# capitalize 第一个字符大写，其他都转为小写
print(splStr.capitalize())
print('AAAAA'.capitalize())
# lower 大写字母转为小写
print('BBBBB'.lower())
# upper 小写字母转为大写
print('ccccc'.upper())

