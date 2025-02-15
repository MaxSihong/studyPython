import copy

# 类型转换
# int() 转换证书，只能转由纯数字组成的字符串

print(int('1'))
print(int('12'))
# print(int('12.2'))  # 无法转换，报错
print(int(1.2))  # 1
print(int('+10'))  # 10
print(int('-10'))  # -10

# float() 小数
print(float(11))  # 11.0
print(float(-11))  # -11.0

# str() 字符串，任何类型都可以转换字符串
print(str(10))  # 10
print(str(True))  # True
print(str(-1.00))  # -1.0
print(str(-1.002))  # -1.002

# eval() 执行字符串表的是，并返回表达式的值
print(10 + 10)  # 20
print('10' + '10')  # 1010
print(eval('10+10'))  # 20
# str -> list
st1 = '[[1,2], [3,4], [5,6]]'
print(type(st1))  # str
li = eval(st1)
print(li, type(li))  # [[1, 2], [3, 4], [5, 6]] <class 'list'>
# str -> dict
st2 = "{'name':'max','age':18}"
dic = eval(st2)
print(dic, type(dic))  # {'name': 'max', 'age': 18} <class 'dict'>

# list() 将可迭代对象转换成列表
# 支持转换list的类型：str、tuple、dict、set
print(list('abcd'))  # ['a', 'b', 'c', 'd']
# tuple -> llist
print(list((1, 2, 3, 4, 5)))  # [1, 2, 3, 4, 5]
# dict -> list 字典转换成列表，会取键名作为列表的值
print(list({'name': 'max', 'age': 18}))  # ['name', 'age']
# set -> list 集合转换成列表，会先去重
print(list({'a', 'b', 'c', 'b'}))  # ['a', 'c', 'b']

# -------------------------

# 深浅拷贝
li = [1, 2, 3, 4]
li2 = li
print('li', li)  # [1, 2, 3, 4]
print('li2', li2)  # [1, 2, 3, 4]
li.append(5)
print('新增后li', li)  # [1, 2, 3, 4，5]
print('新增后li2', li2)  # [1, 2, 3, 4，5]
# 复制等于完全共享资源，一个值的改变会完全改变另一个共享（类似内存地址赋值过去了，内存地址是一样的）
# 浅拷贝 会创建新的对象，拷贝第一次的数据，嵌套曾会指向原来的内存地址（半拷贝）
li = [1, 2, 3, [4, 5, 6]]
li2 = copy.copy(li)  # 选哟引用 copy  import copy
print('li内存地址：', id(li))  # 2001739239808
print('li2内存地址：', id(li2))  # 2001741818624
li.append(888)
print('新增后li', li)  # 新增后li [1, 2, 3, [4, 5, 6], 888]
print('新增后li2', li2)  # 新增后li2 [1, 2, 3, [4, 5, 6]]
li[3].append(8)  # 两个嵌套的都新增了，嵌套曾的内存地址是一致的
print('新增后li', li)  # 新增后li [1, 2, 3, [4, 5, 6, 8], 888]
print('新增后li2', li2)  # 新增后li2 [1, 2, 3, [4, 5, 6, 8]]

# 深拷贝 （数据完全不共享
li = [1, 2, 3, [4, 5, 6]]
li2 = copy.deepcopy(li)
print('li内存地址：', id(li))  # 2611630583744
print('li2内存地址：', id(li2))  # 2611628331392
li[3].append(8)  # 两个嵌套的都新增了，嵌套曾的内存地址是一致的
print('新增后li', li)  # 新增后li [1, 2, 3, [4, 5, 6, 8]]
print('新增后li2', li2)  # 新增后li2 [1, 2, 3, [4, 5, 6]]
