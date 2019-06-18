# -*- coding: UTF-8 -*-

import tushare as ts

#设置token
ts.set_token('3ea669fb8b5b912691fdc1cf3e9b7ed200c81c5f4ce59a970ec7dca6')

#初始化pro接口
pro = ts.pro_api()

#查询当前所有上市交易的股票列表
#data是pandas.core.frame.DataFrame
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code, symbol, name, industry, market')


#显示全部行业
def industry_list():

    stock_tmp = data['industry'].unique()
    stock_industry_list = list(stock_tmp)
    stock_industry_list.remove(None)

    return stock_industry_list


#显示特定行业全部股票
def stocks_list(industry):

    tmp_list = industry_list()

    if industry in tmp_list:
        industry_true = data['industry']==industry
        stocks = data[industry_true]
        
        return stocks
    else:
        return "----------\n请输入正确的行业名称 --> 可以通过'industry.py'获取全部行业名称\n----------"

