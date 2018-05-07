# _*_ coding : UTF-8 _*_
import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import operator
from matplotlib.font_manager import FontProperties

'''
    K-邻近算法简介
    存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，
    即我们知道样本集中每一个数据与所属分类的对应关系。输入没有标签的新数据后，
    将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。
    一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。
    最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。
'''

"""
函数说明:kNN算法,分类器

Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果

Modify:
    2017-03-24
"""


def classify0(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向),行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方,计算出距离
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
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


'''
函数说明：打开并解析文件，对数据进行分类：1代表不喜欢,2代表魅力一般,3代表极具魅力

Parameters:
    filename - 文件名
Returns:
    returnMat - 特征矩阵
    classLabelVector - 分类Label向量
    
'''


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    # 返回的NumPy矩阵,解析完成的数据:numberOfLines行,3列
    returnMat = np.zeros((numberOfLines, 3))
    # 返回的分类标签向量
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        listFromLine = line.split('\t')
        # 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index, :] = listFromLine[0:3]
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        if listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        if listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector


'''
    数据可视化
Parameters:
    datingDataMat - 特征矩阵
    datingLabels - 分类Label
Returns:
    无
    
'''


def showdatas(datingDataMat, datingLabels):
    font = FontProperties(size=18)
    # 将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    # 当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(13, 8))

    numberOfLabels = len(datingLabels)
    LabelsColors = []
    for i in datingLabels:
        if i == 1:
            LabelsColors.append('black')
        if i == 2:
            LabelsColors.append('orange')
        if i == 3:
            LabelsColors.append('red')

    # 画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第二列(玩游戏)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 1], color=LabelsColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label a:每年获得的飞行常客里程数, b:玩视频游戏所消耗时间占,c:每周消费的冰激淋公升数
    axs0_title_text = axs[0][0].set_title(u'a/b', FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'a', FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'b', FontProperties=font)
    plt.setp(axs0_title_text, size=9, weight='bold', color='red')
    plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

    # 画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][1].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 2], color=LabelsColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label
    axs1_title_text = axs[0][1].set_title(u'a/c', FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(u'a', FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_ylabel(u'c', FontProperties=font)
    plt.setp(axs1_title_text, size=9, weight='bold', color='red')
    plt.setp(axs1_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs1_ylabel_text, size=7, weight='bold', color='black')

    # 画出散点图,以datingDataMat矩阵的第二(玩游戏)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[1][0].scatter(x=datingDataMat[:, 1], y=datingDataMat[:, 2], color=LabelsColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label
    axs2_title_text = axs[1][0].set_title(u'b/c', FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(u'b', FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(u'c', FontProperties=font)
    plt.setp(axs2_title_text, size=9, weight='bold', color='red')
    plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs2_ylabel_text, size=7, weight='bold', color='black')
    # 设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                              markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                               markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                               markersize=6, label='largeDoses')
    # 添加图例
    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
    # 显示图片
    plt.show()


'''
对数据进行归一化

归一化公式： newValue = (oldValue - min) / (max - min)

Parameters:
    dataSet - 特征矩阵
Returns:
    normDataSet - 归一化后的特征矩阵
    ranges - 数据范围
    minVals - 数据最小值
'''


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 获得最大值和最小值范围
    ranges = maxVals - minVals
    # shape(dataSet)返回dataSet的矩阵行列数
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    # 原始值减去 最小值
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 除以最大值和最小值的差，得到归一化的数据
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


'''
    分类器测试函数
Parameters:
    无
Returns:
    normDataSet - 归一化后的特征矩阵
    ranges - 数据范围
    minVals - 数据最小值
'''


def datingClassTest():
    filename = 'datingTestSet.txt'
    # 得到特征矩阵和分类向量
    datingDataMat, datingLabels = file2matrix(filename)
    # 取所有数据的百分之十
    hoRatio = 0.10
    # 得到归一化后的数据
    norMat, ranges, minVals = autoNorm(datingDataMat)
    m = norMat.shape[0]
    # 得到百分之十测试数据的个数
    numTest = int(m * hoRatio)
    errCount = 0.0
    for x in range(numTest):
        # 前numTest个数据作为测试集,后m-numTest个数据作为训练集
        classResult = classify0(norMat[x, :], norMat[numTest:m, :], datingLabels[numTest:m], 4)
        print("分类结果：%d \t 真实类别：%d" % (classResult, datingLabels[x]))
        if classResult != datingLabels[x]:
            errCount += 1.0
    print("错误率：%f%%" % (errCount / float(numTest) * 100))


'''
    通过输入一个人的三维特征,进行分类输出

'''


def classifyPerson():
    resultList = ['讨厌', '有些喜欢', '非常喜欢']
    precentTats = float(input("玩视频游戏所占时间百分比："))
    ffMiles = float(input("每年获得飞行乘客里数里数:"))
    icreCream = float(input("吃冰淇凌消耗的公升数:"))
    filename = "datingTestSet.txt"
    # 训练数据
    datingDataMat, datingLabels = file2matrix(filename)
    # 训练集归一化
    normData, ranges, minVals = autoNorm(datingDataMat)
    # 样本数组测试生成测试集
    inArr = np.array([precentTats, ffMiles, icreCream])
    # 得到的测试集归一化
    norminArr = (inArr - minVals) / ranges
    # 返回分类结果
    classifierResult = classify0(norminArr, normData, datingLabels, 3)
    print("你可能%s这个人" % (resultList[classifierResult - 1]))


# 测试
if __name__ == '__main__':
    # 打开的文件名
    filename = "datingTestSet.txt"
    # # 打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    showdatas(datingDataMat, datingLabels)
    # 处理分类结果
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    print(normDataSet)
    print(ranges)
    print(minVals)
    datingClassTest()
    classifyPerson()
