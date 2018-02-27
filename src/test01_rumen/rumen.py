'''
Created on 2016年12月23日
print('Merry Christmas!!!')
@author: lenovo
'''

import numpy as np
import pandas as pd

df = pd.DataFrame([1,2,4,6,3],columns=['number'],index=['a','b','c','d','e'])
print(df)
print(df.ix[['a','d']])

 
