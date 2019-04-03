# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newuserpage.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
import sqlite3
from PyQt5 import QtWidgets


class Ui_Newuser(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Newuser):
        Newuser.setObjectName("Newuser")
        Newuser.resize(682, 449)
        self.gridLayoutWidget = QtWidgets.QWidget(Newuser)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 90, 611, 207))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_firstname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_firstname.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                       "color: \"white\";")
        self.l_firstname.setObjectName("l_firstname")
        self.gridLayout.addWidget(self.l_firstname, 1, 1, 1, 1)
        self.txt_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_username.setObjectName("txt_username")
        self.gridLayout.addWidget(self.txt_username, 7, 1, 1, 1)
        self.l_phone = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_phone.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                   "color: \"white\";")
        self.l_phone.setObjectName("l_phone")
        self.gridLayout.addWidget(self.l_phone, 4, 1, 1, 1)
        self.l_lastname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_lastname.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                      "color: \"white\";")
        self.l_lastname.setObjectName("l_lastname")
        self.gridLayout.addWidget(self.l_lastname, 1, 3, 1, 1)
        self.txt_phone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_phone.setObjectName("txt_phone")
        self.gridLayout.addWidget(self.txt_phone, 5, 1, 1, 1)
        self.l_email = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_email.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                   "color: \"white\";")
        self.l_email.setObjectName("l_email")
        self.gridLayout.addWidget(self.l_email, 4, 3, 1, 1)
        self.txt_lastename = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_lastename.setObjectName("txt_lastename")
        self.gridLayout.addWidget(self.txt_lastename, 2, 3, 1, 1)
        self.txt_firstname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_firstname.setObjectName("txt_firstname")
        self.gridLayout.addWidget(self.txt_firstname, 2, 1, 1, 1)
        self.l_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_password.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                      "color: \"white\";")
        self.l_password.setObjectName("l_password")
        self.gridLayout.addWidget(self.l_password, 6, 3, 1, 1)
        self.txt_emailid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_emailid.setObjectName("txt_emailid")
        self.gridLayout.addWidget(self.txt_emailid, 5, 3, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 7, 3, 1, 1)
        self.l_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_username.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                      "color: \"white\";")
        self.l_username.setObjectName("l_username")
        self.gridLayout.addWidget(self.l_username, 6, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Newuser)
        self.textBrowser.setGeometry(QtCore.QRect(120, 20, 401, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget = QtWidgets.QWidget(Newuser)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 310, 331, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_submit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_submit.setStyleSheet("background-color: rgb(62, 0, 255);\n"
                                      "color: \"white\";")
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setStyleSheet("background-color: rgb(62, 0, 255);\n"
                                    "color: \"white\";")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.l_status = QtWidgets.QLabel(Newuser)
        self.l_status.setGeometry(QtCore.QRect(240, 390, 181, 31))
        self.l_status.setText("")
        self.l_status.setObjectName("l_status")

        self.retranslateUi(Newuser)
        QtCore.QMetaObject.connectSlotsByName(Newuser)

        self.btn_exit.clicked.connect(self.btn_exit_handler)
        self.btn_submit.clicked.connect(self.database)


    def btn_exit_handler(self):
        self.openwindow()

    def pop_message(self,text):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def database(self):
        try:
            txt_firstname_v=self.txt_firstname.text()
            txt_lastname_v = self.txt_lastename.text()
            txt_phone_v = self.txt_phone.text()
            txt_emailid_v=self.txt_emailid.text()
            txt_username_v=self.txt_username.text()
            txt_password_v=self.txt_password.text()

            conn=sqlite3.connect('user.db')
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS credentials 
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fname TEXT, 
                lname TEXT, 
                Phone TEXT, 
                email TEXT,
                username TEXT, 
                password TEXT)""")


            cursor.execute(""" INSERT INTO credentials 
                (fname,
                lname,
                Phone,
                email,
                username, 
                password)
                
            VALUES 
            (?,?,?,?,?,?)
            """,(txt_firstname_v, txt_lastname_v, txt_phone_v, txt_emailid_v,txt_username_v,txt_password_v))


            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Added to  Database ")
        except:
            self.pop_message("Cannot add  to  Database ")



    def retranslateUi(self, Newuser):
        _translate = QtCore.QCoreApplication.translate
        Newuser.setWindowTitle(_translate("Newuser", "Form"))
        self.l_firstname.setText(_translate("Newuser", "First Name"))
        self.l_phone.setText(_translate("Newuser", "Phone Number"))
        self.l_lastname.setText(_translate("Newuser", "Last Name"))
        self.l_email.setText(_translate("Newuser", "Email ID"))
        self.l_password.setText(_translate("Newuser", "Password"))
        self.l_username.setText(_translate("Newuser", "username"))
        self.textBrowser.setHtml(_translate("Newuser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">New User </span></p></body></html>"))
        self.btn_submit.setText(_translate("Newuser", "Submit"))
        self.btn_exit.setText(_translate("Newuser", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Newuser = QtWidgets.QWidget()

    ui = Ui_Newuser()
    ui.setupUi(Newuser)
    Newuser.show()
    sys.exit(app.exec_())
