# -*- coding: utf-8 -*-
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on Sun Jul 16 2017

DESCRIPTION: Creating different statistical metrics from
             student points during tests.

Code Author: Bruno Slaus
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
import numpy as np
import matplotlib.pyplot as plt
import astropy
from astropy.io import fits
from astropy.io import ascii

from Tablemake import table
from Metricsmake import metrics

##############################################################################################
#   User defined parameters:                                                                 #
##############################################################################################
results_input      = 'Input/results.txt'
jmbags_input       = 'Input/jmbags.txt'
bonus_input        = 'Input/bonus.txt'
max_points_per_problem = 10
limit_pass             = 15
##############################################################################################

student_data = ascii.read(results_input, data_start=0)
print('Student results:\n')
print(student_data)
print('\n\n')

#Adding JMBAGS
jmbag_data = ascii.read(jmbags_input, data_start=0)
jmbag_col  = np.full(len(student_data['name'].data), ''.zfill(10))
student_data['jmbag'] = jmbag_col
for name in student_data['name'].data:
    jmbag = jmbag_data['jmbag'][jmbag_data['name'] == name].data
    if np.size(jmbag) != 0:
        student_data['jmbag'][student_data['name'] == name] = str(jmbag[0]).zfill(10)

#Adding BONUS points
bonus_data = ascii.read(bonus_input, data_start=0)
bonus_col  = np.full(len(student_data['name'].data), 0)
student_data['bonus'] = bonus_col
for name in student_data['name'].data:
    bonus = bonus_data['bonus'][bonus_data['name'] == name].data
    if np.size(bonus) != 0:
        student_data['bonus'][student_data['name'] == name] = bonus



#Create table for Overleaf
table(student_data)

#Create fun graphs
metrics(student_data, max_points_per_problem, limit_pass)

print('Student results:\n')
print(student_data)
print('\n\n')




"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
End of code.
Modification history:


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
