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

def table(student_data):

    #print(student_data)

    table_text_UP = str(
    '\\begin{table}[] \n'+
    '\caption{Caption }\n'+
    '\centering\n'+
    '\\begin{tabular}{|p{3.5cm}|p{2.5cm}||p{0.5cm}|p{0.5cm}|p{0.5cm}|p{0.5cm}|p{0.5cm}|p{0.8cm}|p{0.8cm}|}\n'+
    '     \hline\n'+
    '      Ime & JMBAG & Z1 & Z2 & Z3 & Z4 & Z5 & Bonus & Sum \\\\ \n'+
    '     \hline\n')
    
    table_text_DATA = str('')
    for r in range(len(student_data['name'].data)):
        table_text_DATA = table_text_DATA + str(student_data['name'].data[r]).replace("_", " " ) + ' & ' \
                                          + str(student_data['jmbag'].data[r]) + ' & ' \
                                          + str(student_data['z1'].data[r]) + ' & '\
                                          + str(student_data['z2'].data[r]) + ' & '\
                                          + str(student_data['z3'].data[r]) + ' & '\
                                          + str(student_data['z4'].data[r]) + ' & '\
                                          + str(student_data['z5'].data[r]) + ' & '\
                                          + str(student_data['bonus'].data[r]) + ' & '\
                                          + str(student_data['z1'].data[r] + \
                                                student_data['z2'].data[r] + \
                                                student_data['z3'].data[r] + \
                                                student_data['z4'].data[r] + \
                                                student_data['z5'].data[r] + \
                                                student_data['bonus'].data[r] ) + ' \\\\ \n'
                                              
    table_text_DOWN = str(
    '\hline \n'+
    '\end{tabular} \n'+
    '\end{table}')



    table_text = table_text_UP + table_text_DATA + table_text_DOWN

    with open('output_table.txt', 'w') as f:
        f.write(table_text)

    return()


