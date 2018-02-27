import numpy
import pandas
# import pandas.io.data
import pandas_datareader.data

px=pandas_datareader.data.DataReader('F-F_Research_Data_factors','famafrench')

print(px)
# sp500 = pandas.io.data.datareader

df01 = pandas.Series([1,3,5,2,5,2])

print(df01)

'''
# rand简单随机数
# randn有具有正态分布的随机数
# randint(low[, high, size])
# random其他具体用法http://www.mamicode.com/info-detail-507676.html
'''
arr01 = numpy.random.rand(1,10)

print(arr01)
