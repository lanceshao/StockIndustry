# -*- coding: UTF-8 -*-
from my_module import stocks_list
import sys

def show_stocks():
    
    res = stocks_list(sys.argv[1])

    print(res)

#执行
show_stocks()