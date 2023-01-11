# import imp, sys, os
import cv2
from matplotlib.pyplot import imshow
import pyautogui
import numpy as np
from time import sleep
import os
import serial
import openpyxl 
from paddleocr import PaddleOCR, draw_ocr




# def serial_set(step):
#     '''
#     通过串口来控制旋转
    
#     '''
#     ser=serial.Serial('COM1',115200,timeout=0.5)
#     ser.open()
#     ord_str = "d1s2p"+step+"r1p0010e"
#     ser.write(ord_str.encode("gbk"))
#     sleep(10)


# def control_moto():    
#     global num
#     while num == 0:
#         pass
#         num = num+1
#     while num<=4:
#         serial_set("8000")
        
#         num = num+1
#     while num>4 and num<=54:
#         num = num+1
#     while num>54 and num<63:
#         num = num+1


a=abs(round(123.4*0.01524-8))
b = abs(round(-333.7*0.01524-8))
print(a,b)
# import pandas as pd
 
# list_data=[['786.6'], ['-2341.8'], ['99.99']]
# list_data = np.transpose(list_data)
# # 下面这行代码运行报错
# # list.to_csv('e:/testcsv.csv',encoding='utf-8')
# name=['power','peak_x','peak_y']
# test=pd.DataFrame(columns=name,data=list_data)#数据有三列，列名分别为one,two,three
# print(test)
# test.to_csv('testcsv.csv',encoding='gbk')


import re


string="25.23.222."

a = re.findall(r"-?\d+\.?\d*",string)[0]
print(type(a),a)



def serial_set(step):
    '''
    通过串口来控制旋转
    
    '''
    ser=serial.Serial('COM7',115200,timeout=0.5)
    # ser.open()

    ord_str = "d0s2p"+str(step).zfill(4)+"r1p0000e"
    # ord_str = 'd1s2p0000r0p0010e'
    print(ord_str)
    ser.write(ord_str.encode("gbk"))
    sleep(0.2)
    ser.close()

serial_set(1)




