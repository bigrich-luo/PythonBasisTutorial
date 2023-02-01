# 参数值传递

# def demo(obj):
#     obj += obj
#     print('形参值为:', obj)
#
#
# a = 'Python YYDS'
# print('a的值为:', a)
# demo(a)
# print('实参值为:', a)


# 位置参数
# 计算矩形的面积
# def area(width, length):
#     print(f'宽度为: {width}, 长度为: {length}, 面积为: {width * length}')
#     return width * length
#
#
# area(2, 4)


# 关键字参数

# 创建一个矩形面积函数，打印宽和长
def area(width, length):
    print(f'宽为: {width}, 长为: {length}')


# 位置传参
# area(12, 16)
# area(16, 12)
#
# area(width=12, length=16)
# area(length=16, width=12)
#
# # 混合传参
# area(12, length=16)


# 默认值参数
# def hello(name='Python'):
#     print(f'Hello, {name}')
#
#
# hello()
# hello('PyCharm')

# 两数求和
## 错误写法
# def sum(a=10, b):
#     return a + b

# def sum(a, b=10):
#     return a + b
#
# print(sum(1))
# print(sum(1, 2))


# 可变数量传参
def function(*args):
    print(f'args: {args}, 类型为: {type(args)}')


# function(1, 2, 3)

# 多种参数混合使用
# def function_2(*args, param_1, param_2='默认值'):
#     print(f'args: {args}, param_1: {param_1}, param_2: {param_2}')
#
# # 正确的示范
# function_2(1, 2, 3, param_1=4)
#
# # 错误的示范
# function_2(1, 2, 3, 4)

# 收集不定长的关键字参数
def function_3(**kwargs):
    print(f'kwargs: {kwargs}, 数据类型为{type(kwargs)}')


# function_3(a=1, b=2, c=4, d='a')

# 方块函数
def cube(name, **features):
    print(f'==========={name}方块的特征================')
    print(f'体积为: {features["length"] * features["width"] * features["height"]}')
    print(f'质量为: {features["mass"]}')
    print(f'颜色为: {features["color"]}')


# cube('a', length=1, width=2, height=3, mass=4, color='黄色')
cube(length=1, width=2, height=3, mass=4, color='黄色', name='a')