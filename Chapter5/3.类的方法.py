# 类的方法
# class Dog:
#
#     def sleep(self):
#         print('睡觉')
#
#     def eat(self, food):
#         print(f'吃{food}')
#
#
# # 实例化
# my_dog = Dog()
#
# # 调用类中的方法
# my_dog.sleep()
# my_dog.eat('骨头')


# __init__() 方法
class Dog:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print('睡觉')

    def eat(self, food):
        print(f'吃{food}')

    def speak(self):
        print(f'这条狗的名字是: {self.name}')

# 实例化
my_dog = Dog('旺财')
my_dog.speak()

your_dog = Dog('小黑')
your_dog.speak()