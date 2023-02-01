# 类的属性
class Dog:
    # 狗子共有的特征
    legs = 4
    eyes = 2


# 实例化两个对象
my_dog = Dog()
your_dog = Dog()

print('==========获取狗的公共属性============')
print(f'我的狗的腿有: {my_dog.legs}, 眼睛有: {my_dog.eyes}')
print(f'你的狗的腿有: {your_dog.legs}, 眼睛有: {your_dog.eyes}')

# 添加示例属性
my_dog.name = '旺财'
my_dog.color = '白色'
my_dog.weight = 10

your_dog.weight = 5
your_dog.color = '黑色'
your_dog.age = 4
print('=======获取不同的实例属性==========')
print(f'我的狗的特征: 重: {my_dog.weight}, 颜色: {my_dog.color}, 名字叫: {my_dog.name}')
print(f'你的狗的特征: 重: {your_dog.weight}, 颜色: {your_dog.color}, 年龄是: {your_dog.age}')
# print(my_dog.age)

# 修改类的属性
Dog.legs = 2

print('=============打印修改之后的类的公共属性=============')
print(my_dog.legs, your_dog.legs)

# 修改实例属性
my_dog.legs = 1
print(f'我的狗腿数为: {my_dog.legs}, 你的狗腿数为: {your_dog.legs}, 狗类的腿数为: {Dog.legs}')