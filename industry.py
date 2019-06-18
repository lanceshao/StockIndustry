# -*- coding: UTF-8 -*-
from my_module import industry_list

#获取全部行业列表
list_tmp = industry_list()

for index, value in enumerate(list_tmp):
    print("%6s  %6s"%(index+1, value))