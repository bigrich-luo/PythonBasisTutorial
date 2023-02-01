# 打印 1, 2, 3, 4, 5的立方

# # 创建一个列表
# list_num =[1, 2, 3, 4, 5]
#
# # 使用for循环
# for num in list_num:
#     print(f'{num}的立方是{num ** 3}')


# 打印 1-100的立方
# for num in range(1, 101):
#     print(f'{num}的立方是{num ** 3}')

# 练习1: 输出 1-100中所有的奇数
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i, end=' ')

# 练习2: 用米粒填充国际象棋盘。在国际象棋棋盘上，第 1 格放 1 粒米，第 2 格放 2 粒米，第 3 格放 4 粒，第 4 格放 8 粒，计算 64 个格子总共可以放多少粒米。

# 声明变量存储米的数量
count = 0
for i in range(1, 65):
    count = count + 2 ** (i - 1)

print(count)

