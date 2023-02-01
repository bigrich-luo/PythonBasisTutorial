# 语法格式
# class MyError(Exception):
#     pass

class LengthError(Exception):

    def __init__(self):
        self.value = '名字太长'

    def __str__(self):
        return self.value


try:
    name = input('请输入一个名字：')

    if len(name) > 10:
        raise LengthError
    else:
        print(name)
except Exception as e:
    print(e)
