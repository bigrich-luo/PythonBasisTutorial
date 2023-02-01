# 创建元组

# # 创建一个空元组
# tuple_a = ()
# tuple_b = tuple()
# print(f'a 的值为{tuple_a}, 数据类型是{type(tuple_a)}')
# print(f'b 的值为{tuple_b}, 数据类型是{type(tuple_b)}')
#
# # 创建一个只有一个元素的元组
# tuple_c = (1)
# tuple_d = (1, )
# print(f'c 的值为{tuple_c}, 数据类型是{type(tuple_c)}')
# print(f'd 的值为{tuple_d}, 数据类型是{type(tuple_d)}')

# 访问元组中的元素
tuple_e = (1, 2, 3, 4, 5)
# print(tuple_e)

# # 访问元组中第一个元素
# print(tuple_e[0])
# print(tuple_e[-1])
#
# # 访问多个元素
# print(tuple_e[1:3])
#
# # len()
# print(len(tuple_e))

# 修改元组中的元素
# tuple_e[1] = 0
# print(tuple_e)
# tuple_e = list(tuple_e)
# print(f'e的值为: {tuple_e}, 数据类型是{type(tuple_e)}')
# tuple_e[1] = 0
# print(tuple_e)
# tuple_e = tuple(tuple_e)
# print(f'e的值为: {tuple_e}, 数据类型是{type(tuple_e)}')

# 元组的操作函数
tuple_f = (2, 4, 6, 87, 2, 3)
# count()
print(tuple_f.count(2))

# index()
print(tuple_f.index(87))
