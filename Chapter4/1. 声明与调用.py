# 示例函数
def hello():
    """显示问候语"""
    print('Hello')


# hello()


# 有参数的函数
def hello_user(name):
    print(f'Hello, {name}')


# hello_user('梨花')
# hello_user('韩梅梅')


# 返回值
# 定义一个两数相加的函数
# def sum(a, b):
#     result = a + b
#     return result
#
#
# r = sum(1, 3)
# print(r)


# 函数的注释
def sum(a, b):
    """
    这是一个对两数求和的函数
    :param a: 求和的其中一个值
    :param b: 求和的另一个值
    :return: 两数和
    """
    result = a + b
    return result
