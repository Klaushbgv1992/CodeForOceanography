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
# NET PRIMARY PRODUCTION

'''Compute Primary Production Via Michaelis-Menton Kinetics
%  vmax : Maximal uptake
%  PO4 : phosphate concentration
%  rCP : redfield ratio c:p
%  T: temperature (C)
%  KS  : Half saturation constant
%  Vmax as function of temperature (Eppley et al.,1972)
'''
a1 = 20
a2 = 10 
a3 = (2*np.pi)/12
t = np.arange(1,13,1)
T = a1 + a2*np.cos(a3*(t-1) + np.pi )
#T=10.0 ;
KS =12.5;
KS_ = 6.1e-3 ;
PO4 = 25.   
rcp  =  116 ;
vmax = 0.85 * np.exp(0.063*T) ;
PO4h = 35
PO4l = 10

npp = rcp * vmax * PO4 * PO4 /(PO4 + KS) ;
npp_newKS = rcp * vmax * PO4 * PO4 /(PO4 + KS_) ;
npp_nut_h = rcp * vmax * PO4h * PO4h /(PO4h + KS)
npp_nut_l = rcp * vmax * PO4l * PO4l /(PO4l + KS)
#%%
plt.figure(figsize=(10,5))
plt.title('NPP over time')
plt.plot(t,npp,label='KS = 12.5, [PO4]=25', color='pink')
plt.plot(t,npp_nut_h,label='KS = 12.5, high [Phosphate Concentration]', color='yellow')
plt.plot(t,npp_newKS,label='Ks = 6.1e-3, [Phosphate Concentration]=25')
plt.plot(t,npp_nut_l,label='KS = 12.5, low [Phosphate Concentration]')
plt.ylabel('Net Primary Production (millimoles per litre)')
plt.xlabel('Months')
plt.xlim(1,12)
plt.legend()

