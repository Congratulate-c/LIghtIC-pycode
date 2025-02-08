# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:59:32 2024

@author: zc1997
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy import io
import numpy as np
import math
import quaternion


wavelength = 1.55
ne = 1.5363
no = 1.5277
d = 45.05813953488403


def lag_data(n1,n2,d,l):
    a = 2*np.pi*d*(n1 - n2)/l
    a = a/np.pi
    return a
    
#a=lag_data(ne,no,d,1.55)

theta = np.deg2rad(20)   
axis = np.array([0,1,0])
q = np.quaternion(np.cos(theta/2), np.sin(theta/2) * axis[0], np.sin(theta/2) * axis[1], np.sin(theta/2) * axis[2]) #定义四元数：沿着转轴axis转theta角度
N = [-1,0,0]
point = quaternion.from_vector_part(N) #将一个点转换为四元数，实部为0
p_new = q * point * q.conjugate()   #旋转点，结果为四元数
p_new = quaternion.as_vector_part(p_new) #结果四元数转换为点，直接去掉实部即可



def quartz_outputangle(input_i,material):
    Ni = [-1,0,0]
    #Ni = [-1,0,0]
    eta = 1/material                         #1550nm波长在QUARTZ的折射率是1.444
    k = 1.0 - eta * eta * (1.0 - np.dot(Ni, input_i) * np.dot(Ni, input_i))
    R = np.dot(eta, input_i) -np.dot((np.dot(eta, np.dot(Ni, input_i)) + math.sqrt(k)),Ni)    
    return R

#w=quartz_outputangle([np.sqrt(1/2),np.sqrt(1/2),0],1.53)


phase_d = []
ice_angle = []

for i in range(21):
    
    deg = np.deg2rad(i)
    w = quartz_outputangle([np.cos(deg),np.sin(deg),0],ne)
    optic_l = d/np.sin(np.arctan(w[0]/w[1]))
    #print(optic_l)
    a=lag_data(ne,no,optic_l,1.55)*180
    phase_d.append(a)
    ice_angle.append(i)
for i in np.linspace(21,40,20):
    delta = -2
    delta = -0
    deg = np.deg2rad(i)
    w = quartz_outputangle([np.cos(deg),np.sin(deg),0],ne)
    optic_l = d/np.sin(np.arctan(w[0]/w[1]))
    #print(optic_l)
    a=(lag_data(ne,no,optic_l+delta,1.55))*180
    phase_d.append(a)
    ice_angle.append(i)
    
for i in np.linspace(41,60,20):
    delta = -6
    delta = -0
    deg = np.deg2rad(i)
    w = quartz_outputangle([np.cos(deg),np.sin(deg),0],ne)
    optic_l = d/np.sin(np.arctan(w[0]/w[1]))
    #print(optic_l)
    a=(lag_data(ne,no,optic_l+delta,1.55))*180
    phase_d.append(a)
    ice_angle.append(i)
    
        
    
    
plt.scatter(ice_angle, phase_d)    
