# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 18:02
# @Author  : shihao
# @Email   : chensh@udcredit.com
# @File    : test04.py
# @Software: PyCharm

from mpmath import log
from Ch03X import test
from Ch03X import test03
import operator
import pickle

'''
使用决策树分类
Parameters:
    inputTree - 已经生成的决策树
    featLabels - 存储选择的最优特征标签
    testVec - 测试数据列表，顺序对应最优特征标签
Returns:
    classLabel - 分类结果
'''


def classify(inputTree, featLabels, testVec):
    firstStr = next(iter(inputTree))
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


'''
    函数说明:存储决策树

Parameters:
    inputTree - 已经生成的决策树
    filename - 决策树的存储文件名
Returns:
    无
'''
def storeTree(inputTree,filename):
    with open (filename,'wb') as fw:
        pickle.dump(inputTree, fw)


def grabTree(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)

if __name__ == '__main__':
    # dataSet, labels = test.createDataSet()
    # featLabels = []
    # myTree = test03.createTree(dataSet, labels, featLabels)
    # testVec = [0,1]                                        #测试数据
    # result = classify(myTree, featLabels, testVec)
    # if result == 'yes':
    #     print('放贷')
    # if result == 'no':
    #     print('不放贷')
    # myTree = {'有自己的房子': {0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
    # storeTree(myTree,'classifierStorage.txt')
    myTree = grabTree('classifierStorage.txt')
    print(myTree)