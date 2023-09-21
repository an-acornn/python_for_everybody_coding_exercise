#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:29:42 2023

"""

hours=float(input('Enter Hours: '))
rate=float(input('Enter Rate: '))


    
def computepay(hours, rate):
    if hours>40:
        pay=40*rate+(hours-40)*rate*1.5
    else:
        pay=hours*rate
    print('Pay: ',pay)
    return pay

computepay(hours, rate)