import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  y = x > 0
  return y.astype(np.int)

# xの幅の定義
x = np.arange(-5.0, 5.0, 0.1)
# 関数の呼び出し
y = step_function(x)
# 関数の描画
plt.plot(x, y)
# yのリミットをの定義
plt.ylim(-0.1, 1.1)
# グラフ出力
plt.show()