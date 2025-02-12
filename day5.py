# 列表
nameList = ['张三', '李四', '王五', '赵六']
print(nameList)
print(nameList[1:3])
for i in range(0, len(nameList)):
    print(f'{i}-{nameList[i]}')

# 添加元素
nameList.append('san')  # 往后加
nameList.extend('si')  # 分散加  ['张三', '李四', '王五', '赵六', 'san', 's', 'i']
nameList.insert(1, '指定')  # 指定位置加，如果有元素，原有元素就会往后移
print(nameList)
# 修改元素
nameList[6] = 'si'
print(nameList)
# 查询
print('si' in nameList)
print('si' not in nameList)

# test 注册昵称，昵称不可重复
# nameList = ['max', 'gem', 'libai', 'chen']
# while True:
#     registerName = input('请输入昵称：')
#     if registerName in nameList:
#         print(f"您输入的昵称:{registerName}已被注册，请重新输入~")
#     else:
#         nameList.append(registerName)
#         print(f"注册成功！！")
#         print(nameList)
#         break

# 删除
# del nameList  # 删除列表
del nameList[0]
print(nameList)
nameList.pop()  # 默认删除最后一个元素
print(nameList)
nameList.pop(0)  # 删除指定下表元素
print(nameList)
# 删除指定值
nameList.remove('si')  # 默认删除最开始出现的指定元素，如果列表不存在这个元素则会报错
print(nameList)

# 排序
sortList = [4, 2, 1, 5, 3]
sortList.sort()  # 从小到大排序
print(sortList)  # [1, 2, 3, 4, 5]
sortList.reverse()  # 将列表反转过来，并非排序，如果先sort再reverse则能实现从大到小排序
print(sortList)  # [5, 4, 3, 2, 1]
sortListV2 = [4, 2, 1, 5, 3]
sortListV2.reverse()
print(sortListV2)  # [3, 5, 1, 2, 4]

# 列表推到式
li = []
[li.append(i) for i in range(1, 11) if i % 2 == 1]
print(li)

