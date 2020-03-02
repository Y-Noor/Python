# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credentials.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(261, 308)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(10, 40, 69, 16))
        self.label1.setObjectName("label1")
        self.Username = QtWidgets.QLineEdit(Form)
        self.Username.setGeometry(QtCore.QRect(10, 110, 241, 20))
        self.Username.setObjectName("Username")
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(101, 250, 75, 23))
        self.submit.setObjectName("submit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 90, 48, 16))
        self.label.setObjectName("label")
        self.pw = QtWidgets.QLineEdit(Form)
        self.pw.setGeometry(QtCore.QRect(10, 210, 241, 20))
        self.pw.setObjectName("pw")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 46, 16))
        self.label_3.setObjectName("label_3")
        self.websiteOrGame = QtWidgets.QLineEdit(Form)
        self.websiteOrGame.setGeometry(QtCore.QRect(10, 60, 241, 20))
        self.websiteOrGame.setObjectName("websiteOrGame")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(10, 160, 241, 20))
        self.email.setObjectName("email")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.submit.clicked.connect(self.login)
        self.submit.clicked.connect(Form.close)


    def login(self):
        entry =[]
        loc = self.websiteOrGame.text() + ','
        entry.append(loc)
        username = self.Username.text() + ','
        entry.append(username)
        email = self.email.text() + ','
        entry.append(email)
        pw = self.pw.text()
        entry.append(pw)

        file = open('db.csv', 'a')
        for i in range(0, len(entry)):
            file.write(entry[i])
        file.write('\n')

        self.show_popUp()

    def show_popUp(self):
        msg = QMessageBox()
        msg.setWindowTitle('Success')
        msg.setText('Credentials successfully stored!')

        x = msg.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "Website/game"))
        self.submit.setText(_translate("Form", "Submit"))
        self.label_2.setText(_translate("Form", "email address used"))
        self.label.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
