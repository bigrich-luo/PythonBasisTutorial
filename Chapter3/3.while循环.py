# 打印 1-5 的立方

# 创建一个列表
# list_num = [1, 2, 3, 4, 5]

# 获取列表的长度
# length = len(list_num)

# 初始化循环控制变量
# i = 0

# 使用while循环
# while i < length:
#     print(f'{list_num[i]}的立方是{list_num[i] ** 3}')
#     # 修改控制变量
#     i = i + 1

# 增量赋值运算符
# while i < length:
#     print(f'{list_num[i]}的立方是{list_num[i] ** 3}')
#     # 修改控制变量
#     i += 1

# 练习1:　输出 1-100中所有的奇数

# # 初始化循环控制变量
# num = 0
# while num < 100:
#     if num % 2 != 0:
#         print(num, end=' ')
#     num += 1

# 练习2:　用米粒填充国际象棋盘。在国际象棋棋盘上，第 1 格放 1 粒米，第 2 格放 2 粒米，第 3 格放 4 粒，第 4 格放 8 粒，计算 64 个格子总共可以放多少粒米。
# 初始化循环控制变量
i = 0

# 初始化米的数量
count = 0

while i < 64:
    count += 2 ** i
    i += 1
print(count)
