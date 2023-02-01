# 继承

# 私有属性
# class Dog:
#
#     # 设置私有属性
#     __legs = 4
#
#     # 内部获取狗腿数量
#     def print_legs_count(self):
#         print(f'狗有{self.__legs}条腿')
#
#
# # 实例化我的小狗
# my_dog = Dog()
# my_dog.print_legs_count()


# 私有方法
# class Dog:
#
#     # 设置私有属性
#     __legs = 4
#
#     # 内部获取狗腿数量
#     def __print_legs_count(self):
#         print(f'狗有{self.__legs}条腿')
#
#     def print_legs_count_outside(self):
#         self.__print_legs_count()
#
#
# # 实例化一个对象
# your_dog = Dog()
# your_dog.print_legs_count_outside()


# set与get方法

class Dog:
    __legs = 4

    # get方法
    def get_legs(self):
        return self.__legs

    # set方法
    def set_legs(self, legs):
        self.__legs = legs


# 实例化一个对象
my_dog = Dog()
print(my_dog.get_legs())
my_dog.set_legs(2)
print(my_dog.get_legs())
