# -*- coding: UTF-8 -*-
from mpmath import log

'''
    得到数据集
    年龄：0代表青年，1代表中年，2代表老年；
    有工作：0代表否，1代表是；
    有自己的房子：0代表否，1代表是；
    信贷情况：0代表一般，1代表好，2代表非常好；
    类别(是否给贷款)：no代表否，yes代表是。
'''

#functions

def createDataSet():
    dataSet = [[0, 0, 0, 0, 'no'],  # 数据集
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    labels = ['age', 'work', 'house', 'credit']
    return dataSet, labels


'''
计算给定数据集的经验熵(香农熵)

Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)
    
    公式： H(D) = -∑ p(xi)log2p(xi)
    求和公式得到所有期望值
    
'''


def calcShannonEnt(dataSet):
    # 得到数据集的行数
    numEntries = len(dataSet)
    labelCounts = {}
    for x in dataSet:
        # 获得标签信息
        currentLabel = x[-1]
        # 标签不在字典中 就添加进去
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    # 计算香农熵
    for key in labelCounts:
        # 选择该标签的概率
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


'''
    按照给定的特征划分数据集
    
 dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
'''


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 去掉axis特征
            reduceFeatVec = featVec[:axis]
            # 将符合条件的添加到返回的数据集中
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


'''
    选取最优特征
    dataSet -数据集
'''

'''
    选择最优特征
    dataSet - 数据集
returns:
    bestFeature - 信息增益最大的(最优）特征的索引值    
    
    信息增益公式：信息增益  =  信息熵 - 该特征下的条件熵 

'''

#functions
def chooseBestFeatureTopSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 获取dataSet 的第i个所有特征
        featList = [example[i] for example in dataSet]
        # 经验条件熵
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # subDataSet划分后的子集
            subDataSet = splitDataSet(dataSet, i, value)
            # 计算子集的概率
            prob = len(subDataSet) / float(len(dataSet))
            # 根据公式计算经验条件熵
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        print("第%d个特征的增益为%.3f" % (i, infoGain))
        if (infoGain > bestInfoGain):
            #更新信息增益，找到最大的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


if __name__ == '__main__':
    dataSet, features = createDataSet()
    print("最优特征索引值：" + str(chooseBestFeatureTopSplit(dataSet)))
