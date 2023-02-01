import os

# 获取工作目录
print(os.getcwd())

# 获取当前目录下的所有内容
print(os.listdir(os.getcwd()))

# 创建一个文件夹
# os.mkdir('D:\\Desktop\\测试文件夹')

# 删除文件夹
os.rmdir('D:\\Desktop\\测试文件夹')