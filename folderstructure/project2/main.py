# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:29:41 2021

@author: CHHAG
"""

import sys
import os
import pandas as pd

os.chdir('../common/')   #changing cwd to the common folder will solve the problem

sys.path.append('..')

from common.func import *

os.chdir('../project2/')    #changing cwd back to project2 folder
#read project2spesific data
y=pd.read_csv('project2spesificdata.csv')

print(myfunc(5,3))
