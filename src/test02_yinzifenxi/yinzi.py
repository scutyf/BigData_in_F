'''
Created on 2016年12月26日
@author: lenovo
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from symbol import factor


'''
每月初取所有因子数值（以2015-01-01为例）
（1）估值：账面市值比（B/M)、盈利收益率（EPS）、动态市盈（PEG）
（2）成长性：ROE、ROA、主营毛利率（GP/R)、净利率(P/R)
（3）资本结构：资产负债（L/A)、固定资产比例（FAP）、流通市值（CMV）
'''

# DataAPI.MktStockFactorsDateRangeProGet(secID=u"",ticker=u"600000",beginDate=u"20160401",endDate=u"20160801",field=u"ticker,tradeDate,pe",pandas="1")

factors = ['B/M','EPS','PEG','ROE','ROS','GP/R','P/R','L/A','FAP','CMV']

def get_factors(f_date,factors):
    
    return
