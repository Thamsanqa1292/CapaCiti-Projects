# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:22:01 2020

@author: Thamsanqa
"""
#This is a Random Password Generator
import random

alphabets = ["A","B","C","D","E","F"]

smallAlpha = ['a','b','c','d','e','f']

numbers =[1,2,3,4,5,6,7,8,9,0]

chars = ['!','@','#','$']

ran_1 = random.choice(alphabets) + random.choice(smallAlpha) + str(random.choice(numbers)) + random.choice(chars)
ran_2 = random.choice(alphabets) + random.choice(smallAlpha) + str(random.choice(numbers)) + random.choice(chars)
print('Your Random Password is:  ',ran_1 + ran_2)
