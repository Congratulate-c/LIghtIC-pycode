# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\code\PYTHON_CODE\fmlb\lark\扫描pattern\fov_pattern20230829.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy import io
import numpy as np
import math
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph as pg
import random
from math_sanjiao import *
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph.opengl as gl
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 1299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 1299))
        MainWindow.setMaximumSize(QtCore.QSize(1001, 1300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 320, 971, 881))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 971, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Channel_nums = QtWidgets.QSpinBox(self.layoutWidget)
        self.Channel_nums.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.Channel_nums.sizePolicy().hasHeightForWidth())
        self.Channel_nums.setSizePolicy(sizePolicy)
        self.Channel_nums.setMinimumSize(QtCore.QSize(72, 45))
        self.Channel_nums.setObjectName("Channel_nums")
        self.verticalLayout_2.addWidget(self.Channel_nums)
        self.ifov = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.ifov.sizePolicy().hasHeightForWidth())
        self.ifov.setSizePolicy(sizePolicy)
        self.ifov.setMinimumSize(QtCore.QSize(20, 0))
        self.ifov.setObjectName("ifov")
        self.verticalLayout_2.addWidget(self.ifov)
        self.ifov_2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(72)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.ifov_2.sizePolicy().hasHeightForWidth())
        self.ifov_2.setSizePolicy(sizePolicy)
        self.ifov_2.setMinimumSize(QtCore.QSize(10, 0))
        self.ifov_2.setObjectName("ifov_2")
        self.verticalLayout_2.addWidget(self.ifov_2)
        self.FOV_T = QtWidgets.QSpinBox(self.layoutWidget)
        self.FOV_T.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.FOV_T.sizePolicy().hasHeightForWidth())
        self.FOV_T.setSizePolicy(sizePolicy)
        self.FOV_T.setMinimumSize(QtCore.QSize(72, 45))
        self.FOV_T.setObjectName("FOV_T")
        self.verticalLayout_2.addWidget(self.FOV_T)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 230, 971, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Angle1 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle1.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle1.setDecimals(3)
        self.Angle1.setSingleStep(0.001)
        self.Angle1.setObjectName("Angle1")
        self.horizontalLayout_2.addWidget(self.Angle1)
        self.checkBox_angle1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle1.setText("")
        self.checkBox_angle1.setObjectName("checkBox_angle1")
        self.horizontalLayout_2.addWidget(self.checkBox_angle1)
        self.Angle2 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle2.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle2.setDecimals(3)
        self.Angle2.setSingleStep(0.001)
        self.Angle2.setObjectName("Angle2")
        self.horizontalLayout_2.addWidget(self.Angle2)
        self.checkBox_angle2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle2.setText("")
        self.checkBox_angle2.setObjectName("checkBox_angle2")
        self.horizontalLayout_2.addWidget(self.checkBox_angle2)
        self.Angle3 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle3.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle3.setDecimals(3)
        self.Angle3.setSingleStep(0.001)
        self.Angle3.setObjectName("Angle3")
        self.horizontalLayout_2.addWidget(self.Angle3)
        self.checkBox_angle3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle3.setText("")
        self.checkBox_angle3.setObjectName("checkBox_angle3")
        self.horizontalLayout_2.addWidget(self.checkBox_angle3)
        self.Angle4 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle4.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle4.setDecimals(3)
        self.Angle4.setSingleStep(0.001)
        self.Angle4.setObjectName("Angle4")
        self.horizontalLayout_2.addWidget(self.Angle4)
        self.checkBox_angle4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle4.setText("")
        self.checkBox_angle4.setObjectName("checkBox_angle4")
        self.horizontalLayout_2.addWidget(self.checkBox_angle4)
        self.Angle5 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle5.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle5.setDecimals(3)
        self.Angle5.setSingleStep(0.001)
        self.Angle5.setObjectName("Angle5")
        self.horizontalLayout_2.addWidget(self.Angle5)
        self.checkBox_angle5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle5.setText("")
        self.checkBox_angle5.setObjectName("checkBox_angle5")
        self.horizontalLayout_2.addWidget(self.checkBox_angle5)
        self.Angle6 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle6.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle6.setDecimals(3)
        self.Angle6.setSingleStep(0.001)
        self.Angle6.setObjectName("Angle6")
        self.horizontalLayout_2.addWidget(self.Angle6)
        self.checkBox_angle6 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle6.setText("")
        self.checkBox_angle6.setObjectName("checkBox_angle6")
        self.horizontalLayout_2.addWidget(self.checkBox_angle6)
        self.Angle7 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle7.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle7.setDecimals(3)
        self.Angle7.setSingleStep(0.001)
        self.Angle7.setObjectName("Angle7")
        self.horizontalLayout_2.addWidget(self.Angle7)
        self.checkBox_angle7 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle7.setText("")
        self.checkBox_angle7.setObjectName("checkBox_angle7")
        self.horizontalLayout_2.addWidget(self.checkBox_angle7)
        self.Angle8 = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.Angle8.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle8.setDecimals(3)
        self.Angle8.setSingleStep(0.001)
        self.Angle8.setObjectName("Angle8")
        self.horizontalLayout_2.addWidget(self.Angle8)
        self.checkBox_angle8 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_angle8.setText("")
        self.checkBox_angle8.setObjectName("checkBox_angle8")
        self.horizontalLayout_2.addWidget(self.checkBox_angle8)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 280, 971, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Angle9 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle9.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle9.setDecimals(3)
        self.Angle9.setSingleStep(0.001)
        self.Angle9.setObjectName("Angle9")
        self.horizontalLayout_3.addWidget(self.Angle9)
        self.checkBox_angle9 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle9.setText("")
        self.checkBox_angle9.setObjectName("checkBox_angle9")
        self.horizontalLayout_3.addWidget(self.checkBox_angle9)
        self.Angle10 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle10.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle10.setDecimals(3)
        self.Angle10.setSingleStep(0.001)
        self.Angle10.setObjectName("Angle10")
        self.horizontalLayout_3.addWidget(self.Angle10)
        self.checkBox_angle10 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle10.setText("")
        self.checkBox_angle10.setObjectName("checkBox_angle10")
        self.horizontalLayout_3.addWidget(self.checkBox_angle10)
        self.Angle11 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle11.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle11.setDecimals(3)
        self.Angle11.setSingleStep(0.001)
        self.Angle11.setObjectName("Angle11")
        self.horizontalLayout_3.addWidget(self.Angle11)
        self.checkBox_angle11 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle11.setText("")
        self.checkBox_angle11.setObjectName("checkBox_angle11")
        self.horizontalLayout_3.addWidget(self.checkBox_angle11)
        self.Angle12 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle12.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle12.setDecimals(3)
        self.Angle12.setSingleStep(0.001)
        self.Angle12.setObjectName("Angle12")
        self.horizontalLayout_3.addWidget(self.Angle12)
        self.checkBox_angle12 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle12.setText("")
        self.checkBox_angle12.setObjectName("checkBox_angle12")
        self.horizontalLayout_3.addWidget(self.checkBox_angle12)
        self.Angle13 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle13.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle13.setDecimals(3)
        self.Angle13.setSingleStep(0.001)
        self.Angle13.setObjectName("Angle13")
        self.horizontalLayout_3.addWidget(self.Angle13)
        self.checkBox_angle13 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle13.setText("")
        self.checkBox_angle13.setObjectName("checkBox_angle13")
        self.horizontalLayout_3.addWidget(self.checkBox_angle13)
        self.Angle14 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle14.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle14.setDecimals(3)
        self.Angle14.setSingleStep(0.001)
        self.Angle14.setObjectName("Angle14")
        self.horizontalLayout_3.addWidget(self.Angle14)
        self.checkBox_angle14 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle14.setText("")
        self.checkBox_angle14.setObjectName("checkBox_angle14")
        self.horizontalLayout_3.addWidget(self.checkBox_angle14)
        self.Angle15 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle15.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle15.setDecimals(3)
        self.Angle15.setSingleStep(0.001)
        self.Angle15.setObjectName("Angle15")
        self.horizontalLayout_3.addWidget(self.Angle15)
        self.checkBox_angle15 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle15.setText("")
        self.checkBox_angle15.setObjectName("checkBox_angle15")
        self.horizontalLayout_3.addWidget(self.checkBox_angle15)
        self.Angle16 = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        self.Angle16.setMinimumSize(QtCore.QSize(90, 30))
        self.Angle16.setDecimals(3)
        self.Angle16.setSingleStep(0.001)
        self.Angle16.setObjectName("Angle16")
        self.horizontalLayout_3.addWidget(self.Angle16)
        self.checkBox_angle16 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_angle16.setText("")
        self.checkBox_angle16.setObjectName("checkBox_angle16")
        self.horizontalLayout_3.addWidget(self.checkBox_angle16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Angle1.setRange(-10,10)
        self.Angle2.setRange(-10,10)
        self.Angle3.setRange(-10,10)
        self.Angle4.setRange(-10,10)
        self.Angle5.setRange(-10,10)
        self.Angle6.setRange(-10,10)
        self.Angle7.setRange(-10,10)
        self.Angle8.setRange(-10,10)
        self.Angle9.setRange(-10,10)
        self.Angle10.setRange(-10,10)
        self.Angle11.setRange(-10,10)
        self.Angle12.setRange(-10,10)
        self.Angle13.setRange(-10,10)
        self.Angle14.setRange(-10,10)
        self.Angle15.setRange(-10,10)
        self.Angle16.setRange(-10,10)



        #视场参数
        self.ifov.textChanged.connect(lambda current_text: self.source_fov_show(self))
        self.Channel_nums.valueChanged.connect(lambda current_text: self.source_fov_show(self))
        

        #绘图
        #self.Channel_nums.valueChanged.connect(self.plot_slot)
        self.checkBox_angle1.stateChanged.connect(self.plot_show)
        self.Angle1.valueChanged.connect(self.huadong_plot_show)
        self.Angle2.valueChanged.connect(self.huadong_plot_show)
        self.Angle3.valueChanged.connect(self.huadong_plot_show)
        self.Angle4.valueChanged.connect(self.huadong_plot_show)
        self.Angle5.valueChanged.connect(self.huadong_plot_show)
        self.Angle6.valueChanged.connect(self.huadong_plot_show)
        self.Angle7.valueChanged.connect(self.huadong_plot_show)
        self.Angle8.valueChanged.connect(self.huadong_plot_show)
        self.Angle9.valueChanged.connect(self.huadong_plot_show)
        self.Angle10.valueChanged.connect(self.huadong_plot_show)
        self.Angle12.valueChanged.connect(self.huadong_plot_show)
        self.Angle13.valueChanged.connect(self.huadong_plot_show)
        self.Angle14.valueChanged.connect(self.huadong_plot_show)
        self.Angle15.valueChanged.connect(self.huadong_plot_show)
        self.Angle16.valueChanged.connect(self.huadong_plot_show)
        self.Angle11.valueChanged.connect(self.huadong_plot_show)
        self.FOV_T.valueChanged.connect(self.huadong_plot_show)
        self.Angle1.valueChanged.connect(self.show_text)
        self.Angle2.valueChanged.connect(self.show_text)
        self.Angle3.valueChanged.connect(self.show_text)
        self.Angle4.valueChanged.connect(self.show_text)
        self.Angle5.valueChanged.connect(self.show_text)
        self.Angle6.valueChanged.connect(self.show_text)
        self.Angle7.valueChanged.connect(self.show_text)
        self.Angle8.valueChanged.connect(self.show_text)
        self.Angle9.valueChanged.connect(self.show_text)
        self.Angle10.valueChanged.connect(self.show_text)
        self.Angle12.valueChanged.connect(self.show_text)
        self.Angle13.valueChanged.connect(self.show_text)
        self.Angle14.valueChanged.connect(self.show_text)
        self.Angle15.valueChanged.connect(self.show_text)
        self.Angle16.valueChanged.connect(self.show_text)
        self.Angle11.valueChanged.connect(self.show_text)
        self.FOV_T.valueChanged.connect(self.show_text)
        #全局变量
        self.field = 0
        self.emit_phi_list = 0
        self.emit_gamma_list = 0
        # 创建十字光标对象
    def shizixian(self):
        vLine = pg.InfiniteLine(angle=90, movable=False)
        hLine = pg.InfiniteLine(angle=0, movable=False)
        self.graphicsView.addItem(vLine, ignoreBounds=True)
        self.graphicsView.addItem(hLine, ignoreBounds=True)
        pos = self.graphicsView.mapFromScene(QtGui.QCursor.pos())
        vLine.setPos(pos.x())
        hLine.setPos(pos.y())





    # def check_box_onoff(self):
    #     nums = int(self.ifov_2.text())
    #     if nums == 1:
    #         self.checkBox_angle1.setCheckable(True)
    #     if nums == 2:
    #         self.checkBox_angle1.setCheckable(True)
    #         self.checkBox_angle2.setCheckable(True)

    def g_angle_list(self):
        angle1 = self.Angle1.value()
        angle2 = self.Angle2.value()
        angle3 = self.Angle3.value()
        angle4 = self.Angle4.value()
        angle5 = self.Angle5.value()
        angle6 = self.Angle6.value()
        angle7 = self.Angle7.value()
        angle8 = self.Angle8.value()
        angle9 = self.Angle9.value()
        angle10 = self.Angle10.value()
        angle11 = self.Angle11.value()
        angle12 = self.Angle12.value()
        angle13 = self.Angle13.value()
        angle14 = self.Angle14.value()
        angle15 = self.Angle15.value()
        angle16 = self.Angle16.value()
        angle_list = [angle1,angle2,angle3,angle4,angle5,angle6,angle7,angle8,angle9,angle10,angle11,angle12,angle13,angle14,angle15,angle16]
        return angle_list


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Lidar scan pattern"))
        self.label_2.setText(_translate("MainWindow", " Beam Nums"))
        self.label_3.setText(_translate("MainWindow", " Field Lens  "))
        self.label_4.setText(_translate("MainWindow", " Mirror"))
        self.label_5.setText(_translate("MainWindow", " FOV倾斜"))

    #%%楔形晶体 角度为1°
    def wedge_d_offset(input_i,degree,material,self):   
        wedge_d = degree
        N = [sind(wedge_d),-cosd(wedge_d),0]
        eta = 1/material                           #1550nm波长在QUARTZ的折射率是1.444
        k = 1.0 - eta * eta * (1.0 - np.dot(N, input_i) * np.dot(N, input_i))
        R = np.dot(eta, input_i) -np.dot((np.dot(eta, np.dot(N, input_i)) + math.sqrt(k)),N)
        R = unit(R)
        return R
    #%%整形棱镜，角度为-43.27164°
    def prims3_d_shaping(input_i,degree,material,self):
        prims3_d = degree
        N2 = [-cosd(prims3_d),sind(prims3_d),0]
        eta2 = material/1                           #1550nm波长在QUARTZ的折射率是1.444
        k2 = 1.0 - eta2 * eta2 * (1.0 - np.dot(N2, input_i) * np.dot(N2, input_i))
        R2 = np.dot(eta2, input_i) -np.dot((np.dot(eta2, np.dot(N2, input_i)) + math.sqrt(k2)),N2)
        R2 = unit(R2)
        return R2
    def ref_vec_cal(N,I,self):
        a = np.dot(N,I)*2
        b = np.dot(a,N)
        r = I-b
        r = unit(r)
        return r

    def show_text(self):
        self.graphicsView.scene().sigMouseMoved.connect(self.shizixian)
        self.emit_phi_list = 0
        self.emit_gamma_list = 0
        angle = self.Angle1.value()
        channel_nums = self.Channel_nums.value()
        total_field = np.float64(self.ifov.text())
        lens_beam_emit_unit_vector_all = []
        core_K = []
        emitting_XYZ_unit_vector_all = []
        theta = self.g_angle_list()
        #print(theta)
        field = list(self.field)
        #print(field,channel_nums)
        n = int(self.ifov_2.text())
        #print(n)
        hor_p = 21
        alpha = np.linspace(49.855-30,49.855+30,hor_p)
        beta = self.FOV_T.value()
        for j in range(n):
            for i in range(channel_nums):
                for k in range(hor_p):
                    i_INPUT = [0,cosd(field[i]),sind(field[i])]
                    print(i_INPUT)
                    I2 = self.wedge_d_offset(i_INPUT, -1, 1.444)
                    I3 = self.prims3_d_shaping(I2, -46.7284, 1.444)
                    #lens_emit_x = -cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])-cosd(field[i])/2
                    #lens_emit_y = cosd(field[i])/2 - cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])
                    #lens_emit_z = np.sqrt(2)/2*cosd(field[i])*sind(2*theta[j])+cosd(2*theta[j])*sind(field[i])


                    n1 = theta[j]
                    i2 = self.ref_vec_cal(n1, I3)     #振镜出光                  
                    n2 = [-cosd(alpha[k]),sind(alpha[k]),0]   #棱镜法线旋转
                    i3 = self.ref_vec_cal(n2, i2)    #棱镜出光
                    emitting_XYZ_vector = i3
                    emitting_XYZ_unit_vector = emitting_XYZ_vector/np.linalg.norm(emitting_XYZ_vector)
                    emitting_XYZ_unit_vector_all.append(emitting_XYZ_unit_vector)
        emit_phi_list = np.array([np.arctan(x[2])*57.3 for x in emitting_XYZ_unit_vector_all])
        emit_gamma_list = np.array([np.arctan(x[0]/x[1])*57.3 for x in emitting_XYZ_unit_vector_all])
        self.emit_phi_list = emit_phi_list
        self.emit_gamma_list = emit_gamma_list
        l = len(self.emit_gamma_list)
        num = l/20
        #print(num)
        # if num == 1:
        #     text=pg.TextItem()
        #     txt1 = 'x:'+str(round(self.emit_gamma_list[0],3))+'  y:'+str(round(self.emit_phi_list[0],3))
        #     text.setHtml('<font size="4" color="blue">%s</font>'%(txt1))
        #     text.setPos(self.emit_gamma_list[0]+1, self.emit_phi_list[0])
        #     self.graphicsView.addItem(text)
        for i in range(int(num)):
            text=pg.TextItem()
            n = i*20
            n = int(n)
            #print(type(self.emit_gamma_list),type(n),self.emit_gamma_list[n])
            txt1 = 'x:'+str(round(self.emit_gamma_list[n],3))+'  y:'+str(round(self.emit_phi_list[n],3))
            #print(str(round(self.emit_gamma_list[n],3)))
            text.setHtml('<font size="5" color="white">%s</font>'%(txt1))
            text.setPos(self.emit_gamma_list[n]+1, self.emit_phi_list[n])
            self.graphicsView.addItem(text)
        # if num ==2:
        #     text=pg.TextItem()
        #     txt1 = 'x:'+str(round(self.emit_gamma_list[0],3))+'  y:'+str(round(self.emit_phi_list[0],3))
        #     text.setHtml('<font size="4" color="blue">%s</font>'%(txt1))
        #     text.setPos(self.emit_gamma_list[0]+1, self.emit_phi_list[0])
        #     self.graphicsView.addItem(text)
        #     text2=pg.TextItem()
        #     txt2 = 'x:'+str(round(self.emit_gamma_list[20],3))+'  y:'+str(round(self.emit_phi_list[20],3))
        #     print(str(round(self.emit_gamma_list[20],3)),str(round(self.emit_phi_list[20],3)))
        #     text2.setHtml('<font size="4" color="blue">%s</font>'%(txt2))
        #     text2.setPos(self.emit_gamma_list[20]+1, self.emit_phi_list[20])
        #     self.graphicsView.addItem(text2)

        pass
    def plot_show(self):
        self.graphicsView.scene().sigMouseMoved.connect(self.shizixian)
        self.emit_phi_list = 0
        self.emit_gamma_list = 0
        angle = self.Angle1.value()
        channel_nums = self.Channel_nums.value()
        total_field = np.float64(self.ifov.text())
        lens_beam_emit_unit_vector_all = []
        core_K = []
        emitting_XYZ_unit_vector_all = []
        theta = self.g_angle_list()
        #print(theta)
        field = list(self.field)
        #print(field,channel_nums)
        n = int(self.ifov_2.text())
        #print(n)
        hor_p = 21
        alpha = np.linspace(49.855-30,49.855+30,hor_p)
        beta = self.FOV_T.value()
        for j in range(n):
            for i in range(channel_nums):
                for k in range(hor_p):
                    i_INPUT = [0,cosd(field[i]),sind(field[i])]
                    print(i_INPUT)
                    I2 = self.wedge_d_offset(i_INPUT, -1, 1.444)
                    I3 = self.prims3_d_shaping(I2, -46.7284, 1.444)
                    #lens_emit_x = -cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])-cosd(field[i])/2
                    #lens_emit_y = cosd(field[i])/2 - cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])
                    #lens_emit_z = np.sqrt(2)/2*cosd(field[i])*sind(2*theta[j])+cosd(2*theta[j])*sind(field[i])


                    n1 = theta[j]
                    i2 = self.ref_vec_cal(n1, I3)     #振镜出光                  
                    n2 = [-cosd(alpha[k]),sind(alpha[k]),0]   #棱镜法线旋转
                    i3 = self.ref_vec_cal(n2, i2)    #棱镜出光
                    emitting_XYZ_vector = i3
                    emitting_XYZ_unit_vector = emitting_XYZ_vector/np.linalg.norm(emitting_XYZ_vector)
                    emitting_XYZ_unit_vector_all.append(emitting_XYZ_unit_vector)
        emit_phi_list = np.array([np.arctan(x[2])*57.3 for x in emitting_XYZ_unit_vector_all])
        emit_gamma_list = np.array([np.arctan(x[0]/x[1])*57.3 for x in emitting_XYZ_unit_vector_all])
        #print(len(emit_gamma_list))
        if n == 1:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums],pen=None, symbol='o', symbolBrush='b')
            self.show_text()
           # text=pg.TextItem()
            #txt = str(emit_gamma_list[19])+str(emit_phi_list[19])
            #text.setHtml('<font size="4" color="blue">%s</font>'%(txt))
            #text.setPos(0, 0)
            #self.graphicsView.addItem(text)
            #self.graphicsView.addItem()
            #self.graphicsView.
            #self.graphicsView.addItem(a)
             
        if n == 2:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.show_text()
        if n == 3:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.show_text()
        if n == 4:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.show_text()
        if n == 5:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.show_text()
        if n == 6:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.show_text()
        if n == 7:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.show_text()
        if n == 8:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.show_text()
        if n == 9:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.show_text()

        if n == 10:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.show_text()
 
        if n == 11:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.show_text()

        if n == 12:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime') 
            self.show_text()         
        if n == 13:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo') 
            self.show_text()
        if n == 14:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='orange') 
            self.show_text() 
        if n == 15:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*14:hor_p*channel_nums*15], emit_phi_list[hor_p*channel_nums*14:hor_p*channel_nums*15], pen=None, symbol='o', symbolBrush='slategray')
            self.show_text()
        if n == 16:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*14:hor_p*channel_nums*15], emit_phi_list[hor_p*channel_nums*14:hor_p*channel_nums*15], pen=None, symbol='o', symbolBrush='slategray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*15:hor_p*channel_nums*16], emit_phi_list[hor_p*channel_nums*15:hor_p*channel_nums*16], pen=None, symbol='o', symbolBrush='peru') 
        #print(emit_gamma_list,type(emit_gamma_list))
        #self.graphicsView.plotItem.clear()
            self.show_text()

    def huadong_plot_show(self):
        self.graphicsView.scene().sigMouseMoved.connect(self.shizixian)
        print(self.checkBox_angle1.isChecked())
        if self.checkBox_angle1.isChecked() == False:
            pass

        else:
            #print(1)
            self.graphicsView.scene().sigMouseMoved.connect(self.shizixian)
            self.emit_phi_list = 0
            self.emit_gamma_list = 0
            angle = self.Angle1.value()
            channel_nums = self.Channel_nums.value()
            total_field = np.float64(self.ifov.text())
            lens_beam_emit_unit_vector_all = []
            core_K = []
            emitting_XYZ_unit_vector_all = []
            theta = self.g_angle_list()
            #print(theta)
            field = list(self.field)
            #print(field,channel_nums)
            n = int(self.ifov_2.text())
            #print(n)
            hor_p = 21
            alpha = np.linspace(49.855-30,49.855+30,hor_p)
            beta = self.FOV_T.value()
            for j in range(n):
                for i in range(channel_nums):
                    for k in range(hor_p):
                        i_INPUT = [0,cosd(field[i]),sind(field[i])]
                        I2 = self.wedge_d_offset(i_INPUT, -1, 1.444)
                        I3 = self.prims3_d_shaping(I2, -46.7284, 1.444)
                        #lens_emit_x = -cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])-cosd(field[i])/2
                        #lens_emit_y = cosd(field[i])/2 - cosd(field[i])/2*cosd(2*theta[j])+np.sqrt(2)/2*sind(field[i])*sind(2*theta[j])
                        #lens_emit_z = np.sqrt(2)/2*cosd(field[i])*sind(2*theta[j])+cosd(2*theta[j])*sind(field[i])


                        n1 = theta[j]
                        i2 = self.ref_vec_cal(n1, I3)     #振镜出光                  
                        n2 = [-cosd(alpha[k]),sind(alpha[k]),0]   #棱镜法线旋转
                        i3 = self.ref_vec_cal(n2, i2)    #棱镜出光
                        emitting_XYZ_vector = i3
                        emitting_XYZ_unit_vector = emitting_XYZ_vector/np.linalg.norm(emitting_XYZ_vector)
                        emitting_XYZ_unit_vector_all.append(emitting_XYZ_unit_vector)
            emit_phi_list = np.array([np.arctan(x[2])*57.3 for x in emitting_XYZ_unit_vector_all])
            emit_gamma_list = np.array([np.arctan(x[0]/x[1])*57.3 for x in emitting_XYZ_unit_vector_all])
        if n == 1:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.show_text()
        if n == 2:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.show_text()
        if n == 3:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.show_text()
        if n == 4:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.show_text()
        if n == 5:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.show_text()
        if n == 6:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.show_text()
        if n == 7:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.show_text()
        if n == 8:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.show_text()
        if n == 9:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.show_text()


        if n == 10:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.show_text()
        if n == 11:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.show_text()
        if n == 12:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')          
            self.show_text()
        if n == 13:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo') 
            self.show_text()
        if n == 14:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='orange')  
            self.show_text()
        if n == 15:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*14:hor_p*channel_nums*15], emit_phi_list[hor_p*channel_nums*14:hor_p*channel_nums*15], pen=None, symbol='o', symbolBrush='slategray')
            self.show_text()
        if n == 16:
            self.graphicsView.plotItem.clear()
            self.graphicsView.plot(emit_gamma_list[0:hor_p*channel_nums], emit_phi_list[0:hor_p*channel_nums], pen=None, symbol='o', symbolBrush='b')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*1:hor_p*channel_nums*2], emit_phi_list[hor_p*channel_nums*1:hor_p*channel_nums*2], pen=None, symbol='o', symbolBrush='r')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*2:hor_p*channel_nums*3], emit_phi_list[hor_p*channel_nums*2:hor_p*channel_nums*3], pen=None, symbol='o', symbolBrush='g')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*3:hor_p*channel_nums*4], emit_phi_list[hor_p*channel_nums*3:hor_p*channel_nums*4], pen=None, symbol='o', symbolBrush='purple')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*4:hor_p*channel_nums*5], emit_phi_list[hor_p*channel_nums*4:hor_p*channel_nums*5], pen=None, symbol='o', symbolBrush='lightgray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*5:hor_p*channel_nums*6], emit_phi_list[hor_p*channel_nums*5:hor_p*channel_nums*6], pen=None, symbol='o', symbolBrush='yellow')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*6:hor_p*channel_nums*7], emit_phi_list[hor_p*channel_nums*6:hor_p*channel_nums*7], pen=None, symbol='o', symbolBrush='dodgerblue')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*7:hor_p*channel_nums*8], emit_phi_list[hor_p*channel_nums*7:hor_p*channel_nums*8], pen=None, symbol='o', symbolBrush='orange')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*8:hor_p*channel_nums*9], emit_phi_list[hor_p*channel_nums*8:hor_p*channel_nums*9], pen=None, symbol='o', symbolBrush='violet')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*9:hor_p*channel_nums*10], emit_phi_list[hor_p*channel_nums*9:hor_p*channel_nums*10], pen=None, symbol='o', symbolBrush='lawngreen')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*10:hor_p*channel_nums*11], emit_phi_list[hor_p*channel_nums*10:hor_p*channel_nums*11], pen=None, symbol='o', symbolBrush='gold')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*11:hor_p*channel_nums*12], emit_phi_list[hor_p*channel_nums*11:hor_p*channel_nums*12], pen=None, symbol='o', symbolBrush='lime')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*12:hor_p*channel_nums*13], emit_phi_list[hor_p*channel_nums*12:hor_p*channel_nums*13], pen=None, symbol='o', symbolBrush='indigo')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*13:hor_p*channel_nums*14], emit_phi_list[hor_p*channel_nums*13:hor_p*channel_nums*14], pen=None, symbol='o', symbolBrush='lightcoral')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*14:hor_p*channel_nums*15], emit_phi_list[hor_p*channel_nums*14:hor_p*channel_nums*15], pen=None, symbol='o', symbolBrush='slategray')
            self.graphicsView.plot(emit_gamma_list[hor_p*channel_nums*15:hor_p*channel_nums*16], emit_phi_list[hor_p*channel_nums*15:hor_p*channel_nums*16], pen=None, symbol='o', symbolBrush='peru') 
            self.show_text()
        #print(emit_gamma_list,type(emit_gamma_list))

    # def plot_slot(self):
    #     x = np.random.normal(size=10)
    #     y = np.random.normal(size=10)
    #     r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
    #     r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
    #     print(x,type(x))
    #     print(y,type(y))
    #     self.graphicsView.plotItem.clear()
    #     self.graphicsView.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)


    def source_fov_show(self, MainWindow):
        if self.Channel_nums.value() != '' and self.ifov.text() == '':
            self.lineEdit.setText(str([1]*self.Channel_nums.value()))  
    
        if self.Channel_nums.value() != '' and self.ifov.text() != '':

            total_field = np.float64(self.ifov.text())
            field = np.linspace(total_field/2, -total_field/2, self.Channel_nums.value())
            self.field = np.around(field, decimals=2)
            self.lineEdit.setText(str(self.field))      
    def messageBox(self):
        QMessageBox.warning(self,"warn","Please turn on the switch")
        self.statusbar.showMessage("Please turn on the switch!!!!!!!!!!!!!")




    # def mouseMoved(self,evt):
    #     vLine = pg.InfiniteLine(angle=90, movable=False)
    #     hLine = pg.InfiniteLine(angle=0, movable=False)
    #     p1 = self.graphicsView
    #     vb = p1.vb
    #     pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    #     if p1.sceneBoundingRect().contains(pos):
    #         mousePoint = vb.mapSceneToView(pos)
    #         index = int(mousePoint.x())
    #         if index > 0 and index < len(data1):
    #             label.setText(
    #                 "<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>"
    #                 % (mousePoint.x(), data1[index], data2[index]))
    #         vLine.setPos(mousePoint.x())
    #         hLine.setPos(mousePoint.y())


# proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

if __name__ == "__main__":
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()    # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()      # 实例化QMainWindow类
    aw.setupUi(w)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()               # 显示主窗体
    # App.exit()
    sys.exit(App.exec_())   # 循环中等待退出程序
