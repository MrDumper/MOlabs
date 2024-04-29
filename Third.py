import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv('saves/Apple_stock_history.csv', index_col='Date', parse_dates=True)
data = df.dropna()
train = data['2013':'2015']
test = data['2015':]

model = ExponentialSmoothing(train['Open'], trend='add', seasonal='add', seasonal_periods=365)
model_fit = model.fit()
forecast = model_fit.forecast(len(test))

plt.plot(test.index, test['Open'], label='Фактические значения')
plt.plot(test.index, forecast, label='Прогноз')
plt.legend(loc='upper left')
plt.show()

rmse = mean_squared_error(test['Open'], forecast, squared=False)
print('RMSE:', rmse)
