# import test_module_1, test_module_2
#
# print(test_module_1.test_name)
# test_module_1.test_function()
#
# test_module_2.test_function()
#
# from test_module_1 import test_name
# from test_module_2 import test_name
#
# print(test_name)


# 模块位置
# sys.path.append(‘自定义模块目录名’)
# import sys
#
# print(sys.path)
#
# sys.path.append(r'D:\Desktop\Python-base\Chapter7\module_dir')
#
# import test_module_3
# test_module_3.test_function()


from module_dir import test_module_3

print(test_module_3.test_name)
