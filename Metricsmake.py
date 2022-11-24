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

def metrics(student_data, max_points_per_problem, limit_pass):

    #print(student_data)

    fig = plt.figure(figsize=(8,7))
    ax1 = fig.add_axes([0.10, 0.10, 0.35, 0.30])
    ax2 = fig.add_axes([0.55, 0.10, 0.35, 0.30])
    ax3 = fig.add_axes([0.10, 0.60, 0.35, 0.30])
    ax4 = fig.add_axes([0.55, 0.60, 0.35, 0.30])

    #Plot 1: Mean Points per Problem
    mean_z1 = np.mean(student_data['z1'].data)
    mean_z2 = np.mean(student_data['z2'].data)
    mean_z3 = np.mean(student_data['z3'].data)
    mean_z4 = np.mean(student_data['z4'].data)
    mean_z5 = np.mean(student_data['z5'].data)
    means = [mean_z1, mean_z2, mean_z3, mean_z4, mean_z5]
    
    ax1.axes.bar(range(5), means, width=0.8)
    ax1.set_ylim(0, max_points_per_problem)    
    ax1.set_title('Mean points per problem')
    ax1.set_xlabel('Problem')
    ax1.set_ylabel('Points / ' + str(max_points_per_problem))



    #Plot 2: Pie_Chart
    points_sum = student_data['z1'].data +\
                 student_data['z2'].data +\
                 student_data['z3'].data +\
                 student_data['z4'].data +\
                 student_data['z5'].data 

    fails  = (points_sum < limit_pass).sum()
    passes = (points_sum >= limit_pass).sum()
    colorlist = ['green','red']
    ax2.pie([passes, fails], labels=['passes', 'fails'], autopct='%1.1f%%', colors = colorlist)
    ax2.legend(loc="center left", bbox_to_anchor=(0.9, 0, 0.4, 1))
    ax2.set_title('Pass ratio, Points > ' + str(limit_pass))



    #Plot 3: Gaussian
    total_points = max_points_per_problem * 5 #Assuming 5 probl
    percentage   = points_sum / total_points
    num_bins     = int(10 + len(points_sum) / 10)
    n, bins, patches = ax3.hist(percentage, num_bins, density=True)

    mu = 0.5
    sigma = 0.1  

    gauss_x = np.linspace(0,1,100)
    gauss_y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *\
         np.exp(-0.5 * (1 / sigma * (gauss_x - mu))**2))
    ax3.plot(gauss_x, gauss_y, '--')
    ax3.set_title('Total student points distribution')
    ax3.set_xlim(0, 1)
    #ax3.set_ylim(0, 1)
    ax3.set_xlabel('Points/Total')
    ax3.set_ylabel('Student N (normalised)')


    #Plot 4: Cumulative Pass ratio
    old_pass_perct     = ascii.read('Input/cumulative_stat.txt', data_start=0)
    current_pass_perct = passes / (passes + fails)
    current_n_test     = old_pass_perct['n_test'][-1] + 1
    total_pass_perct   = np.append(old_pass_perct['pass_perct'], current_pass_perct)
    total_n_test       = np.append(old_pass_perct['n_test'], current_n_test)   
    ax4.axes.plot(total_n_test[1:], total_pass_perct[1:])
    ax4.axes.scatter(total_n_test[1:], total_pass_perct[1:])

    ax4.set_title('Cumulative pass percentage')
    #ax4.set_xlim(0, 1)
    #ax4.set_ylim(0, 1)
    ax4.set_xlabel('N Test')
    ax4.set_ylabel('Percentage')

    plt.savefig('metricsplot.png', dpi=130)
    plt.close()


    return()
    





