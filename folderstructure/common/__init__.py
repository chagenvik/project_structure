# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:17:35 2021

@author: CHHAG
"""
import os

cwd=os.getcwd()

dir_path=os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)
import setup
import func

os.chdir(cwd)



