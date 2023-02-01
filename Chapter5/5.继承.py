# 继承示例
# class Animal:
#     name = '动物'
#
#     def sleep(self):
#         print('动物需要睡觉')
#
#
# class Dog(Animal):
#     pass
#
#
# # 实例化对象
# my_dog = Dog()
# print(my_dog.name)
# my_dog.sleep()


# 重载
# class Animal:
#     name = '动物'
#
#     def sleep(self):
#         print('动物需要睡觉')
#
#
# class Dog(Animal):
#     name = '狗'
#
#     def sleep(self):
#         print('狗需要睡觉')
#
#
# # 实例化对象
# my_dog = Dog()
# print(my_dog.name)
# my_dog.sleep()


# super()
# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#
#     # 重写父类方法
#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age
#
#     # super()
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#
# # 实例化
# my_dog = Dog('旺财', 4)
# print(my_dog.name, my_dog.age)


# 多继承
# 语法格式
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A, B):
#     pass

class Dog:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f'狗的名字叫: {self.name}')

    def run(self):
        print('狗跑的很快')


class Husky:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f'哈士奇的名字叫: {self.name}')

    def run(self):
        print('哈士奇跑得慢')

    def sofa(self):
        print('哈士奇咬沙发')


class MyDog(Dog, Husky):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_info(self):
        print(f'MyDog的名字叫: {self.name}')


# 实例化MyDog
my_dog = MyDog('旺财', 4)
# 继承狗类
my_dog.run()
# 继承哈士奇类
my_dog.sofa()
#
my_dog.show_info()