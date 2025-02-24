def sayHello():
    print('hello')


sayHello()


def buy():
    return '买了一瓶可口可乐'


print(buy())


def add(num1, num2):
    return num1 + num2


print(add(1, 2))


def defaultVal(de=1):
    print(de)


defaultVal()


# 可变参数
def funA(*args):
    print(args)


funA(1, 2, 3, 4, 5)


# 关键字参数
def funB(**args):
    print(args)


funB(name='max', age=23)


# 嵌套定义
def study():
    print('学习ing')

    def course():
        print('python')

    course()


study()
