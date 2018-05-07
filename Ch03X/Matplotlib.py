# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 17:01
# @Author  : shihao
# @Email   : chensh@udcredit.com
# @File    : Matplotlib.py
# @Software: PyCharm

from pylab import *


def test1():
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    figure(figsize=(8, 6), dpi=88)
    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    subplot(1, 1, 1)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # 绘制余弦蓝色，连续宽度1
    plot(X, C, color="blue", linewidth=1.0, linestyle="-")
    plot(X, S, color="red", linewidth=1.0, linestyle="-")
    # 设置横轴的上下限
    xlim(-4.0, -4.0)
    # 设置横轴记号
    xticks(np.linspace(-4, 4, 9, endpoint=True))
    ylim(-1.0, 1.0)
    yticks(np.linspace(-1, 1, 5, endpoint=True))
    show()


if __name__ == '__main__':
    test1()
