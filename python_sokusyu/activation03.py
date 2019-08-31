import numpy as np
import matplotlib.pylab as plt

def relu(x):
  return np.maximum(0, x)

# xの幅の定義
x = np.arange(-5.0, 5.0, 0.1)
# 関数の呼び出し
y = relu(x)
# 関数の描画
plt.plot(x, y)
# yのリミットをの定義
plt.ylim(-0.1, 1.1)
# グラフ出力
plt.show()
