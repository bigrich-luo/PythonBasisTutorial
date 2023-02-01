# open()打开文件
# file = open(file='a.txt', encoding='utf-8', mode='a+')
# # 读取文件
# # content = file.read()
# # print(content)
#
# # readline()
# # content_readline = file.readline()
# # print(content_readline)
# # while 1:
# #     line = file.readline()
# #     if not line:
# #         break
# #     else:
# #         print(line)
#
# # 覆盖写入内容
# # file.write('覆盖写入新内容')
#
# # 追加写
# file.write('追加写入新内容')
#
# # 手动关闭文件
# file.close()

# 绝对路径: D:\Desktop\Python-base\Chapter8\a.txt
# 相对路径: a.txt


# with
with open('a.txt', encoding='utf-8', mode='r+') as file:
    content = file.read()
    print(content)