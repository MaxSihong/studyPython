# 元组 名称 = (元素1, 元素2)
element = (1, 2, 'a', 'b', 3)
print(element)
aa = (2,)  # 只有一个元素必须加上逗号，否则返回唯一的值的数据类型
bb = (2)
print(type(aa))  # <class 'tuple'>
print(type(bb))  # <class 'int'>

# 元组只支持查询操作，不支持增删改
print(element[1])

#  字典 key必须唯一，重复不会报错前面的值会被后面的覆盖
dictionary = {'name': 'max', 'age': 25, 'ext': {'e1': 'isA', 'e2': 'isB'}}
print(type(dictionary))
print(dictionary['name'])
print(dictionary.get('name'))
print(dictionary.get('aa', '不存在'))  # 如果不存在则返回自己设置的默认值
# 修改
dictionary['age'] = 18
print(dictionary)
# 删除指定的键值对，key不存在就会报错
del dictionary['ext']
dictionary.pop('age')
dictionary.popitem()  # 3.7之前的版本是随机删除一个，3.7之后是默认删除最后一个
print(dictionary)
# 清空整个字典内容
dictionary.clear()
print(dictionary)
# 删除 del 删除整个字典
del dictionary

dictionary = {'new': 'nameMax', 'tel': '123'}
print(len(dictionary))  # 长度
print(dictionary.keys())  # 获取所有key dict_keys(['new', 'tel'])
print(dictionary.values())  # 获取所有值 dict_values(['nameMax', '123'])
print(dictionary.items())  # 返回所有的键值对 元组的形式  dict_items([('new', 'nameMax'), ('tel', '123')])

# 集合，具有无序性，重复的会去除，无限性不能修改集合中的值  name = {元素1, 元素2}
# s1 = set()  # 定义空集合
s1 = {3, 2, 1, 5, 4, 1}  # 每次运行的结果都一样  {1, 2, 3, 4, 5}
print(s1)
s2 = {'a', 'c', 'd', 'd'}  # 每次运行的结果都不一样
print(s2)
# 集合无序的实现方式涉及hash表，每次运行结果的不同，hash值不同，那么位置也不同
# python 中 int 整型的hash值就是他本身，所以在hash表中不发生改变，然如果用引号括起来实际也是变成了字符串，所以也会改变
print(hash('a'))
print(hash('b'))
print(hash('c'))
# 集合只能添加和删除，不能查询因为是无序的。如果需要添加的元素在远集合存在，那么就不进行任何操作
s2.add('bbb')
print(s2)
# update 把传入的元素拆分，一个个放进集合中
s2.update('xih')  # {'d', 'c', 'bbb', 'x', 'i', 'h', 'a'}
print(s2)
s2.update(('qq', 'le'))  # 元素必须是能够被for循环取代的可迭代对象
print(s2)
# 删除
s2.remove('c')  # 如果有则删除，没有则报错
print('s2')
s2.pop()
print(s2)  # 默认删除根据hash表排序后的第一个元素
s2.discard('x')  # 没有要删除的内容，也不会报错
print(s2)

# 交集(&)和并集(|)
# 交集
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)  # {3, 4}
print(a | b)  # {1, 2, 3, 4, 5, 6}  所有的都放一起，重复的不算（集合的唯一性）
