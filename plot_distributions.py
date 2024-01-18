#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

before = pd.read_csv('before_installation.csv', delimiter="\t")
after = pd.read_csv('after_installation.csv', delimiter="\t")
winter = pd.read_csv('winter.csv', delimiter="\t")
fig, axs = plt.subplots(ncols = 1)
plt.xlabel('Скорость, км/ч')
plt.ylabel('Доля автомобилей')
sns.kdeplot(before['Speed est.'], x = before['Speed est.'], ax = axs, label = "Без конусов")
sns.kdeplot(after['Speed est.'], x = after['Speed est.'], ax = axs, label = "С конусами")
sns.kdeplot(winter['Speed est.'], x = winter['Speed est.'], ax = axs, label = "Без конусов, зима")
plt.legend()
plt.show()
