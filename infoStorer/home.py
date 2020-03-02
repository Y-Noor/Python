# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from credentials import Ui_Form
from retrieval import Ui_Form1
from effacer import Ui_Form2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 171, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.addNew = QtWidgets.QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(80, 90, 201, 41))
        self.addNew.setObjectName("addNew")
        self.retrieve = QtWidgets.QPushButton(self.centralwidget)
        self.retrieve.setGeometry(QtCore.QRect(80, 140, 91, 31))
        self.retrieve.setObjectName("retrieve")
        self.deletion = QtWidgets.QPushButton(self.centralwidget)
        self.deletion.setGeometry(QtCore.QRect(190, 140, 91, 31))
        self.deletion.setObjectName("deletion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.addNew.clicked.connect(self.add_new)
        self.retrieve.clicked.connect(self.look_up)
        self.deletion.clicked.connect(self.retirey)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_new(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def look_up(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def retirey(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "What do you wish to do?"))
        self.addNew.setText(_translate("MainWindow", "Add New"))
        self.retrieve.setText(_translate("MainWindow", "Search specific"))
        self.deletion.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
