#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:36:30 2023

"""
total=0
count=0
average=0

while True:
    try:
        usr_input=input('enter a number: ')
        if usr_input=='done':
            print ('total: ',total,'count: ',count, 'average: ', total/count)
            break
        else:
            usr_input=float(usr_input)
            total=total+usr_input
            count=count+1
    except:
        print ('Invalid input')

