# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize


def f1(x, a, b):
    return a*x + b


def f2(x, a, b, c):
    return a*x*x + b*x + c


def plot_test():
    plt.figure(figsize=(8, 6))

    # 拟合点
    # x0 = [1, 2, 3, 4, 5]
    # y0 = [1, 3, 8, 18, 36]
    # y0 = [8663.1737785, 9000.481299000003, 9333.197167000002, 9439.8274415, 9483.961620999999, 9634.408301]
    # x0 = [302.5600, 315.5900, 329.0500, 332.9800, 334.9800, 334.9800]

    x0 = [1, 2, 3, 4, 5, 6]
    y0 = [9, 14, 21, 30, 41, 54]

    # 绘制散点
    plt.scatter(x0[0:], y0[0:], 25, color='red', label='数据', linewidth=1)

    # 直线拟合与绘制
    # A1, B1 = optimize.curve_fit(f1, x0, y0)[0]
    # x1 = np.arange(0, 6, 0.01)
    # y1 = A1*x1 + B1
    # plt.plot(x1, y1, color='blue', label='qwewe', lineWidth=1)

    # 二次曲线拟合与绘制
    A2, B2, C2 = optimize.curve_fit(f2, x0, y0)[0]
    print(A2)
    print(B2)
    print(C2)
    # x2 = np.arange(300, 360, 10)
    x2 = np.arange(1, 6, 0.01)
    y2 = A2*x2*x2 + B2*x2 + C2
    plt.plot(x2, y2, color='blue', label='曲线', lineWidth=1)

    plt.title("二次拟合")
    plt.xlabel('时间')
    plt.ylabel('响应')
    # 绘制图例
    plt.legend()
    # 支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 保存
    plt.savefig('D:/101.jpg', format='jpg')
    # plt.close()
    # 显示
    plt.show()


plot_test()
