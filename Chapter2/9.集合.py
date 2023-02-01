# 创建一个空集合
set_a = set()
# print(f'a: {set_a}, 数据类型是{type(set_a)}')

# 创建一个拥有重复元素的集合
set_b = {1, 2, 3, 4, 4}
# print(set_b)

# 添加元素
set_b.add(5)
print(set_b)

# 合并两个集合
set_c = {6, 7, 8}
set_b.update(set_c)
print(set_b)

# 删除集合中的元素
set_b.remove(8)
print(set_b)
set_b.discard(8)
print(set_b)
# set_b.remove(8)
# print(set_b)

# len
print(len(set_b))