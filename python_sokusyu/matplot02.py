import numpy as np
import matplotlib.pyplot as plt

# 描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.arange(-10, 10, 0.1)

# 計算式
y = 2 * (x**2)

# 横軸の変数。縦軸の変数。
plt.plot(x, y)

# 描画処理
plt.show()