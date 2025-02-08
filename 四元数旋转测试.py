# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:24:48 2024

@author: zc1997
"""



import csv
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import io
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as mp    
import quaternion








    
#df = pd.read_csv(r'C:\Users\zc1997\Desktop\lark32_0723_chip2prism_2.csv',encoding='ANSI')
df = pd.read_csv(r'C:\Users\zc1997\Desktop\aaa.csv',encoding='ANSI')
source_data_array = df.values



G1 = [1	,2,	3,	4,	5,	6,	7,	8]
G2 = [9,	11,	13,	15,	17,	19,	21,	23]
G3 = [10,	12,	14,	16,	18,	20,	22,	24]
G4 = [25,	35,	45,	55,	65,	75,	85,	95]
G5 = [26,	36,	46,	56,	66,	76,	86,	96]
G6 = [27,	37,	47,	57,	67,	77,	87,	97]
G7 = [28,	38,	48,58,	68,	78,	88,	98]
G8 = [29,	39,	49,	59,	69,79,89,99]
G9 = [30,	40,	50,	60,	70,	80,	90,	100]
G10 =[ 31,	41,	51,	61,	71,	81,	91	,101]
G11 =[32,	42,	52,	62,	72,	82,	92	,102]
G12 = [33,	43,	53,	63,	73,	83,	93,	103]
G13 = [34,	44,	54,64,	74	,84,	94	,104]
G14 = [105,	107,	109,111,	113	,115,	117,	119]
G15 =[106,	108,	110,	112,	114	,116,	118,	120]
ADC_list = [G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15]

x_list = []
y_list = []
for i in range(len(ADC_list)):
    x = source_data_array[[xx-1 for xx in ADC_list[i]],0]
    y = source_data_array[[xx-1 for xx in ADC_list[i]],1]
    x_list.append(x)
    y_list.append(y)
    index_num = i%5
    plt.scatter(x,y,s=10,cmap='viridis',label = "转镜面编号-"+str(index_num))        
plt.legend(bbox_to_anchor=(1,1),#图例边界框起始位置
             loc="upper left",#图例的位置
             ncol=1,#列数
             mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
             borderaxespad=0,#坐标轴和图例边界之间的间距
             #title="转镜面序号",#图例标题
             shadow=False,#是否为线框添加阴影
             fancybox=True)#线框圆角处理参数
    #plt.scatter(emit_gamma_list, emit_phi_list)
plt.rcParams['font.sans-serif'] = ['SimHei']	# 显示中文
plt.rcParams['axes.unicode_minus'] = False		# 显示负号
my_y_ticks = np.arange(-10, 15, 2)
my_x_ticks = np.arange(-60, -59.25, 0.05)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

#plt.grid(which="major", alpha=0.5,linestyle='-.',c = 'red')
#plt.grid(which="minor", alpha=0.25,linestyle='--',c = 'blue')

plt.show()
