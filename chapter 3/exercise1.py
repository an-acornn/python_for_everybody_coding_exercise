#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:10:08 2023

"""
hour=float(input('Enter Hours: '))
rate=float(input('Enter Rate: '))

if hour>40:
    pay=40*rate+(hour-40)*rate*1.5
else:
    pay=hour*rate
    
print('Pay: ',pay)