# Form implementation generated from reading ui file 'm:\DOCS\_prog\_mirror_rename\renamemirrors.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 748)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 610, 321, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layouthb1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layouthb1.setContentsMargins(0, 0, 0, 0)
        self.layouthb1.setObjectName("layouthb1")
        self.dev1 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.dev1.setObjectName("dev1")
        self.layouthb1.addWidget(self.dev1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 781, 591))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layouth1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layouth1.setContentsMargins(0, 0, 0, 0)
        self.layouth1.setObjectName("layouth1")
        self.layoutv1 = QtWidgets.QVBoxLayout()
        self.layoutv1.setObjectName("layoutv1")
        self.path1 = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.path1.setText("")
        self.path1.setObjectName("path1")
        self.layoutv1.addWidget(self.path1)
        self.list1 = QtWidgets.QListWidget(parent=self.horizontalLayoutWidget_2)
        self.list1.setObjectName("list1")
        self.layoutv1.addWidget(self.list1)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.layoutv1.addWidget(self.pushButton)
        self.layouth1.addLayout(self.layoutv1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dev1.setText(_translate("MainWindow", "Clone explorer"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
