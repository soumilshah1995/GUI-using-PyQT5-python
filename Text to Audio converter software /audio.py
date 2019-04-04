# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Audio.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5 import QtWidgets
import threading



class Ui_Audio(object):
    def setupUi(self, Audio):
        Audio.setObjectName("Audio")
        Audio.resize(592, 434)
        self.textBrowser = QtWidgets.QTextBrowser(Audio)
        self.textBrowser.setGeometry(QtCore.QRect(60, 10, 451, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutWidget = QtWidgets.QWidget(Audio)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 270, 461, 57))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_name_file = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_name_file.setObjectName("txt_name_file")
        self.gridLayout.addWidget(self.txt_name_file, 2, 0, 1, 1)
        self.btn_download = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_download.setStyleSheet("background-color: rgb(16, 16, 16);\n"
                                        "color: \"white\";\n"
                                        "font: 14pt \".SF NS Text\";")

        self.btn_download.clicked.connect(self.text_mp3)

        self.btn_download.setObjectName("btn_download")
        self.gridLayout.addWidget(self.btn_download, 3, 0, 1, 1)
        self.txt_write = QtWidgets.QTextEdit(Audio)
        self.txt_write.setGeometry(QtCore.QRect(60, 100, 451, 151))
        self.txt_write.setObjectName("txt_write")

        self.retranslateUi(Audio)
        QtCore.QMetaObject.connectSlotsByName(Audio)

    def retranslateUi(self, Audio):
        _translate = QtCore.QCoreApplication.translate
        Audio.setWindowTitle(_translate("Audio", "Form"))
        self.textBrowser.setHtml(_translate("Audio", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Welcome to Text to Audio Converter Software</span></p>\n"
                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))
        self.txt_name_file.setText(_translate("Audio", "Name of File"))
        self.btn_download.setText(_translate("Audio", "Download File"))
        self.txt_write.setHtml(_translate("Audio", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type your text here</p></body></html>"))


    def pop_message(self,text):

        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def text_mp3(self):

        threading.Thread().start()

        txt_name_file_v = self.txt_name_file.text()
        txt_write_v = self.txt_write.toPlainText()

        self.my_server(txt_name_file_v,txt_write_v)

    def my_server(self,txt_name_file_v,txt_write_v):


        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }

        url = 'https://text-to-speech-demo.ng.bluemix.net/api/v1/synthesize?t'

        params= {
            'text': 'hello everyone i am going to teach you python',
            'voice': 'en-US_AllisonV2Voice',
            'download': True,
            'accept': 'audio/mp3'
        }

        params['text'] = txt_write_v

        response = requests.get(url, headers=headers,params=params)

        with open('{}.mp3'.format(txt_name_file_v),'wb') as f:
            f.write(response.content)

        self.pop_message("Download Complete ")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Audio = QtWidgets.QWidget()
    ui = Ui_Audio()
    ui.setupUi(Audio)
    Audio.show()
    sys.exit(app.exec_())
