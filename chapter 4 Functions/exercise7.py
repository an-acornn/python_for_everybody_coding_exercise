#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:39:29 2023

"""



def computegrade(score):
    if score>=0 and score<0.6:
        score_grade='F'
    elif score>=0.6 and score<0.7:
        score_grade='D'
    elif score>=0.7 and score<0.8:
        score_grade='C'
    elif score>=0.8 and score<0.9:
        score_grade='B'
    elif score >=0.9 and score<=1:
        score_grade='A'
    print (score_grade)
    return score_grade

try:
    score=float(input('Enter score: '))
    computegrade(score)
except:
    print ('Bad score')
    
