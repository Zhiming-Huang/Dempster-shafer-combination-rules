# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:25:11 2017

Dempster-Shafer Combination rule

@author: Zhiming
"""
from numpy import *

def DSCombination (Dic1, Dic2):
    ## extract the frame dicernment      
    sets=set(Dic1.keys()).union(set(Dic2.keys()))
    Result=dict.fromkeys(sets,0)
    ## Combination process
    for i in Dic1.keys():
        for j in Dic2.keys():
            if set(str(i)).intersection(set(str(j))) == set(str(i)):
                Result[i]+=Dic1[i]*Dic2[j]
            elif set(str(i)).intersection(set(str(j))) == set(str(j)):
                Result[j]+=Dic1[i]*Dic2[j]
                 
     ## normalize the results
    f= sum(list(Result.values()))
    for i in Result.keys():
        Result[i] /=f
    return Result
