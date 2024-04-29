import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('saves/challenge.csv')
for index, row in df.iterrows():
    if row["Overall Position"] < 6:
        df = df.drop(index)
"""Удаление гендер позиции, если убрать из коммента, то на 20 строчки нужно из списка убрать тоже"""
# df.drop(['Gender Position'], axis=1, inplace=True)

df["Overall Position"] = (df["Overall Position"] - df["Overall Position"].min()) / (
        df["Overall Position"].max() - df["Overall Position"].min())
df["Category Position"] = (df["Category Position"] - df["Category Position"].min()) / (
        df["Category Position"].max() - df["Category Position"].min())
df.to_csv(
    "challenge_result.csv"
)

corr_matrix = df[['Overall Position', 'Gender Position', 'Category Position', 'Race No']].corr(method='pearson')

fig, ax = plt.subplots(figsize=(10, 8))  # настройка размеров хитмапа
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')  # создание хитмапа

plt.show()  # вывод хитмапа

print(df.to_string())
