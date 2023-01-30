# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 11:48:14 2021

@author: klaus
Oxygen utilization in lakes/ocean 
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
TEMP = 23.5
SALT = 0.2
T0_Kelvin = 273.15 ;
a_0 = 2.00907  ;      
a_1 = 3.22014  ;     
a_2 = 4.05010  ;      
a_3 = 4.94457  ;      
a_4 = -2.56847e-1 ;      
a_5 = 3.88767 ;      
b_0 = -6.24523e-3 ;      
b_1 = -7.37614e-3 ;      
b_2 = -1.03410e-2 ;      
b_3 = -8.17083e-3 ;
c_0 = -4.88682e-7 ;
#%%
TS = np.log( ((T0_Kelvin + 25.0) - TEMP) / (T0_Kelvin + TEMP) ) ;      
oxyarg=a_0+TS*(a_1+TS*(a_2+TS*(a_3+TS*(a_4+TS*a_5))))+SALT*(b_0+TS*(b_1+TS*(b_2+TS*b_3))+SALT*c_0) ;      

O2SAT = np.exp(oxyarg) 
#Convert from ml/l to mg/L%;   
O2SAT = O2SAT/0.7 ;
#%%
O2 = [7.63,7.63,7.70,7.65,7.64,7.64,7.64,7.55,7.52,7.52,7.62,7.60,7.59,7.53,7.55]
AOU = O2SAT - O2
Depth = np.arange(0,-15,-1)
O2sat = [8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,
         8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,
         8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,8.484445230501295,]
#%%
 plt.figure(figsize=(10,2))
 plt.plot(AOU,Depth,label='[AOU]')
 plt.plot(O2sat,Depth,label='[O2SAT]')
 plt.plot(O2,Depth,label='[O2]')
 plt.title('[O2], [O2SAT] & [AOU] As a function of depth')
 plt.xlabel('O2 concentration [mg/L]')
 plt.ylabel('Depth (m)')
 plt.ylim(-14,0)
 plt.legend()
 plt.subplots_adjust(bottom=0.3)
#%%
