import functions as func
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.float_format', '{:.15f}'.format)

dane = pd.read_csv('.\\9.csv', header=None)
dane.columns = ['first', 'second']

# histograms
plt.style.use('dark_background')
dane['first'].plot(kind = 'hist', bins = 1000, title = 'First Dataset', xlabel ='values', ylabel = 'frequency')
plt.show()
dane['second'].plot(kind = 'hist', bins = 1000, title = 'Second Dataset', xlabel ='values', ylabel = 'frequency')
plt.show()

pos_ind_1 = func.position_indicators(dane['first'].values, 'result1')
pos_ind_2 = func.position_indicators(dane['second'].values, 'result2')

pos_ind_all = pos_ind_1.join(pos_ind_2)


dis_rates_1 = func.dispersion_rates(dane['first'].values, 'result1')
dis_rates_2 = func.dispersion_rates(dane['second'].values, 'result2')
dis_rates_all = dis_rates_1.join(dis_rates_2)

print('position_indicators')
print(pos_ind_all)
print('dispersion rates')
print(dis_rates_all)
print()
print('first test')
func.test(dane['first'].values,1)
print()
print('second test')
func.test(dane['second'].values,2)
print()
print('third test')
func.test3(dane['first'].values,dane['second'].values)
