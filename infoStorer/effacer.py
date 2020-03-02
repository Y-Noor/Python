# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'effacer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 175)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.rodeii)
        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name of website or game"))
        self.pushButton.setText(_translate("Form", "Delete"))


    def rodeii(self):
        import csv

        index = self.lineEdit.text()
        data = []
        with open('db.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        flag = False

        for i in range(0, len(data)):
            if data[i][0] == index:
                flag = True
                data.pop(i)
                with open('db.csv', 'w') as csvfile:
                    for i in range(0,len(data)):
                        for j in range(0,len(data[i])):
                            csvfile.write(data[i][j] + ',')
                        csvfile.write('\n')

                self.show_popUpGud()
                break

        if flag == False:
            self.show_popUpBad()

    def show_popUpBad(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error!')
        msg.setText('You do not have data for this website/game')

        x = msg.exec()

    def show_popUpGud(self):
        msg = QMessageBox()
        msg.setWindowTitle('Success!')
        msg.setText('Item deleted')

        x = msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
