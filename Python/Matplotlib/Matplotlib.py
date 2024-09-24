import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4], [2, 5, 9, 10], marker='o', color='red', linestyle='--', label='Line A')
plt.plot([2, 5, 8, 0], [1, 2, 9, 10], marker='D', color='black', linestyle=':', label='Line B')
plt.title("嘻嘻哈哈")
plt.xlabel('嘻嘻')
plt.ylabel('哈哈')
plt.legend()  # 显示图例 #
plt.show()

x = np.linspace(-10, 10, 100)
y1 = x.copy()
y2 = x ** 2
y3 = x ** 3 + 2 * x ** 2 + 1
plt.plot(x, y1, color='red', label='y=x')
plt.plot(x, y2, color='green', label='y=x^2')
plt.plot(x, y3, color='blue', label='y=x^3+2x^2+1')
plt.legend()
plt.show()

data = [10, 20, 80, 40]
days = ['Fri', 'Sat', 'Sun', 'Mon']
plt.bar(range(1, 5), data, align='center', label=days)
plt.xticks(range(1, 5), labels=days)
plt.legend()
plt.show()
