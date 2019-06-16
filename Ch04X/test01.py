# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 23:25
# @Author  : shihao
# @Email   : chensh@udcredit.com
# @File    : test01.py
# @Software: PyCharm
import numpy as np
from functools import reduce

'''
朴素贝叶斯算法实现

'''

'''
创建实验样本

Parameters:
    无
Returns:
    postingList - 实验样本切分的词条
    classVec - 类别标签向量
'''


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


'''
根据vocabList词汇表，将inputSet向量化，向量的每个元素为1或0

Parameters:
    vocabList - createVocabList返回的列表
    inputSet - 切分的词条列表
Returns:
    returnVec - 文档向量,词集模型
'''


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
    for word in inputSet:  # 遍历每个词条
        if word in vocabList:  # 如果词条存在于词汇表中，则置1
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


'''
将切分的实验样本词条整理成不重复的词条列表，也就是词汇表

Parameters:
    dataSet - 整理的样本数据集
Returns:
    vocabSet - 返回不重复的词条列表，也就是词汇表
'''


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # 取并集
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


'''
朴素贝叶斯分类器训练函数

Parameters:
    trainMatrix - 训练文档矩阵，即setOfWords2Vec返回的returnVec构成的矩阵
    trainCategory - 训练类别标签向量，即loadDataSet返回的classVec
Returns:
    p0Vect - 侮辱类的条件概率数组
    p1Vect - 非侮辱类的条件概率数组
    pAbusive - 文档属于侮辱类的概率
'''


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 计算训练的文档数目
    numWords = len(trainMatrix[0])  # 计算每篇文档的词条数
    pAbusive = sum(trainCategory) / float(numTrainDocs)  # 文档属于侮辱类的概率
    p0Num = np.zeros(numWords);
    p1Num = np.zeros(numWords)  # 创建numpy.zeros数组,词条出现数初始化为0
    p0Denom = 0.0;
    p1Denom = 0.0  # 分母初始化为0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:  # 统计属于侮辱类的条件概率所需的数据，即P(w0|1),P(w1|1),P(w2|1)···
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:  # 统计属于非侮辱类的条件概率所需的数据，即P(w0|0),P(w1|0),P(w2|0)···
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


'''
朴素贝叶斯分类器分类函数

Parameters:
    vec2Classify - 待分类的词条数组
    p0Vec - 侮辱类的条件概率数组
    p1Vec -非侮辱类的条件概率数组
    pClass1 - 文档属于侮辱类的概率
Returns:
    0 - 属于非侮辱类
    1 - 属于侮辱类

'''


def classifyNB(v2Classify, p0vec, p1vec, pclass1):
    # 对应元素相乘
    p1 = reduce(lambda x, y: x * y, v2Classify * p1vec) * pclass1
    p0 = reduce(lambda x, y: x * y, v2Classify * p0vec) * (1 - pclass1)
    if p1 > p0:
        return 1
    else:
        return 0


'''
朴素贝叶斯分类器分类函数


'''


def testingNB():
    # 创建实验样本
    listOPosts, listClasses = loadDataSet()
    # 创建词汇列表
    myVocabList = createVocabList(listOPosts)
    print("myVocabList:\n", myVocabList)
    trainMat = []
    # 将实验样本向量化
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    print("trainMat:\n", trainMat)
    # 训练分类器
    p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    testEnty = ['love', 'my', 'dalmation']
    # 测试样本向量化
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEnty))
    if classifyNB(thisDoc, p0V, p1V, pAb):
        print(testEnty, '属于侮辱类')
    else:
        print(testEnty, '属于非侮辱类')
    testEnty = ['stupid', 'garbage']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEnty))
    if classifyNB(thisDoc, p0V, p1V, pAb):
        print(testEnty, '属于侮辱类')
    else:
        print(testEnty, '属于非侮辱类')


'''
朴素贝叶斯函数修改版
Parameters:
    trainMatrix - 训练文档矩阵，即setOfWords2Vec返回的returnVec构成的矩阵
    trainCategory - 训练类别标签向量，即loadDataSet返回的classVec
Returns:
    p0Vect - 侮辱类的条件概率数组
    p1Vect - 非侮辱类的条件概率数组
    pAbusive - 文档属于侮辱类的概率
'''


def trainNB0Edit(trainMatrix, trainCategory):
    numTrainMax = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainMax)
    # 创建numpy.ones数组,词条出现数初始化为1，拉普拉斯平滑
    p0Num = np.ones(numWords);
    p1Num = np.ones(numWords)
    # 分母初始化为2, 拉普拉斯平滑
    p0Same = 2.0;
    p1Same = 2.0
    for i in range(numTrainMax):
        # 统计侮辱性条件所需要的概率 即p(w0|1) p(w1|1)..
        if (trainCategory[i]) == 1:
            p1Num += trainMatrix[i]
            p1Same += sum(trainMatrix[i])
        else:
            p0Num += trainCategory[i]
            p0Same += sum(trainMatrix[i])
    # 取对数 防止向下溢出
    p1Vect = np.log(p1Num / p1Same)
    p0Vect = np.log(p0Num / p0Same)
    # 返回侮辱类条件概率数组，非侮辱类条件概率数组 ，文档属于侮辱类条件概率
    return p0Vect, p1Vect, pAbusive


'''
朴素贝叶斯函数分类器分类函数修改版
Parameters:
    vec2Classify - 待分类的词条数组
    p0Vec - 侮辱类的条件概率数组
    p1Vec -非侮辱类的条件概率数组
    pClass1 - 文档属于侮辱类的概率
Returns:
    0 - 属于非侮辱类
    1 - 属于侮辱类
'''


def classifNBTest(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + np.log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    postingList, classVec = loadDataSet()
    myVocabList = createVocabList(postingList)
    print('myVocabList:\n', myVocabList)
    trainMat = []
    for postinDoc in postingList:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0Edit(trainMat, classVec)
    print('p0V:\n', p0V)
    print('p1V:\n', p1V)
    print('classVec:\n', classVec)
    print('pAb:\n', pAb)
