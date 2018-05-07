# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 20:05
# @Author  : shihao
# @Email   : chensh@udcredit.com
# @File    : test05.py
# @Software: PyCharm

from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import numpy as np
import pydotplus
import pandas as pd

'''
原始数据->字典->pandas数据
'''

if __name__ == '__main__':
    with open('lenses.txt', 'r') as fr:  # 加载文件
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]  # 处理文件
    lenses_target = []  # 提取每组数据的类别，保存在列表里
    for each in lenses:
        lenses_target.append(each[-1])

    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']  # 特征标签
    lenses_list = []  # 保存lenses数据的临时列表
    lenses_dict = {}  # 保存lenses数据的字典，用于生成pandas
    for each_label in lensesLabels:  # 提取信息，生成字典
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
   # print(lenses_dict)  # 打印字典信息
    lenses_pd = pd.DataFrame(lenses_dict)  # 生成pandas.DataFrame
  #  print(lenses_pd)
    #创建序列化对象
    le = LabelEncoder()
    for col in lenses_pd.columns:
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    #构建决策树
    clf = tree.DecisionTreeClassifier(max_depth= 4)
    clf = clf.fit(lenses_pd.values.tolist(),lenses_target)
    dot_data = StringIO()
    tree.export_graphviz(clf,out_file = dot_data,
                         feature_names=lenses_pd.keys(),
                         class_names=clf.classes_,
                         filled = True,
                         rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("tree.pdf")

    print(clf.predict([[1, 1, 1, 0]]))  # 预测