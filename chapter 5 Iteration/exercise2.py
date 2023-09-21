#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:45:41 2023

"""
max_num=None
min_num=None

while True:
    try:
        usr_input=input('enter a number: ')
        if usr_input=='done':
            print ('done! max: ',max_num,'min: ',min_num)
            break
        else:
            usr_input=float(usr_input)
            if max_num is None:
                max_num=usr_input
            elif usr_input>max_num:
                max_num=usr_input
                
            if min_num is None:
                min_num=usr_input
            elif usr_input<min_num:
                min_num=usr_input
            print ('input: ',usr_input,'max: ',max_num,'min: ',min_num)
            
    except:
        print ('Invalid input')
