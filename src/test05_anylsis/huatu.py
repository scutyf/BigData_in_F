'''
Created on 2017年3月6日

@author: lenovo
'''
import numpy
import pandas
import matplotlib.pyplot as plt
import test04_stock_data.data as t4



stock = t4.Hist_data(code='000001',datatype='D',start='2017-01-01',end='2017-02-01')
a = stock.get_hist_data()
'''将索引设置成datetime形式'''
a.set_index(pandas.to_datetime(a.index))  
# a['open'].plot(figsize=(8,5))
# x = a['date']
b = a['open']
a.info()


x = a.index.tolist()
print(x)

y = b.tolist()
plt.plot(y)
'''将x轴自定义为时间'''
plt.xticks(numpy.arange(len(x)),x)

# print(len(x),len(y))

plt.show()