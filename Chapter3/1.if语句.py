# # 获取一个整数
# num = int(input('请输入一个整数：'))
#
# # 判断这个数是不是正数
# if num > 0:
#     print('正数')
# elif num < 0:
#     print('负数')
# # elif num == 0:
# #     print('0')
# else:
#     print(0)

# if 语句的嵌套
# 招聘健身教练,要求: 男的身高不能低于180, 体重不能低于75kg.女生身高不能低于168, 体重不能超过75.

# # 创建三个变量用于存储用户的性别,身高,体重
# gender = input('请输入你的性别(男/女): ')
# height = int(input('请输入你的身高(cm): '))
# weight = int(input('请输入你的体重(kg): '))
#
# # 判断用户是否符合要求
# if gender == '男':
#     if height >= 180:
#         if weight >= 75:
#             print('符合要求')
#         else:
#             print('不符合要求')
#     else:
#         print('不符合要求')
# elif gender == '女':
#     if height >= 168 and weight <= 75:
#         print('符合要求')
#     else:
#         print('不符合要求')

# 练习1：要求用户输入成绩，判断用户成绩的档次并返回。85分以上是优，75分以上是良，65分以上是中，50分以上是合格，其余为挂科。

score = int(input('请输入你的成绩: '))

#　判断成绩的档次
if score >= 85:
    print('优')
elif score >= 75:
    print('良')
elif score >= 65:
    print('中')
elif score >= 50:
    print('及格')
else:
    print('挂科')