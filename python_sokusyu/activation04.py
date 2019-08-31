import numpy as np
import matplotlib.pylab as plt

def identity(a):
  return a

# xの幅の定義
x = np.arange(-5.0, 5.0, 0.1)
# 関数の呼び出し
y = identity(x)
# 関数の描画
plt.plot(x, y)
# yのリミットをの定義
plt.ylim(-5.0, 5.0)
# グラフ出力
plt.show()
