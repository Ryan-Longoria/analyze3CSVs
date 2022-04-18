# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:37:09 2019
HW2 code skeleton
@author: Ryan Longoria
"""

import matplotlib.pyplot as plt
import numpy as np

#%% load data
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

# close all existing floating figures
plt.close('all')

#%% Q1. plot annual total mumps cases in each year

x = []
y = []

for row in mumps:
    x.append(row[0])
    y.append(row[1] + row[2] + row[3] + row [4] + row[5] + row[6] + row[7] + row[8] + row[9] + row[10] + row[11] + row[12])

plt.figure()
plt.plot(x, y,'*-')
plt.title('Fig 1: NYC mumps cases')
plt.xlabel('Year')
plt.ylabel('Number of cases')
# complete this part

plt.show()

#%% Q2 plot annual total measels and mumps cases in log scale
y1 = []

for row in measles:
    y1.append(row[1] + row[2] + row[3] + row [4] + row[5] + row[6] + row[7] + row[8] + row[9] + row[10] + row[11] + row[12])

plt.figure()
plt.title('Fig 2: Measles and mumps cases in NYC')
plt.plot(x, y1,'g*:')
plt.yscale("log")
plt.plot(x, y, 'b*-')
plt.xlabel('Year')
plt.ylabel('Number of cases')
# complete this part

plt.show()

#%% Q3 plot average measles cases for each month of the year
x2 = []
y2 = []
y3 = []

for row in measles:
    x2.append(row[0])
    y2 = np.array([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]])
    y3.append(average(y2[axis = 0]))

plt.figure()
plt.plot(x2, y3)
plt.title('Fig 3: Average monthly measle cases')
plt.xlabel('Year')
plt.ylabel('Average number of cases')
# complete this part

plt.show()


#%% Q4 plot monthly measles cases against mumps cases 

plt.figure()
plt.title('Fig 4: Monthly measles vs mumps cases')

# complete this part

plt.show()


#%% Q5 plot monthly measles cases against mumps cases in log scale
plt.figure()
plt.title('Fig 5: Monthly measles vs mumps cases (log scale)')

# complete this part

plt.show()


#%% Q6 plot annual total chicken pox cases in each year

plt.figure()
plt.title('Fig 6: NYC chicken pox cases')
x = []
y = []

for row in chickenPox:
    x.append(row[0])
    y.append(row[1] + row[2] + row[3] + row [4] + row[5] + row[6] + row[7] + row[8] + row[9] + row[10] + row[11] + row[12])

x.sort()
plt.plot(x, y,'*-')
# complete this part

plt.show()
