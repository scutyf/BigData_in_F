'''
Created on 2017年3月11日

@author: lenovo
'''
import numpy
import tushare as ts
import matplotlib.pyplot as plt

_000001 = ts.get_hist_data('000001')

x = _000001.index.tolist()
y = _000001['ma5'].tolist()

plt.plot(y)
plt.xticks(numpy.arange(len(x)),x)

plt.show()