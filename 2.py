import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)  # массив из 5 случайных чисел
y = np.random.rand(5)

plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title(" диаграмма рассеяния")

plt.show()