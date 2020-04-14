# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQUTdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.shortAudioRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.shortAudioRadio.setObjectName("shortAudioRadio")
        self.verticalLayout.addWidget(self.shortAudioRadio)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.longAudioRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.longAudioRadio.setObjectName("longAudioRadio")
        self.verticalLayout.addWidget(self.longAudioRadio)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.liveAudioRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.liveAudioRadio.setObjectName("liveAudioRadio")
        self.verticalLayout.addWidget(self.liveAudioRadio)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fileView = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileView.setObjectName("fileView")
        self.verticalLayout_2.addWidget(self.fileView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.selectFeedLive = QtWidgets.QPushButton(self.centralwidget)
        self.selectFeedLive.setObjectName("selectFeedLive")
        self.horizontalLayout.addWidget(self.selectFeedLive)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.openFilesShort = QtWidgets.QPushButton(self.centralwidget)
        self.openFilesShort.setObjectName("openFilesShort")
        self.horizontalLayout.addWidget(self.openFilesShort)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelView = QtWidgets.QTextBrowser(self.centralwidget)
        self.labelView.setObjectName("labelView")
        self.verticalLayout_3.addWidget(self.labelView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setObjectName("goButton")
        self.horizontalLayout_2.addWidget(self.goButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 30))
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
        self.shortAudioRadio.setText(_translate("MainWindow", "Short Audio Samples"))
        self.longAudioRadio.setText(_translate("MainWindow", "Long Audio Samples"))
        self.liveAudioRadio.setText(_translate("MainWindow", "Live Audio Feed"))
        self.selectFeedLive.setText(_translate("MainWindow", "Select Feed"))
        self.openFilesShort.setText(_translate("MainWindow", "Open Files"))
        self.goButton.setText(_translate("MainWindow", "Go"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    names = []
    allWav = True

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.goButton.clicked.connect(self.goFunc)
        self.openFilesShort.clicked.connect(self.getFiles)

    def getFiles(self):
        self.allWav = True
        self.fileView.clear()
        # self.
        self.names, _ = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File')
        for i in self.names:
            path, ext = os.path.splitext(i)
            # print(path)
            # print(ext)
            if ext != '.wav':
                i = '<span style=\" color: #ff0000;\">%s</span>' % i
                self.allWav = False
            self.fileView.append(i)
    
    
    # Here is where you'll put the functions for the short, long, and live audio inputs.
    # When selecting files, the path to the file is stored in the list names and can be called/itterated through like so:
    # for i in length(self.names):
    #   print(self.names[i])               < this will print the file path
    def goFunc(self):
        print("stuff")
        if self.shortAudioRadio.isChecked():
            if self.allWav == False:
                self.labelView.setText("ERROR: Some files are not in .wav format")
                return
            # DO SHORT AUDIO FUNC
            print("short is pressed")
        elif self.longAudioRadio.isChecked():
            if self.allWav == False:
                self.labelView.setText("ERROR: Some files are not in .wav format")
                return
            # DO LONG AUDIO FUNC
            print("long is pressed")
        elif self.liveAudioRadio.isChecked():
            # DO LIVE AUDIO FUNC
            print("live is pressed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
