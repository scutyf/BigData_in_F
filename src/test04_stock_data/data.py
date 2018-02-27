'''
Created on 2017年2月27日
  
@author: yangfan
'''
  
import test04_stock_data.const as tconst
import pandas
import json
import requests



class Realtime_data(object):
    '''
    Real-time data
    '''
    def __init__(self,code = None):            
        if code in tconst.INDEX_KEY:
            self.__code = tconst.INDEX_LIST[code]
        else:
            if len(code)!=6:
                raise IOError('WRONG CODE')
            else:
                if code[0] in ['0','3']:
                    self.__code = 'sz%s'%code
                elif code[0] in ['6']:
                    self.__code = 'sh'+code
                else:
                    raise IOError('WRONG CODE')
                
    def get_realtime_data(self):
        list01 = self.ping_url().split(sep=',')
        df = pandas.DataFrame(list01,index = tconst.REALTIME_PRICE_COLS,columns=[self.__code])   
        return df
    
    def get_url(self):
        '''
        function:
            to get relative url of the code
            SINA_REALTIME_URL = 'http://hq.sinajs.cn/list=sh%s'
        '''          
        if None!=self.__code:
            url = tconst.SINA_REALTIME_URL % (self.__code)
            return url
        else:
            raise  IOError('WRONG CODE OR DATATYPE')                
    def ping_url(self):
        '''
        function:
            to test the url is useful or not
            if it is useful:
                return the url
            else:
                return fail
        '''
        try:
            req = requests.get(self.get_url())
            if len(req.text)<30:
                raise IOError('No data!')
        except Exception as e:
            print(e)
        else: 
            return self.cut_string(req.text)
        
    def cut_string(self,str01):
        text = ''
        for i in range(len(str01)):
            if str01[i] == '\"':
                text += str01[i+1:-3]
                break              
        return text
  
class Hist_data(object):
    '''
    history datas
    '''
    def __init__(self,code = None,start = None,end = None,datatype = None):     
        self.__start = start
        self.__end = end
        self.__datatype = datatype
        
        if code in tconst.INDEX_KEY:
            self.__code = tconst.INDEX_LIST[code]
        else:
            if len(code)!=6:
                raise IOError('WRONG CODE')
            else:
                if code[0] in ['0','3']:
                    self.__code = 'sz%s'%code
                elif code[0] in ['6']:
                    self.__code = 'sh'+code
                else:
                    raise IOError('WRONG CODE')
 
    def get_hist_data(self):
        js = json.loads(self.ping_url())
        cols=[]
        if len(js['record'][0])==14:
            cols = tconst.INDEX_DAY_PRICE_COLS
        elif len(js['record'][0])==15:
            cols = tconst.DAY_PRICE_COLS
        else:
            raise IOError('不知道出什么问题了')
        
        df = pandas.DataFrame(js['record'],columns = cols)
        
        if None!=self.__start and None!=self.__end and self.__start>self.__end:
            raise IOError('输入起止时间错误')               
        else:
            if None!=self.__start:
                df = df[df.date>=self.__start]
            if None!=self.__end:
                df = df[df.date<=self.__end]
           
        df = df.set_index('date')
        return df      
      
    def get_url(self):
        '''
        function:
            to get relative url of the code
            IFENGCOM_URL ='http://api.finance.ifeng.com/%s/?code=%s&type=last'
            SINA_REALTIME_URL = 'http://hq.sinajs.cn/list=sh%s'
        '''
        if self.__datatype in tconst.K_TYPE_KEY:
            url = tconst.IFENGCOM_DAY_URL % (tconst.K_TYPE[self.__datatype],self.__code)
            return url
          
        if self.__datatype in tconst.K_TYPE_MIN_KEY:
            url = tconst.IFENGCOM_MIN_URL % (self.__code,self.__datatype)
            return url
          
        else:
            raise  IOError('WRONG CODE OR DATATYPE')
      
    def ping_url(self):
        '''
        function:
            to test the url is useful or not
            if it is useful:
                return the url
            else:
                return fail
        '''
        try:
            req = requests.get(self.get_url())
            if len(req.text)<20:
                raise IOError('No data!')
        except Exception as e:
            print(e)
        else: 
            return req.text