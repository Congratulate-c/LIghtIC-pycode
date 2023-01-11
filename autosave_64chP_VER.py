import cv2
from matplotlib.pyplot import imshow
import pyautogui
import numpy as np
from time import sleep
import os, sys
import serial
import openpyxl 
from paddleocr import PaddleOCR, draw_ocr
import pandas as pd
import datetime
import re


#by zc
#整机能量测试（光斑是沿着垂直方向排布的）




peak_x = []
peak_y = []
power_dbm = []


def screen_capture():
    '''
    截取beamscaner当前的测试界面
    '''
    img_name = 'currendt_img.png'
    img_name2 = 'valid_data_img.png'
    img = pyautogui.screenshot(img_name)
    img2 = pyautogui.screenshot(img_name2,region=(938, 215, 80 ,120))

def read_img(path):
    '''
    读取截图信息
    '''
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # need to run only once to download and load model into memory
    img_path = path
    result = ocr.ocr(img_path, cls=True)
    peak_x = result[0][0][1][0]
    peak_y = result[0][1][1][0]
    total_power = result[0][5][1][0]
    return peak_x,peak_y,total_power
    print(peak_x,peak_y,total_power)



def serial_set(step):
    '''
    通过串口来控制旋转
    
    '''
    ser=serial.Serial('COM7',115200,timeout=0.5)
    # ord_str = "d1s2p0000r1p"+str(step).zfill(4)+"e"
    
    ser.write(step.encode("gbk"))
    sleep(1)

def control_motor():
    '''
    
    控制电机进行粗调、精调以及读数存储
    
    '''
    global num
    global peak_x
    global peak_y
    global power_dbm
    global save_img
    while num == 1:
        elaboration_motor(3)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1200,155,665,665))
        num = num+1
        print('------------->',num)
    while num>=2 and num<=3:
        ord_str3 = 'd1s2p0310r1p0000e'
        serial_set(ord_str3)
        sleep(6)
        elaboration_motor(4)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1243,155,665,665))
        num = num+1
        print('------------->',num)
    while num==4 :
        ord_str4 = 'd1s2p0200r1p0000e'
        serial_set(ord_str4)
        sleep(6)
        elaboration_motor(4)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1243,155,665,665))
        num = num+1
        print('------------->',num)   

    while num == 5:
        ord_str5 = 'd1s2p0100r1p0000e'
        serial_set(ord_str5)
        sleep(6)
        elaboration_motor(4)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1243,155,665,665))
        num = num+1
        print('------------->',num)         
    while num>=6 and num<=54:
        ord_str61 = 'd1s2p0018r1p0000e'
        serial_set(ord_str61)
        sleep(4)
        elaboration_motor(2)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1243,155,665,665))
        num = num+1
        print('------------->',num)
    while num >= 55 and num<=64:
        ord_str7 = 'd1s2p0080r1p0000e'
        serial_set(ord_str7)
        sleep(6)
        elaboration_motor(3)
        x,y,p=verify_data()
        peak_x.append(x)
        peak_y.append(y)
        power_dbm.append(p)
        pyautogui.screenshot(t_str+str(num)+'.png',region=(1243,155,665,665))
        num = num+1
        print('------------->',num)
    while num == 65:
        print('------------->',num)
        break

def verify_data():
    
    '''
    读取有效数据
    '''
    
    screen_capture()
    x,y,power = read_img(path="valid_data_img.png")
    return x,y,power

def elaboration_motor(i):
    
    '''
    
    i表示精调的测试
    
    '''
    
    while i>0:
        x,y,p=verify_data()
        x = float(re.findall(r"-?\d+\.?\d*",x)[0])
        y = float(re.findall(r"-?\d+\.?\d*",y)[0])
        p = float(re.findall(r"-?\d+\.?\d*",p)[0])
        # print(x,y)
        if x>0 and y>0:
            x_str ='r0'
            y_str = 'd0'
        if x>0 and y<0:
            x_str ='r0'
            y_str = 'd1'
        if x<0 and y<0:
            x_str ='r1'
            y_str = 'd1'
        if x<0 and y>0:
            x_str ='r1'
            y_str = 'd0'
        if abs(x)+abs(y)<6000:
            if abs(x)>500 :
                x = abs(round(x*0.01524-8))
                y = abs(round(y*0.006226-0.676))
            elif abs(x)<500 and abs(x)>200:
                x = 3
                y = abs(round(y*0.006226-0.676))

            else  :
                y = 1
                x = 1
            # if abs(x)<100 and abs(y)<100:
            #     x = 0
            #     y = 0
            ord_str = y_str+'s2p'+str(y).zfill(4)+x_str+'p'+'0000'+'e'
            ord_str2 = y_str+'s2p'+'0000'+x_str+'p'+str(x).zfill(4)+'e'
            serial_set(ord_str)

            # print(ord_str,ord_str2)
            sleep(4)
            serial_set(ord_str2)
            sleep(4)    
            i=i-1    
        else:
            sys.exit()   
    print(ord_str)

# def save_data():

#     pass

if __name__ == '__main__' :
    sleep(1)
    print('-------------------------->开始测试记录')
    t_str=datetime.datetime.now().strftime('%Y-%m-%d')
    num = 1
    save_img = t_str+'-'+str(num)+'.png'
    control_motor()
    list_data=[peak_x,peak_y,power_dbm]
    list_data = np.transpose(list_data)
    column_name = ['peak_x','peak_y','power_dbm']
    print()
    save_data = pd.DataFrame(columns=column_name,data=list_data)
    save_data.to_csv(t_str+'_power_save.csv',encoding='gbk')
    print('-------------------------->完成测试')


    