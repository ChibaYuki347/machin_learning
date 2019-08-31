import numpy as np
import matplotlib.pylab as plt

def softmax(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y

# xの幅の定義
x = np.arange(-5.0, 5.0, 0.1)
# 関数の呼び出し
y = softmax(x)
# 関数の描画
plt.plot(x, y)
# グラフ出力
plt.show()
