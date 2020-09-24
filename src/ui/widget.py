# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.vlayout = QtWidgets.QVBoxLayout(Form)
        self.vlayout.setObjectName("vlayout")
        self.global_vlayout = QtWidgets.QVBoxLayout()
        self.global_vlayout.setObjectName("global_vlayout")
        self.trace_name = QtWidgets.QLabel(Form)
        self.trace_name.setMaximumSize(QtCore.QSize(16777215, 60))
        self.trace_name.setObjectName("trace_name")
        self.global_vlayout.addWidget(self.trace_name)
        self.debate_title = QtWidgets.QLabel(Form)
        self.debate_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.debate_title.setObjectName("debate_title")
        self.global_vlayout.addWidget(self.debate_title)
        self.turn_name = QtWidgets.QLabel(Form)
        self.turn_name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.turn_name.setObjectName("turn_name")
        self.global_vlayout.addWidget(self.turn_name)
        self.hlayout = QtWidgets.QHBoxLayout()
        self.hlayout.setObjectName("hlayout")
        self.pros_vlayout = QtWidgets.QVBoxLayout()
        self.pros_vlayout.setObjectName("pros_vlayout")
        self.pros_debate = QtWidgets.QLabel(Form)
        self.pros_debate.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pros_debate.setObjectName("pros_debate")
        self.pros_vlayout.addWidget(self.pros_debate)
        self.pros_name = QtWidgets.QLabel(Form)
        self.pros_name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pros_name.setObjectName("pros_name")
        self.pros_vlayout.addWidget(self.pros_name)
        self.pros_hlayout = QtWidgets.QHBoxLayout()
        self.pros_hlayout.setObjectName("pros_hlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.pros_hlayout.addItem(spacerItem)
        self.pros_vlayout.addLayout(self.pros_hlayout)
        self.hlayout.addLayout(self.pros_vlayout)
        self.mid_vlayout = QtWidgets.QVBoxLayout()
        self.mid_vlayout.setObjectName("mid_vlayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mid_vlayout.addLayout(self.horizontalLayout)
        self.hlayout.addLayout(self.mid_vlayout)
        self.cons_vlayout = QtWidgets.QVBoxLayout()
        self.cons_vlayout.setObjectName("cons_vlayout")
        self.cons_debate = QtWidgets.QLabel(Form)
        self.cons_debate.setMaximumSize(QtCore.QSize(16777215, 40))
        self.cons_debate.setObjectName("cons_debate")
        self.cons_vlayout.addWidget(self.cons_debate)
        self.cons_name = QtWidgets.QLabel(Form)
        self.cons_name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.cons_name.setObjectName("cons_name")
        self.cons_vlayout.addWidget(self.cons_name)
        self.cons_hlayout = QtWidgets.QHBoxLayout()
        self.cons_hlayout.setObjectName("cons_hlayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.cons_hlayout.addItem(spacerItem1)
        self.cons_vlayout.addLayout(self.cons_hlayout)
        self.hlayout.addLayout(self.cons_vlayout)
        self.global_vlayout.addLayout(self.hlayout)
        self.vlayout.addLayout(self.global_vlayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.trace_name.setText(_translate("Form", "TextLabel"))
        self.debate_title.setText(_translate("Form", "TextLabel"))
        self.turn_name.setText(_translate("Form", "TextLabel"))
        self.pros_debate.setText(_translate("Form", "TextLabel"))
        self.pros_name.setText(_translate("Form", "TextLabel"))
        self.cons_debate.setText(_translate("Form", "TextLabel"))
        self.cons_name.setText(_translate("Form", "TextLabel"))
