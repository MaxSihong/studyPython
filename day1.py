print('Hello maxsihong')
print('Hello maxsihong2')
print('Hello maxsihong3')
print('Hello maxsihong4')

# 输出多句话
print('this is one', 'this is two', 'this is three')
# 设置多句话的分割，默认空格
print('this is one', 'this is two', 'this is three', sep='|')
# 设置结束，默认\n换行
print('setEnd', end='')
print('frontNotHasEnd')

# -------------------------

bookPrice = 100.00
eggPrice = 2.00
testFlow = 2.88888668
age = 8

print('书价格：%s' % bookPrice, '鸡蛋价格%s' % eggPrice)
print('书价格：%s，鸡蛋价格%s' % (bookPrice, eggPrice))
print(f"书价格：{bookPrice}，鸡蛋价格{eggPrice}")
print('年龄：%d' % age)
# 默认小数6位，超过则四舍五入
print('书价格：%f，鸡蛋价格%f' % (bookPrice, eggPrice))
print('testFlow %f' % testFlow)
print('testFlow %.2f' % testFlow)
print('bookPrice %.2f' % bookPrice)
# 位数8用0补全，超过则原样输出
no = 8
print('%08d' % no)
