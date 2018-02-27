'''
function:
    store some normal constants，form by list
        
Created on 2017年2月27日

@author: yangfan
'''
REALTIME_PRICE_COLS = ['name','today_open','yesterday_open','now_price',
                       'today_high','today_low','buy1','sell1',
                       'volume','turnover','apply_of_buy1','buy1',
                       'apply_of_buy2','buy2','apply_of_buy3','buy3',
                       'apply_of_buy4','buy4','apply_of_buy5','buy5',
                       'apply_of_sell1','sell1','apply_of_sell2','sell2',
                       'apply_of_sell3','sell3','apply_of_sell4','sell4',
                       'apply_of_sell5','sell5','date','time','other']

DAY_PRICE_COLS = ['date', 'open', 'high', 'close', 'low', 'volume',
                  'chg', '%chg', 'ma5', 'ma10', 'ma20',
                  'vma5', 'vma10', 'vma20', 'turnover']

IFENGCOM_DAY_URL = 'http://api.finance.ifeng.com/%s/?code=%s&type=last'
IFENGCOM_MIN_URL = 'http://api.finance.ifeng.com/akmin?scode=%s&type=%s'
SINA_REALTIME_URL = 'http://hq.sinajs.cn/list=%s'

INDEX_KEY = ['SH', 'SZ', 'HS300', 'SZ50', 'GEB', 'SMEB']
INDEX_LIST = {'SH': 'sh000001', 'SZ': 'sz399001', 'HS300': 'sz399300',
              'SZ50': 'sh000016', 'GEB': 'sz399006', 'SMEB': 'sz399005'}
INDEX_DAY_PRICE_COLS= ['date', 'open', 'high', 'close', 'low', 'volume',
                       'chg', '%chg', 'ma5', 'ma10', 'ma20',
                       'vma5', 'vma10', 'vma20']

K_TYPE_KEY = ['D', 'W', 'M']
K_TYPE = {'D': 'akdaily', 'W': 'akweekly', 'M': 'akmonthly'}
K_TYPE_MIN_KEY = ['5', '15', '30', '60']


PAGE_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
PAGE_DOMAIN = {'sina': 'sina.com.cn', 'ifeng': 'ifeng.com'}
URL_ERROR_MSG = '获取失败，请检查网络状态，或者API端口URL已经不匹配！'