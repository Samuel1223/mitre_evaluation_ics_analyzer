# -*- coding: utf-8 -*-
"""Companys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wnLrHL4QoqPZqw0CcsvLDCN1DiKh9ECL
"""

class companys ():
  import pandas as pd
  pd.options.mode.chained_assignment = None
  
  for i in ['iii','claroty', 'dragos', 'Microsoft','armis']:
    com_data = statistic(i + '_ICS_Results.json' )