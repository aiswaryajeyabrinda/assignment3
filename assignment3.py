#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_excel("C:/Users/senth/OneDrive/Desktop/temperature.xlsx")
data.cityA.mean()
data.cityB.mean()
data.cityA.median()
data.cityB.median()
data.cityA.mode()
data.cityB.mode()

