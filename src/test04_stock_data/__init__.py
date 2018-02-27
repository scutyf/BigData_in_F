 
import test04_stock_data.data as sh
import pandas
import requests
 
# a = sh.Hist_data(code='000001',datatype='D',start='2017-01-01',end='2017-02-01')
# b = a.get_hist_data()
# print(b)

a= sh.Realtime_data(code='601006')

# url = 'http://hq.sinajs.cn/list=sh601006'
# req = requests.get(url)
print(a.get_realtime_data())
# url = a.get_url()
# print(url)

  
# print('2017-01-01'>'2017-02-02')
# print(type(a))
# print(a)
# print(len('var hq_str_sz000001='))