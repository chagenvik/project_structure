# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 07:29:41 2021

@author: CHHAG
"""

import sys
import os

#os.chdir('../common/')   #changing cwd to the common folder will solve the problem

sys.path.append('..')

from common.func import *

print(myfunc(5,3))
