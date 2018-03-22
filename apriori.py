# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# магазин во франции
# Importing the dataset # header не нужен в dataset , поэтому убираем его
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# считываем все данные из dataset в transactions
transactions = []

for i in range(0, 7501):
  # тут пушим в массив другой массив, который считывает
  # данные dataset.values[i, j], потом переводит эти данные в строку str()
  # в интервале от [0 до 20)
  transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

# Training Apriori on the dataset # l161
from apyori import apriori
rules = apriori(
    transactions,
    # мнимальный процент покупок 3(покупкиВдень)*7(неделя)/7500=0.0028
    min_support = 0.003,
    # правильное правило в 90% (но нет таких правил в реальности)
    # поэтому делим на два и потом еще на два делим 0.45 , 0.2
    # хорошая комбинация как сказал учитель
    min_confidence = 0.2,
    # минимум надо 3, можно и 4,5 или даже 6, но это от данных зависит
    min_lift = 3,
    min_length = 2
    # max_length = 4
  )
# это все экспериментально, нужно пробовать с такими параметрами
# потом нужно пробовать эти правила и потом на основе результата
# реального уже можно корректировать настроки под себя

# Visualising the results
# результаты уже отсортированы по комбинации критерий support confidence lift
# в R были отсортированы по lift, результат почти такойже
results = list(rules)
# исправляем проблему отображения данных
results_list = []
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]))















