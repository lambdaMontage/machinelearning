# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 22:22
# @Author  : shihao
# @Email   : chensh@udcredit.com
# @File    : test01.py
# @Software: PyCharm


import re
import sys
from imp import reload

'''
朴素贝叶斯实战之 过滤电子邮件 步骤如下：

收集数据：提供文本文件。
准备数据：将文本文件解析成词条向量。
分析数据：检查词条确保解析的正确性。
训练算法：使用我们之前建立的trainNB0()函数。
测试算法：使用classifyNB()，并构建一个新的测试函数来计算文档集的错误率。
使用算法：构建一个完整的程序对一组文档进行分类，将错分的文档输出到屏幕上。
'''


def textParse(bigString):
    listOfTokens = re.split(r'\W*', bigString)  # 将特殊符号作为切分标志进行字符串切分，即非字母、非数字
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  # 字母长度>2 转换成小写


'''
函数说明:将切分的实验样本词条整理成不重复的词条列表，也就是词汇表

Parameters:
    dataSet - 整理的样本数据集
Returns:
    vocabSet - 返回不重复的词条列表，也就是词汇表
'''


def test():
    i = 0
    while i <= 3:
        qq = input("请输入你的QQ号码：")
        if qq == "123456":
            password = input("请输入密码：")
            if (password == "234567"):
                print("欢迎进入")
                break
            else:
                print("number error")
        else:
            print("qq error")
            if ( 3- i == 0):
                print("错误次数完")
                break
            print("还有%d次机会" % (3 - i))
            i += 1


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(dataSet)
    return list(vocabSet)


if __name__ == '__main__':
    test()
    # docList = [];
    # classList = []
    #
    # for i in range(1, 26):  # 遍历25个txt文件
    #     wordList = textParse(open('/Users/shihao/Desktop/spam/%d.txt' % i, 'r').read())  # 读取每个垃圾邮件，并字符串转换成字符串列表
    #     docList.append(wordList)
    #     classList.append(1)  # 标记垃圾邮件，1表示垃圾文件
    #     wordList = textParse(open('/Users/shihao/Desktop/ham/%d.txt' % i, 'r').read())  # 读取每个非垃圾邮件，并字符串转换成字符串列表
    #     docList.append(wordList)
    #     classList.append(0)  # 标记非垃圾邮件，1表示垃圾文件
    # vocabList = createVocabList(docList)  # 创建词汇表，不重复
    # print(vocabList)
