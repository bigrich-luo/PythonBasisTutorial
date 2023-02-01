# # 声明一个列表
# list_num = [1, 2, 3, 4, 5]
#
# # break
# # 如果发现3, 则停止循环
# for num in list_num:
#     if num == 3:
#         break
#     else:
#         print(num, end=' ')
#
# print()
#
# # continue
# # 如果我们发现元素3, 则跳过本轮循环
# for num in list_num:
#     if num == 3:
#         continue
#     else:
#         print(num, end=' ')

# 遍历字典
dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# 遍历字典中的键
# for key in dict_a:
#     print(key)

# keys()函数
# for key in dict_a.keys():
#     print(key)

# 获取字典中的值
# for key in dict_a:
#     print(dict_a[key])

# values()函数
# for value in dict_a.values():
#     print(value)

# items()函数
# for key, value in dict_a.items():
#     print(f'key: {key}, value: {value}')


# 嵌套循环
# for i in range(10):
#     for j in range(1, 6):
#         print(j, end=' ')
#     print()

# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i*j}', end='\t')
    print()