# raise
# 要求用户输入的名字不能超过10个字符
# name = input('请输入你的名字: ')
#
# try:
#     if len(name) > 10:
#         raise NameError
#     else:
#         print(name)
# except Exception as e:
#     print('捕获到了异常')
#
# print('程序执行结束')


# assert
name = input('请输入你的名字: ')

assert len(name) < 10, '名字太长'
print('程序执行结束')
