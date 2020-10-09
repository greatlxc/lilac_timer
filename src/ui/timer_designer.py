# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 24))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.trace_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.trace_name_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.trace_name_edit.setObjectName("trace_name_edit")
        self.horizontalLayout_4.addWidget(self.trace_name_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 24))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.debate_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.debate_edit.setObjectName("debate_edit")
        self.horizontalLayout_5.addWidget(self.debate_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.pros_debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pros_debate_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pros_debate_edit.setObjectName("pros_debate_edit")
        self.horizontalLayout_9.addWidget(self.pros_debate_edit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.pros_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pros_name_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pros_name_edit.setObjectName("pros_name_edit")
        self.horizontalLayout_11.addWidget(self.pros_name_edit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setMaximumSize(QtCore.QSize(100, 250))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.pros_players_list = QtWidgets.QListWidget(self.centralwidget)
        self.pros_players_list.setMaximumSize(QtCore.QSize(16777215, 250))
        self.pros_players_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pros_players_list.setObjectName("pros_players_list")
        self.horizontalLayout_13.addWidget(self.pros_players_list)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_7.addWidget(self.line_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.cons_debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cons_debate_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cons_debate_edit.setObjectName("cons_debate_edit")
        self.horizontalLayout_10.addWidget(self.cons_debate_edit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.cons_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cons_name_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cons_name_edit.setObjectName("cons_name_edit")
        self.horizontalLayout_12.addWidget(self.cons_name_edit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setMaximumSize(QtCore.QSize(100, 250))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.cons_players_list = QtWidgets.QListWidget(self.centralwidget)
        self.cons_players_list.setMaximumSize(QtCore.QSize(16777215, 250))
        self.cons_players_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.cons_players_list.setObjectName("cons_players_list")
        self.horizontalLayout_14.addWidget(self.cons_players_list)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.number_label = QtWidgets.QLabel(self.centralwidget)
        self.number_label.setMinimumSize(QtCore.QSize(120, 0))
        self.number_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.number_label.setObjectName("number_label")
        self.horizontalLayout_17.addWidget(self.number_label)
        self.number_slider = QtWidgets.QSlider(self.centralwidget)
        self.number_slider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.number_slider.setMinimum(1)
        self.number_slider.setMaximum(10)
        self.number_slider.setProperty("value", 4)
        self.number_slider.setOrientation(QtCore.Qt.Horizontal)
        self.number_slider.setObjectName("number_slider")
        self.horizontalLayout_17.addWidget(self.number_slider)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.timetable_vlayout = QtWidgets.QVBoxLayout()
        self.timetable_vlayout.setObjectName("timetable_vlayout")
        self.verticalLayout_2.addLayout(self.timetable_vlayout)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setMinimumSize(QtCore.QSize(235, 0))
        self.add_button.setMaximumSize(QtCore.QSize(235, 16777215))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_16.addWidget(self.add_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setMinimumSize(QtCore.QSize(235, 0))
        self.delete_button.setMaximumSize(QtCore.QSize(235, 16777215))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_16.addWidget(self.delete_button)
        self.input_button = QtWidgets.QPushButton(self.centralwidget)
        self.input_button.setMaximumSize(QtCore.QSize(235, 16777215))
        self.input_button.setObjectName("input_button")
        self.horizontalLayout_16.addWidget(self.input_button)
        self.output_button = QtWidgets.QPushButton(self.centralwidget)
        self.output_button.setMaximumSize(QtCore.QSize(235, 16777215))
        self.output_button.setObjectName("output_button")
        self.horizontalLayout_16.addWidget(self.output_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(250, 250))
        self.logo.setMaximumSize(QtCore.QSize(250, 250))
        self.logo.setObjectName("logo")
        self.verticalLayout_4.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.right_stop_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.right_stop_checkBox.setChecked(True)
        self.right_stop_checkBox.setObjectName("right_stop_checkBox")
        self.verticalLayout_4.addWidget(self.right_stop_checkBox)
        self.wheel_adjust_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.wheel_adjust_checkBox.setChecked(True)
        self.wheel_adjust_checkBox.setObjectName("wheel_adjust_checkBox")
        self.verticalLayout_4.addWidget(self.wheel_adjust_checkBox)
        self.use_keyboard_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.use_keyboard_checkBox.setChecked(True)
        self.use_keyboard_checkBox.setObjectName("use_keyboard_checkBox")
        self.verticalLayout_4.addWidget(self.use_keyboard_checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.restart_logo = QtWidgets.QLabel(self.centralwidget)
        self.restart_logo.setMinimumSize(QtCore.QSize(0, 40))
        self.restart_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.restart_logo.setObjectName("restart_logo")
        self.horizontalLayout.addWidget(self.restart_logo)
        self.restart_key = QtWidgets.QPushButton(self.centralwidget)
        self.restart_key.setObjectName("restart_key")
        self.horizontalLayout.addWidget(self.restart_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.last_logo = QtWidgets.QLabel(self.centralwidget)
        self.last_logo.setMinimumSize(QtCore.QSize(0, 40))
        self.last_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.last_logo.setObjectName("last_logo")
        self.horizontalLayout_8.addWidget(self.last_logo)
        self.last_key = QtWidgets.QPushButton(self.centralwidget)
        self.last_key.setObjectName("last_key")
        self.horizontalLayout_8.addWidget(self.last_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.stop_start_logo = QtWidgets.QLabel(self.centralwidget)
        self.stop_start_logo.setMinimumSize(QtCore.QSize(0, 40))
        self.stop_start_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.stop_start_logo.setObjectName("stop_start_logo")
        self.horizontalLayout_15.addWidget(self.stop_start_logo)
        self.stop_start_key = QtWidgets.QPushButton(self.centralwidget)
        self.stop_start_key.setObjectName("stop_start_key")
        self.horizontalLayout_15.addWidget(self.stop_start_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.next_logo = QtWidgets.QLabel(self.centralwidget)
        self.next_logo.setMinimumSize(QtCore.QSize(0, 40))
        self.next_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.next_logo.setObjectName("next_logo")
        self.horizontalLayout_18.addWidget(self.next_logo)
        self.next_key = QtWidgets.QPushButton(self.centralwidget)
        self.next_key.setObjectName("next_key")
        self.horizontalLayout_18.addWidget(self.next_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.exit_logo = QtWidgets.QLabel(self.centralwidget)
        self.exit_logo.setMinimumSize(QtCore.QSize(0, 40))
        self.exit_logo.setMaximumSize(QtCore.QSize(40, 40))
        self.exit_logo.setObjectName("exit_logo")
        self.horizontalLayout_19.addWidget(self.exit_logo)
        self.exit_key = QtWidgets.QPushButton(self.centralwidget)
        self.exit_key.setObjectName("exit_key")
        self.horizontalLayout_19.addWidget(self.exit_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setMinimumSize(QtCore.QSize(250, 0))
        self.start_button.setObjectName("start_button")
        self.verticalLayout_4.addWidget(self.start_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "比赛名称："))
        self.label_3.setText(_translate("MainWindow", "辩题："))
        self.label_4.setText(_translate("MainWindow", "正方："))
        self.label_6.setText(_translate("MainWindow", "正方队名:"))
        self.label_8.setText(_translate("MainWindow", "正方队员："))
        self.label_5.setText(_translate("MainWindow", "反方："))
        self.label_7.setText(_translate("MainWindow", "反方队名："))
        self.label_9.setText(_translate("MainWindow", "反方队员："))
        self.number_label.setText(_translate("MainWindow", "每队人数：4"))
        self.add_button.setText(_translate("MainWindow", "添加"))
        self.delete_button.setText(_translate("MainWindow", "删除"))
        self.input_button.setText(_translate("MainWindow", "导入"))
        self.output_button.setText(_translate("MainWindow", "导出"))
        self.logo.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "设置"))
        self.right_stop_checkBox.setText(_translate("MainWindow", "右键暂停"))
        self.wheel_adjust_checkBox.setText(_translate("MainWindow", "滚轮调节时间"))
        self.use_keyboard_checkBox.setText(_translate("MainWindow", "使用键盘快捷键"))
        self.restart_logo.setText(_translate("MainWindow", "TextLabel"))
        self.restart_key.setText(_translate("MainWindow", "PushButton"))
        self.last_logo.setText(_translate("MainWindow", "TextLabel"))
        self.last_key.setText(_translate("MainWindow", "PushButton"))
        self.stop_start_logo.setText(_translate("MainWindow", "TextLabel"))
        self.stop_start_key.setText(_translate("MainWindow", "PushButton"))
        self.next_logo.setText(_translate("MainWindow", "TextLabel"))
        self.next_key.setText(_translate("MainWindow", "PushButton"))
        self.exit_logo.setText(_translate("MainWindow", "TextLabel"))
        self.exit_key.setText(_translate("MainWindow", "PushButton"))
        self.start_button.setText(_translate("MainWindow", "开始计时"))