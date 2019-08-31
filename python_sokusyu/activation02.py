# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
  return 1 / (1+np.exp(-x))

# xの幅の定義
x = np.arange(-5.0, 5.0, 0.1)
# 関数の呼び出し
y = sigmoid(x)
# 関数の描画
plt.plot(x, y)
# yのリミットをの定義
plt.ylim(-0.1, 1.1)
# グラフ出力
plt.show()
