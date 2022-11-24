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
    
'''
#First we open the required data with astropy
print 'Plotting both the inner and the outer part of the field.\n'                                

Data=fits.open(basename + 'OUT_Single.fits')[1].data   
Total_flux_corr = Data['Total_flux_corr']
Spectral_index  = Data['Spectral_index']
print  'len(Total_flux_corr):', len(Total_flux_corr)
print  'len(Spectral_index):' , len(Spectral_index)

Data_2=fits.open(basename + 'IN_Single.fits')[1].data   
Total_flux_corr_2 = Data_2['Total_flux_corr']
Spectral_index_2  = Data_2['Spectral_index']
print  'len(Total_flux_corr_2):', len(Total_flux_corr_2)
print  'len(Spectral_index_2):' , len(Spectral_index_2)



#We define the limit line
x = np.arange(0.00001, 1, 0.0001)
alpha_limit = -(np.log10(x)-np.log10(Det_Limit)) / (np.log10(610)-np.log10(1400))



#Plotting the graph
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0.12, 0.10, 0.8, 0.40])
ax.set_xlabel(r'$S_{610}/\ \mathrm{mJy}$', size=22)
ax.set_ylabel(r'$\alpha$', size=22)
ax.set_xlim(2*10**(-4)*1000, 10*1000)
ax.set_ylim(-2.5, 2.5)
plt.scatter(Total_flux_corr*1000, Spectral_index,color='black', s=2)
plt.plot(x*1000,alpha_limit, color='black', linestyle='--')
plt.xscale('log')
plt.hlines(0.745486, 0.0001, 10*1000, linestyle='-', color='red')
print 'Mean Outer Part: 0.745486'
#plt.hlines(0.87651, 0.0001, 10, linestyle=':', color='red')
#PLOTTING THE VERTICAL LINE OF THE LIMIT WE CUT/CROP
plt.vlines(0.02*1000, -3, 4, linestyle='-', color='blue')
ax.text(0.6*1000, 2, 'Vanjski dio', fontsize=16)

axx = fig.add_axes([0.12, 0.50, 0.8, 0.40])
#axx.set_xlabel(r'$S_{610}/\ mJy$', size=22)
axx.set_ylabel(r'$\alpha$', size=22)
axx.set_xlim(2*10**(-4)*1000, 10*1000)
axx.set_ylim(-1.9, 2)
plt.scatter(Total_flux_corr_2*1000, Spectral_index_2,color='black', s=2)
plt.plot(x*1000,alpha_limit, color='black', linestyle='--')
plt.xscale('log')
plt.hlines(0.646233, 0.0001, 10*1000, linestyle='-', color='red')
print 'Mean Inner Part: 0.646233'
#plt.hlines(0.81143, 0.0001, 10, linestyle=':', color='red')
#PLOTTING THE VERTICAL LINE OF THE LIMIT WE CUT/CROP
plt.vlines(0.015*1000, -3, 4, linestyle='-', color='blue')
axx.text(0.6*1000, 1.6, 'Srednji dio', fontsize=16)
axx.set_xticklabels([], alpha=0.0)

plt.savefig('Plot_Final', dpi=130)
#plt.savefig('/home/bruno/Desktop/BIAS_SEMINAR_TOGETHER', dpi=200)
plt.show()
plt.close()

'''




