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



















