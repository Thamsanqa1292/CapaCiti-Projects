# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 08:43:48 2020

@author: Thamsanqa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = {
    'Category' : [np.nan, 'Chips, Cooldrinks, Chocolates, Pies, Fruit, Cupcakes, Veggies'],
    'Products' : ['Simba, Lays, Coke, Fanta, Cadbury, Tex, Pepper Steak, Chicken, Pear, Apple, Orange, Vanilla, Chocolotae, Spinach, Cabbage ']}
df = pd.DataFrame(raw_data)


df['column'] = df.category.apply(lambda s: ','.join(s.split(',')[-2:]))

print(df)