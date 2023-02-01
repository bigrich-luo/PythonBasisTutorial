# 字符串的不同表示方法
# print('你好')
# print("你好")
# print('''
#     上的法大师傅撒打发撒旦飞洒范德萨发撒法
#     法撒旦飞洒地方撒旦飞洒地方
#     阿斯蒂芬撒地方
# ''')
# print("""
#     fadsfsdaf
#     sdfsdf
#
#     sdfdsf
# """)

# # 字符串运算
# # 字符串的加法
# string_1 = '你好'
# string_2 = 'PyCharm'
#
# print(string_1 + string_2)
#
# # 字符串的乘法
# string_3 = 'hello'
# print(string_3 * 3)

# # 转义字符串
# print('你好')
# print('\n你好')
# print('\\')
# print('\'')
# print("'")
# print("\"")

# print('\\\\')

# 原始字符串
# print('\\\\')
# print(R'\\\\')
# print(r'\\\\')

# 格式化字符串

# 使用占位符

# %s
# name = '梨花'
# print('我的名字叫%s' % name)
#
# age = 12
# print('我的名字叫%s, 今年%s岁' % (name, age))

# %d
# number_int = 18
# number_float = 17.6
# print('number_int的值为: %d, number_float的值为 %d' % (number_int, number_float))
#
# # %f
# print('number_int的值为: %f, number_float的值为 %f' % (number_int, number_float))
# print('number_int的值为: %.1f, number_float的值为 %.2f' % (number_int, number_float))
#
# percent = 91
# print('任务当前完成了%d%%' % percent)


# format 方法

# 1. 默认方法
# print('{}在{}玩了一天的{}'.format('小明', '网吧', 'LOL'))
# print('{}在{}玩了一天的{}'.format('LOL', '网吧', '小明'))

# 2. 设置关键字
# print('{name}在{place}玩了一天的{game}'.format(game='LOL', place='网吧', name='小明'))
# print('{name}在{place}玩了一天的{game}'.format(place='网吧', game='LOL', name='小明'))

# 3. 设置指定位置
# print('{2}在{1}玩了一天的{0}'.format('LOL', '网吧', '小明'))

# f-string
# name = '小明'
# place = '网吧'
# game = 'LOL'
# print(f'{name}在{place}玩了一天的{game}')


# num_1 = int(input('请输入第一个整数: '))
# num_2 = int(input('请输入第二个整数: '))
# print(f'num_1 与 num_2的和为{num_1 + num_2}, 差为{num_1 - num_2}, 积为{num_1 * num_2}, 商为{num_1 / num_2}')

# 字符串处理函数
# string_a = 'hello,worlD'
#
# # len()
# print(len(string_a))
#
# # count()函数
# print(string_a.count('o'))
#
# # upper()
# string_a_upper = string_a.upper()
# print(string_a_upper)
#
# # isupper()
# print(string_a_upper.isupper())
# print(string_a.isupper())
#
# # split()
# string_1, string_2 = string_a_upper.split(',')
# print(string_1)
# print(string_2)


# 练习题
# 1. 要求用户输入两个数，并依次返回给用户两个数的加减乘除的结果。

# num_1 = int(input('请输入第一个整数: '))
# num_2 = int(input('请输入第二个整数: '))
# # 格式化输出
# print(f'num_1 与 num_2 的和为{num_1+num_2}, 差为{num_1-num_2}, 积为{num_1*num_2}, 商为{num_1 / num_2}')

# 2. 敏感词过滤程序
# 通过用户输入一段文本，识别 '性', '爆炸'
string_input = input('请输入你要过滤的文本:　')
# 使用replace函数对文本进行替换
new_string = string_input.replace('性', '*').replace('爆炸', '**')

print(new_string)