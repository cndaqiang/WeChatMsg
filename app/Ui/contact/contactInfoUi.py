# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactInfoUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 748)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_remark = QtWidgets.QLabel(self.frame)
        self.label_remark.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_remark.setFont(font)
        self.label_remark.setText("")
        self.label_remark.setObjectName("label_remark")
        self.horizontalLayout_3.addWidget(self.label_remark)
        self.btn_analysis = QtWidgets.QPushButton(self.frame)
        self.btn_analysis.setObjectName("btn_analysis")
        self.horizontalLayout_3.addWidget(self.btn_analysis)
        self.btn_emotion = QtWidgets.QPushButton(self.frame)
        self.btn_emotion.setObjectName("btn_emotion")
        self.horizontalLayout_3.addWidget(self.btn_emotion)
        self.btn_report = QtWidgets.QPushButton(self.frame)
        self.btn_report.setObjectName("btn_report")
        self.horizontalLayout_3.addWidget(self.btn_report)
        self.toolButton_output = QtWidgets.QToolButton(self.frame)
        self.toolButton_output.setObjectName("toolButton_output")
        self.horizontalLayout_3.addWidget(self.toolButton_output)
        self.btn_back = QtWidgets.QPushButton(self.frame)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_analysis.setText(_translate("Form", "统计信息"))
        self.btn_emotion.setText(_translate("Form", "情感分析"))
        self.btn_report.setText(_translate("Form", "生成年度报告"))
        self.toolButton_output.setText(_translate("Form", "导出聊天记录"))
        self.btn_back.setText(_translate("Form", "退出"))
