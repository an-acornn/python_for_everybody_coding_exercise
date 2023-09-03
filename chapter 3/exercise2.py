#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:01:30 2023

"""


try:
    hour=float(input('Enter Hours: '))
    rate=float(input('Enter Rate: '))
    if hour>40:
        pay=40*rate+(hour-40)*rate*1.5
    else:
        pay=hour*rate
    print ('Pay: ',pay)
except:
    print ('Error, please enter numeric input')