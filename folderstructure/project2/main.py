# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:29:41 2021

@author: CHHAG
"""

import sys
import os
import pandas as pd
import numpy as np

#os.chdir('../common/')   #changing cwd to the common folder will solve the problem

sys.path.append('..')

import common

#os.chdir('../project2/')    #changing cwd back to project2 folder
#read project2spesific data
y=pd.read_csv('project2spesificdata.csv')

z=pd.read_csv('../common/data.csv')

print(common.func.myfunc(5,3))

x=z.to_numpy()
