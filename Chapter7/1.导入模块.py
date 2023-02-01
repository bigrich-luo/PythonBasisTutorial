# 导入 math 模块
# 使用 import 语句导入 math 模块
# import math
#
# # 使用 math模块
# print(math.pi)
# print(math.sin(math.pi / 2))

# import 模块 as 别名
# import math as m
#
# print(m.pi)
# print(m.sin(m.pi / 2))

# from 模块名 import *
# from math import *
#
# print(pi)
# print(sin(pi/2))

# from 模块名 import 功能名
from math import pi, sin

print(pi)
print(sin(pi / 2))

# from 模块名 import 功能名 as 别名
from math import pi as p
from math import sin as s
print(p)
print(s(p / 2))