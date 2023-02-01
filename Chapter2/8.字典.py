# # 创建字典
#
# # 创建一个空字典
# dict_a = {}
# dict_b = dict()
# # print(f'a: {dict_a}, 数据类型为: {type(dict_a)}')
# # print(f'b: {dict_b}, 数据类型为: {type(dict_b)}')
#
# # 创建一个有多个元素的字典
# dict_c = {'a': 1, 'b': 2, 'c': 3}
# dict_d = {1: 'a', 'b': 2.2, 3: [1, 2, 4], 3.3: (1 ,2, 4)}
# # print(dict_c)
# # print(dict_d)
#
# # 通过键名查询字典中的值
# print(dict_c['a'])
#
# # 通过键名修改字典中的值
# dict_c['a'] = 0
# print(dict_c)

# 字典的操作函数
dict_e = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict_e)
# # get
# print(dict_e.get('e', '不存在'))
# # print(dict_e['e'])
#
# # 删除键值对
# dict_e.pop('a')
# print(dict_e)
# # del 关键字
# del dict_e['b']
# print(dict_e)
#
# # 更新键值对
# dict_e.update({'b': 3})
# print(dict_e)
#
# # 清空字典
# dict_e.clear()
# print(dict_e)

# 复制字典
dict_f = dict_e
print(f'f: {dict_f}, e: {dict_e}')
dict_f['a'] = 0
print(f'f: {dict_f}, e: {dict_e}')

dict_g = dict_e.copy()
print(f'g: {dict_g}, e: {dict_e}')
dict_g['a'] = 2
print(f'g: {dict_g}, e: {dict_e}')


