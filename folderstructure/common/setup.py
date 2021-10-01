# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:33:39 2021

@author: CHHAG
"""

import pandas as pd
from pathlib import Path

#read file using pandas and added parent directory
x=pd.read_csv(str(Path().absolute())+'//data.csv')


#read file using open
with open('data.csv') as F:
    a=F.readlines()


# #read file using pandas
# x=pd.read_csv('data.csv')
