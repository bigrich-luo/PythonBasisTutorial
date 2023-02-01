# 异常示例
# print(1 / 0)
# print('下一行代码执行了')

# 捕获异常
# try:
#     # print(1 / 0)
#     print(1)
#     # print('下一行代码执行了')
# except:
#     print('捕获到了异常')
#
# print('下一行代码执行了')

# else finally 关键字
# try:
#     print(1 / 0)
#     # print(1)
# except:
#     print('捕获到了异常')
# else:
#     print('未发现异常')
# finally:
#     print('异常捕获执行结束')
#
# print('下一行代码执行了')


# except 的主要用法
try:
    # print(1 / 0)
    # printt()
    print('a' - 'b')
    # print(1)
# 捕获所有异常
# except:
#     print('捕获到了异常')
# 捕获指定异常
# except ZeroDivisionError:
#     print('捕获了0为除数的异常')
# as 关键字替代值
except ZeroDivisionError as e:
    print(e)
# 捕获多个异常
# except (ZeroDivisionError, NameError):
#     print('捕获到了异常')
except Exception as e:
    print(e)