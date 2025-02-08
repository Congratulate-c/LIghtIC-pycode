# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:35:28 2024

@author: zc
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy import io
import numpy as np
import math
import quaternion

def cosd(a):
    '''
    角度化弧度
    '''
    c = np.cos(np.deg2rad(a))    
    return c
def sind(a):
    c = np.sin(np.deg2rad(a))    
    return c
def unit(a):
    vec = a
    # 计算向量的模长
    vec_norm = np.linalg.norm(vec)
    # 将向量转化为单位向量
    unit_vec = vec / vec_norm
    return(unit_vec)
def Quaternion_rotation(p,theta,zhou):
    #theta = np.deg2rad(-9.8272)  #转角9.827° 
    theta = np.deg2rad(theta)   #Hawaii版本
    #theta = np.deg2rad(-4.8027)
    axis = np.array(zhou)#转轴：z轴
    q = np.quaternion(np.cos(theta/2), np.sin(theta/2) * axis[0], np.sin(theta/2) * axis[1], np.sin(theta/2) * axis[2]) #定义四元数：沿着转轴axis转theta角度
    
    point = p
    point = quaternion.from_vector_part(point) #将一个点转换为四元数，实部为0
    p_new = q * point * q.conjugate()   #旋转点，结果为四元数
    p_new = quaternion.as_vector_part(p_new) #结果四元数转换为点，直接去掉实部即可
    return p_new
#%%模块出光，定义多个通道
def beam_in_module(nums,full_angle):
    channel_nums = nums
    field = np.linspace(full_angle/2, -full_angle/2, channel_nums)
    return field
#%%楔形晶体 角度为1°
def wedge_d_offset(input_i,degree,material):   
    wedge_d = degree
    N = [sind(wedge_d),-cosd(wedge_d),0]
    eta = 1/material                           #1550nm波长在QUARTZ的折射率是1.444
    k = 1.0 - eta * eta * (1.0 - np.dot(N, input_i) * np.dot(N, input_i))
    R = np.dot(eta, input_i) -np.dot((np.dot(eta, np.dot(N, input_i)) + math.sqrt(k)),N)
    R = unit(R)
    return R
#%%整形棱镜，角度为-43.27164°
def prims3_d_shaping(input_i,degree,material):
    prims3_d = degree
    N2 = [-cosd(prims3_d),sind(prims3_d),0]
    eta2 = material/1                           #1550nm波长在QUARTZ的折射率是1.444
    k2 = 1.0 - eta2 * eta2 * (1.0 - np.dot(N2, input_i) * np.dot(N2, input_i))
    R2 = np.dot(eta2, input_i) -np.dot((np.dot(eta2, np.dot(N2, input_i)) + math.sqrt(k2)),N2)
    R2 = unit(R2)
    return R2
#%%振镜的法线旋转
def golva_angle(angle,beam_offset):
    #c = 31.8231
    c = 31.6355+beam_offset
    #c = 30.85
    #c = 32
    theta = angle
    golva_axis = [sind(c),cosd(c),0]
    #再绕x周转
    #golva_axis = [sind(c),cosd(c)*cosd(2),-sind(2)*cosd(c)]
    #golva_axis = [1,0,0]
    q = np.quaternion(cosd(theta/2), sind(theta/2) * golva_axis[0], sind(theta/2) * golva_axis[1], sind(theta/2) * golva_axis[2]) #定义四元数：沿着转轴axis转theta角度
    #qq是q的逆
    qq = np.quaternion(cosd(theta/2), -sind(theta/2) * golva_axis[0], -sind(theta/2) * golva_axis[1], -sind(theta/2) * golva_axis[2]) #定义四元数：沿着转轴axis转theta角度
    #q = np.quaternion(np.cos(theta/2), np.sin(theta/2) * axis[0], np.sin(theta/2) * axis[1], np.sin(theta/2) * axis[2])
    N_vec = [cosd(c),-sind(c),0]
    #N_vec = [0,cosd(45),sind(45)]
    point = quaternion.from_vector_part(N_vec)
    p_new = q * point * q.conjugate()   #旋转点，结果为四元数
    p_new = quaternion.as_vector_part(p_new) #结果四元数转换为点
    p_new = unit(p_new)
    return p_new
#%%反射向量计算
#R = I - 2.0 * dot(N, I) * N;
def ref_vec_cal(N,I):
    a = np.dot(N,I)*2
    b = np.dot(a,N)
    r = I-b
    r = unit(r)
    return r
#%%计算棱镜法线与法线面交点
beam_nums = 8
full_angle = 5.6
beam_out_vec = []
prims_normal_unit_vector_all = []
prims_reflector_normal_intersection_all = []
hor_pionts = 21
beam_offset = 0
#golva_angle_list = [-0.1865,-0.1,-0.0137,0.0727,0.1591]*3
#golva_angle_list = [-0.1757,-0.0892,-0.0029,0.0835,0.1699]*3
#golva_angle_list = [-5.648126,-2.424046,-2.07222,0.837743,0.880165,0.922588,0.96501,1.007432,1.049854,1.09699,1.139412,1.181834,1.224256,4.255080,4.471904]
#golva_angle_list = [-5.823694,-2.598,-2.383662,0.6604292,0.7043245,0.7461575,0.7897582,0.831885,0.874897,0.919381,0.9615094,1.005110,1.0466485,4.0801344,4.29519171]
#golva_angle_list = [-5.8147,-2.6,-2.3843,0.6576,0.7007,0.7439,0.787,0.8301,0.8732,0.9164,0.9595,1.0027,1.0458,4.0877,4.3035]
#golva_angle_list = [-2.6725,-2.5284,-2.3843,0.6576,0.7007,0.7439,0.787,0.8301,0.8732,0.9164,0.9595,1.0027,1.0458,4.0877,4.3035]
#golva_angle_list = [-2.24389,-2.09975,-1.95561,0.6576,0.7007,0.7439,0.787,0.8301,0.8732,0.9164,0.9595,1.0027,1.0458,3.65901,3.8748]
#golva_angle_list = [0.156,0.3,0.444,3.655,3.871]*3 #0.156,0.3,0.444,3.655,3.871
#golva_angle_list = [1.4955,1.5243,1.5531,1.5819,1.6107,1.6395,1.6683,1.6972,1.726,1.7548,1.7836,1.8124,1.8412,1.870,1.8988]
#golva_angle_list = [-5.0936,-2.3051,-2.0907,0.6576,0.7007,0.7439,0.787,0.8301,0.8732,0.9164,0.9595,1.0027,1.0458,3.7872, 4.0023]
golva_angle_list = [-3.42500,
-2.35100,
0.00000,
0.92700,
0.99900,
1.07100,
1.14300,
1.21450,
3.42500,
4.48100,
-3.42500,
-2.35100,
0.00000,
0.92700,
0.99900]





#3.397,0,-3.397, 3.1862, -0.1108,-0.1108-0.1054,-0.1108-0.1054*2,
#golva_angle_list = [ 3.397,0,-3.405, 3.1862, -0.1108,-0.1108-0.1054,-0.1108-0.1054*2,-3.405-0.1054,-3.405-0.1054*2,-3.405-0.1054*3]*2
#prims5_alpha_list = [50.2558]
zero_filed = 49.891 +beam_offset
prims5_alpha_list = np.linspace(zero_filed-30,zero_filed+30,hor_pionts)
#prims5_alpha_list = np.full(hor_pionts,72)
#prims5_alpha_list =  np.linspace(49.855-30,49.855+30,hor_pionts)  #49.855在垂直方向0°时候，对应水平0°
Beam_out_vec = []





for i in range(hor_pionts):

    #计算棱镜转动过程中在XoY面的法线与反射面交点坐标
    #棱镜的旋转轴相对于原点坐标是[-62.71,-30.54,0]
    #棱镜的旋转轴相对于反射面距离是25.46
    dis_midton = 25.46
    prims_normal_vector = [-cosd(prims5_alpha_list[i]),sind(prims5_alpha_list[i]),0]
    prims_normal_unit_vector = prims_normal_vector/np.linalg.norm(prims_normal_vector)
    prims_normal_unit_vector_all.append(prims_normal_unit_vector)
    prims_reflector_normal_intersection = [62.71,-30.54,0]+np.dot(prims_normal_unit_vector,dis_midton)
    #prims_reflector_normal_intersection = [0,0,0]+np.dot(prims_normal_unit_vector,dis_midton)
    prims_reflector_normal_intersection_all.append(prims_reflector_normal_intersection)
#%%开始啦
#%% 镜头出光光束指向
#fov_list_1 = [-2.78073]*8
#fov_list_1 = [0.38+0.76*3,0.38+0.76*2,0.38+0.76,0.38,-0.38,-0.38-0.76,-0.38-0.76*2,-0.38-0.76*3]
#fov_list_1 = [1.33,0.95,0.57,0.19,-0.19,-0.57,-0.95,-1.33]
fov_list_1 = [2.78073,1.98757,1.19305,0.39777,-0.39777,-1.19305,-1.98757,-2.78073]
#fov_list_1 = [1.98757,1.98757,1.19305,0.39777,-0.39777,-1.19305,-1.98757,-2.78073]
#Compensation_Angle = [-0.01981/4,-0.00981/4,-0.00323/2,0,0,-0.00323/2,-0.00981/4,-0.01981/4]
Compensation_Angle = [0]*8
#fov_list_1 = [-0.39777,-1.19305,-1.98757,-2.78073,-0.39777,-1.19305,-1.98757,-2.78073]
#fov_list_1 = [0]
#for i in beam_in_module(beam_nums, full_angle):
for i in fov_list_1:    
    I = [0,cosd(i),sind(i)]
    I2 = wedge_d_offset(I, -1, 1.443)   #前级补偿楔形角度 -1 °
    #I2 = Quaternion_rotation(I2,Compensation_Angle[int(i)],[0,0,1])
    
    
    I3 = prims3_d_shaping(I2, -46.7284, 1.443)   # 46.7284 
    V1 = np.arctan(I3[2]/I3[1])*180/np.pi 
    V2 = 90-np.arccos(I3[0])*180/np.pi
    beam_out_vec.append(I3)

prims_beam_location_all = []
goval_beam_all = []




for i in beam_out_vec:
    for j in golva_angle_list:
        for k in range(hor_pionts):
            n1 = golva_angle(j,beam_offset)
            i2 = ref_vec_cal(n1, i)     #振镜出光
            goval_beam_all.append(i2)
            lens_emit_x = i2[0]
            lens_emit_y = i2[1]
            lens_emit_z = i2[2]
            vpt = prims_normal_unit_vector_all[k][0]*lens_emit_x+prims_normal_unit_vector_all[k][1]*lens_emit_y+prims_normal_unit_vector_all[k][2]*lens_emit_z
            t1 = prims_normal_unit_vector_all[k][0]*(prims_reflector_normal_intersection_all[k][0])+prims_normal_unit_vector_all[k][1]*prims_reflector_normal_intersection_all[k][1]+prims_normal_unit_vector_all[k][2]*prims_reflector_normal_intersection_all[k][2]
            t = t1/vpt
            x_location = i2[0]*t
            y_location = i2[1]*t
            z_location = i2[2]*t
            prims_beam_location = np.array([x_location,y_location,z_location])
            prims_beam_location_all.append(prims_beam_location) 
            
            
            n2 = [-cosd(prims5_alpha_list[k]),sind(prims5_alpha_list[k]),0]   #棱镜法线旋转
            
            theta2 = np.deg2rad(0)   
            axis2 = np.array([1,0,0])#转轴：z轴
            q = np.quaternion(np.cos(theta2/2), np.sin(theta2/2) * axis2[0], np.sin(theta2/2) * axis2[1], np.sin(theta2/2) * axis2[2]) #定义四元数：沿着转轴axis转theta角度
            point = quaternion.from_vector_part(n2) 
            p_new = q * point * q.conjugate()   
            n2 = quaternion.as_vector_part(p_new)
            
            
            i3 = ref_vec_cal(n2, i2)    #棱镜出光+++++
            Beam_out_vec.append(i3)           
emit_phi_list = np.array([90-np.arccos(x[2])*180/np.pi for x in Beam_out_vec])
emit_gamma_list = np.array([np.arctan(x[0]/x[1])*180/np.pi for x in Beam_out_vec])

#%%
#计算旋转轴心指向落点的单位向量r
prims_beam_location_all = np.array(prims_beam_location_all)
dir_vector = np.array([x-[62.71,-30.54,0] for x in prims_beam_location_all])

prims_norm_r = np.array([np.linalg.norm(x)/1000 for x in dir_vector])
prims_unit_vector_r = np.array([x/np.linalg.norm(x) for x in dir_vector])

#转镜的线速度计算
prims_speed = 16
sum_points = beam_nums * len(golva_angle_list)*len(prims5_alpha_list)
linear_velocity = []
return_doppler_f = []
emitting_doppler_f = []
point_speed = np.array([[0,0,-x*2*np.pi*prims_speed] for x in prims_norm_r])
for i in range(sum_points):
      linear_velocity.append(np.cross(point_speed[i],prims_unit_vector_r[i]))

#回程的多普勒频移量计算
lens_beam_emit_unit_vector_all_t = np.array([-x for x in goval_beam_all])
for i in range(sum_points):
    return_doppler_f.append((np.dot(linear_velocity[i],lens_beam_emit_unit_vector_all_t[i]))/(1550*1e-9)*2)
    #return_doppler_f.append((np.dot(linear_velocity[i],lens_beam_emit_unit_vector_all_t[i]))/1*2)
#去程的多普勒频移量计算
for i in range(sum_points):
    emitting_doppler_f.append((np.dot(linear_velocity[i],Beam_out_vec[i]))/(1550*1e-9)*2)
    #emitting_doppler_f.append((np.dot(linear_velocity[i],Beam_out_vec[i]))/1*2)
#%%
#根据循环将38464*1的列向量转为一个64*604的矩阵形式

# 120lines


ADC1 = [1, 9, 10, 25, 26, 27, 28, 29,30,31,32,33,34,105,106]
ADC2 = [2, 11, 12, 35, 36, 37,38, 39,40,41,42,43,44,107,108]
ADC3 = [3, 13,14,45,46,47,48,49,50,51,52,53,54,109,110]
ADC4 = [4, 15,16,55,56,57,58,59,60,61,62,63,64,111,112]
ADC5 = [5, 17,18,65,66,67,68,69,70,71,72,73,74,113,114]
ADC6 = [6, 19,20,75,76,77,78,79,80,81,82,83,84,115,116]
ADC7 = [7, 21,22,85,86,87,88,89,90,91,92,93,94,117,118]
ADC8 = [8, 23,24,95,96,97,98,99,100,101,102,103,104,119,120]
ADC_list = [ADC1,ADC2,ADC3,ADC4,ADC5,ADC6,ADC7,ADC8]

# 80lines

XIANSHU = len(fov_list_1)*len(golva_angle_list)

    
def sort_data(data):
    result_data= np.zeros([XIANSHU,hor_pionts])
    for i in range(8):
        ADC = ADC_list[i]
        print(ADC)
        for index,j in enumerate(ADC):
            result_data[j-1,:] = data[hor_pionts*(index+len(ADC1)*i):hor_pionts*(index+len(ADC1)*i+1)]
    return result_data

emit_phi_list = np.array([90-np.arccos(x[2])*180/np.pi for x in Beam_out_vec])
emitting_phi_array = sort_data(emit_phi_list)
emit_gamma_list = np.array([np.arctan(x[0]/x[1])*180/np.pi for x in Beam_out_vec])
emitting_gamma_array = sort_data(emit_gamma_list)
Doppler_compensation_value = sort_data(return_doppler_f)+sort_data(emitting_doppler_f)

#%%
index1 = np.where(emit_phi_list>7.8)[0]
index2 = np.where((emit_phi_list>2) &(emit_phi_list<7.7))[0]
index3 = np.where((emit_phi_list>-4.8) &(emit_phi_list<2))[0]
index4 = np.where(emit_phi_list<-5)[0]

#绘图
#figure1 水平及垂直角度值指向角度关系图

plt.figure(figsize=(15, 10), dpi=100)
plt.scatter(emit_gamma_list[index1], emit_phi_list[index1],c='blue',s=10,cmap='viridis')
plt.scatter(emit_gamma_list[index2], emit_phi_list[index2],c='red',s=10,cmap='viridis')
plt.scatter(emit_gamma_list[index4], emit_phi_list[index4],c='red',s=10,cmap='viridis')
plt.scatter(emit_gamma_list[index3], emit_phi_list[index3],c='green',s=10,cmap='viridis')
plt.xlabel('Horizontal/°', fontsize=14)
plt.ylabel('vertical/°', fontsize=14)
#plt.scatter(emit_gamma_list, emit_phi_list)
plt.show()


plt.figure(figsize=(15, 10), dpi=100)
plt.scatter(emit_gamma_list, emit_phi_list,c='blue',s=10,cmap='viridis')

plt.xlabel('Horizontal/°', fontsize=14)
plt.ylabel('vertical/°', fontsize=14)
#plt.scatter(emit_gamma_list, emit_phi_list)
plt.show()


#%%figure2绘制多普勒
#3D绘图示意

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as mp    
x3d = []
y3d = []
z3d = []
fig2 = mp.figure("3D Scatter", facecolor="lightgray")
ax3d2 = fig2.add_subplot(projection="3d")  # 创建三维坐标
mp.title('3D Scatter', fontsize=20)
ax3d2.set_xlabel('x', fontsize=14)
ax3d2.set_ylabel('y', fontsize=14)
ax3d2.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
for i in range(len(Beam_out_vec)):
    p2 = Beam_out_vec[i]*6
    x3d.append(p2[0])
    y3d.append(p2[1])
    z3d.append(p2[2]) 
ax3d2.scatter(x3d, y3d, z3d, s=5, cmap="jet", marker="o")
mp.show() 



emitting_doppler_array = sort_data(emitting_doppler_f)
return_doppler_array = sort_data(return_doppler_f)
plt.figure(figsize=(15, 10), dpi=100)
plt.xlabel('Horizontal/°', fontsize=14)
plt.ylabel('Doppler_compensation_value/ m*s-1', fontsize=14)
id_index1 = 0
for i in range(1):
    Any_1 = Doppler_compensation_value[id_index1,:]
    gamma_list = emitting_gamma_array[id_index1,:]
    Any_2 = emitting_doppler_array[id_index1,:]
    Any_3 = return_doppler_array[id_index1,:]
    z1 = gamma_list
    z2 = Any_1
    plt.scatter(gamma_list,Any_2,s=10,cmap='viridis',label = '去程')
    plt.scatter(gamma_list,Any_3,s=10,cmap='viridis',label = '回程')
    plt.scatter(gamma_list,Any_1,s=10,cmap='viridis',label = '回程+去程')
plt.legend(bbox_to_anchor=(1,1),#图例边界框起始位置
             loc="upper right",#图例的位置
             ncol=1,#列数
             mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
             borderaxespad=0,#坐标轴和图例边界之间的间距
             title="频移量类型",#图例标题
             shadow=False,#是否为线框添加阴影
             fancybox=True)#线框圆角处理参数
    #plt.scatter(emit_gamma_list, emit_phi_list)
plt.rcParams['font.sans-serif'] = ['SimHei']	# 显示中文
plt.rcParams['axes.unicode_minus'] = False		# 显示负号
plt.show()

