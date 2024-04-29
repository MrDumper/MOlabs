import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats

"""
    Первая часть, общее задание, аля задание 1 снизу, находится в фунеции one
    Вторая часть, то бишь второе задание, которое по вариантам, находится в функции two
"""


def one():
    x = np.array([0, 38.5, 59, 97.4, 119.2, 129.5, 198.7, 248.7, 318, 438.5])
    y = np.array([19.5, 15, 13.5, 23.3, 6.3, 2.5, 13, 1.8, 6.5, 1.8])
    corr, p_value = scipy.stats.pearsonr(x, y)
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

    plt.scatter(x, y)
    plt.plot(x, intercept + slope * np.array(x), 'r')

    plt.xlabel('X: ')
    plt.ylabel('Y: ')
    plt.title('Зависимость Y от переменной X: ')

    plt.show()
    print("Коэффициент корреляции: ", corr)
    print("p-value: ", p_value)
    print("Уравнение регрессии: y = ", intercept, "+", slope, "* x")


def two():
    x = np.array([26, 48, 65, 23, 150, 123, 264, 156, 152, 154, 520, 415])
    y = np.array([221, 153, 155, 102, 156, 264, 435, 156, 203, 325, 456, 163])

    xy = x * y
    x_squared = x ** 2
    y_squared = y ** 2
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_diff = x - x_mean
    y_diff = y - y_mean
    x_diff_squared = x_diff ** 2
    y_diff_squared = y_diff ** 2
    xy_sum = np.sum(xy)
    x_squared_sum = np.sum(x_squared)
    y_squared_sum = np.sum(y_squared)
    x_diff_squared_sum = np.sum(x_diff_squared)
    y_diff_squared_sum = np.sum(y_diff_squared)

    print("х * y: ", xy)
    print("Квадрат x: ", x_squared)
    print("Квадрат y: ", y_squared)
    print("Отклонение от среднего значения x: ", x_diff)
    print("Отклонение от среднего значения y: ", y_diff)
    print("Отклонение от среднего значения в квадрате x: ", x_diff_squared)
    print("Отклонение от среднего значения в квадрате y: ", y_diff_squared)
    print("Сумма x и y: ", xy_sum)
    print("Сумма квадратов x: ", x_squared_sum)
    print("Сумма квадратов y: ", y_squared_sum)
    print("Сумма квадратов отклонений x: ", x_diff_squared_sum)
    print("Сумма квадратов отклонений y: ", y_diff_squared_sum)

    coefficients = np.polyfit(x, y, 1)

    print("\nУравнение регрессии: y = {:.2f}x + {:.2f}".format(coefficients[0], coefficients[1]))

    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()

    std_err = model.bse

    print("\nСтандартные ошибки коэффициентов: ")
    print(std_err)

    def regression_equation(x):
        return 0.01 * x + 443.71

    x_values = np.array([26, 48, 65, 23, 150, 123, 264, 156, 152, 154, 520, 415])
    y_pred = regression_equation(x_values)

    plt.scatter(x, y)
    plt.title('Корреляционное поле')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red')
    plt.title('Регрессионная линия')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


one()
