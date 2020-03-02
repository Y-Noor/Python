# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retrieval.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(273, 210)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 9, 122, 16))
        self.label.setObjectName("label")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(150, 30, 75, 23))
        self.btn.setObjectName("btn")
        self.inpt = QtWidgets.QLineEdit(Form)
        self.inpt.setGeometry(QtCore.QRect(9, 30, 133, 20))
        self.inpt.setObjectName("inpt")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(9, 84, 78, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(9, 124, 95, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(9, 163, 50, 16))
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(96, 80, 141, 21))
        self.username.setText("")
        self.username.setObjectName("username")
        self.email = QtWidgets.QLabel(Form)
        self.email.setGeometry(QtCore.QRect(110, 120, 161, 21))
        self.email.setText("")
        self.email.setObjectName("email")
        self.pw = QtWidgets.QLabel(Form)
        self.pw.setGeometry(QtCore.QRect(70, 160, 141, 21))
        self.pw.setText("")
        self.pw.setObjectName("pw")

        self.btn.clicked.connect(self.rodeii)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def rodeii(self):
        import csv

        index = self.inpt.text()
        data = []
        with open('db.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        flag = False

        for i in range(0, len(data)):
            if data[i][0] == index:
                found = data[i]
                self.username.setText(found[1])
                self.email.setText(found[2])
                self.pw.setText(found[3])
                flag = True
                break

        if flag == False:
            self.show_popUp()


    def show_popUp(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error!')
        msg.setText('You do not have data for this website/game')

        x = msg.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name of website or game"))
        self.btn.setText(_translate("Form", "Retrieve"))
        self.label_2.setText(_translate("Form", "Username used:"))
        self.label_3.setText(_translate("Form", "email address used:"))
        self.label_4.setText(_translate("Form", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
