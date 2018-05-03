# #打印包含嵌套和不嵌套的列表
# # def print_lol(the_list,indent = False, level=0):
# #         for each_item in the_list:
# #             #如果列表本身是一个列表，递归调用函数
# #             if isinstance(each_item,list):
# #                 print_lol(each_item,indent,level + 1)
# #             else:
# #                 if indent:
# #                     for tab_stop in range(level):
# #                         print("\t",end= '')
# #                 print(each_item)
# #
# # import pickle
# # from helloworld import AthleteList
# #
# # def get_coach_data(filename):
# #    ''' not shom '''
# #
# #
# # def put_to_store(file_list):
# #     all_athletes = {}
# #     for each_file in file_list:
# #         ath = get_coach_data(each_file)
# #         all_athletes[ath.name] = ath

from numpy import *

randMat = mat(random.rand(4, 4))
invRandMat = randMat.I

print(randMat, invRandMat)

print(randMat * invRandMat)
