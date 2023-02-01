# # 创建列表
#
# # 创建一个空列表
# list_a = []
# list_b = list()
# # print(f'a 的值为: {list_a}, 数据类型为: {type(list_a)}')
# # print(f'b 的值为: {list_b}, 数据类型为: {type(list_b)}')
#
# # 创建只有一个元素的列表
# list_c = [1]
# print(list_c)
# # list_c = [1, ]
# # print(list_c)
#
# # 创建一个拥有多个元素的列表
# list_d = [1, 2, 3, 4, 5]
# print(list_d)
# list_e = ['a', 1, 2.2, [1, 2, 3]]
# print(list_e)
#
# # 创建一个二维列表
# list_f = [[1, 2], [3, 4], [5, 6]]
# print(list_f)

# 访问列表中的元素

# # 访问 list_d 中的第一个元素
# print(list_d[0])
# # 访问 list_d 中的第三个元素
# print(list_d[2])
# # 访问 list_d 中的最后一个元素
# print(list_d[4])
# print(list_d[-1])
# # len()
# print(f'列表list_d长度为: {len(list_d)}')
# print(list_d[len(list_d) - 1])

# 列表的运算
# 加法
# list_g = list_c + list_d
# print(list_g)
# # 乘法
# list_h = list_c * 3
# print(list_h)


# 列表操作函数
# 创建一个列表
list_i = [1, 2, 3, 4, 5]
print(list_i)
# 列表尾部追加元素 1
list_i.append(1)
print(list_i)

# 统计 1 在列表中出现的次数
print(list_i.count(1))

# 列表后追加另一个列表所有元素
list_i.extend([8, 2, 4])
print(list_i)

# 元素 2 在列表中首次出现的序号
print(list_i.index(2))

# 在序号 3 处插入元素 0
list_i.insert(3, 0)
print(list_i)

# 返回并删除列表最后一个元素
print(list_i.pop())
print(list_i)

# 删除列表中的元素 1（仅删除第一个）
list_i.remove(1)
print(list_i)
# 列表内元素顺序颠倒
list_i.reverse()
print(list_i)
# 对列表元素排序
list_i.sort()
print(list_i)
