import numpy as np
import operator

'''
    K-邻近算法简介
    存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，
    即我们知道样本集中每一个数据与所属分类的对应关系。输入没有标签的新数据后，
    将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。
    一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。
    最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。
'''


def createDataSet():
    # 四组 二维特征
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    # 标签
    labels = ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels


# k-邻近算法
'''
    KNN算法，分类器

Parameters:
    inx _ 分类的输入向量
    dataSet _ 输入的样本训练集
    lables _ 标签向量
    k _ 最近邻居的数目
Returns:    
    sortedClassCount[0][0] _ 分类结果
 '''


def classify0(inX, dataSet, lables, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    # sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方，计算出距离
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}
    # 选择距离最小的两个k点
    for i in range(k):
        # 取出前key个类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDataSet()
    test = [101, 20]
    test_class = classify0(test, group, labels, 3)
    print(test_class)


