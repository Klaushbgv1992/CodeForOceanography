# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 11:48:14 2021

@author: klaus
Lokta and Voltera model to estimate populations of predators (N2) and prey (N1).  
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
#%%

#%%% LAST one BABYYYY
# Program Locta Voltera
time_dat = [] ;
prey_dat = []
pred_dat = []
B1 = 0.1 ;
K1 = 0.01 ;
K2 = 0.0001 ;
D2 = 0.1 ;
T = 0. ;
TimeStep = 1. ;
N1 = 1000. ;
N2 = 11. ; #change here
#fprintf('Input T1 %d ', T) ;
#fprintf('Input N1 %d ',N1 ) ;
#fprintf('Input N2 %d ' , N2) ;
s =1000 ;

#%%
for t in range(1000):
    T = t;
    DN1 = (B1 * N1 * TimeStep) - (K1 * N1 * N2 * TimeStep) ;
    DN2 = (K2 * N1 * N2 * TimeStep) - (D2 * N2 * TimeStep) ;
    N1 = N1 + DN1 ;
    N2 = N2 + DN2 ;
    time_dat.append(T)
    prey_dat.append(N1)
    pred_dat.append(N2)
    if N1 < 1: 
        break
    if N2 < 1: 
        break
#%%
plt.figure()
plt.title('1000 prey vs 11 predators')
#plt.subplot(2,1,1)
plt.plot(time_dat, pred_dat, color='red')
plt.xlabel('Over Time')
plt.xlim(0,1000)
plt.ylabel('Population N')
plt.title('Predators') 

#plt.subplot(2,1,2)
plt.figure()
plt.title('1000 prey vs 11 predators')
plt.plot(time_dat, prey_dat, color='red')
plt.xlim(0,1000)
plt.ylabel('Population N')
plt.title('Prey') 
#plt.subplots_adjust(hspace=0.8)
#%%
plt.figure()
#plt.suptitle('Lotka-Voltera phase diagram showing predator and prey abundance')
plt.title('Lotka-Voltera phase diagram showing predator and prey abundance')
#plt.subplot(2,1,1)
plt.plot(prey_dat,pred_dat)
plt.ylabel('Predators')
plt.xlabel('Prey')
plt.title('10 predators vs 1000 prey')

#plt.subplot(2,1,2)
plt.title('Lotka-Voltera phase diagram showing predator and prey abundance')
plt.plot(prey_dat,pred_dat, color='red')
plt.ylabel('Predators')
plt.xlabel('Prey')
plt.title(' 11 predators vs 1000 prey')
plt.subplots_adjust(hspace=0.4)