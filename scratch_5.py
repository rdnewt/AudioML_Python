
####### ADD THESE 2 FILES INTO THE PROGRAM BEFORE MAINWINDOW
class Ui_deviceSelectorWindow(object):
    def setupUi(self, deviceSelectorWindow):
        deviceSelectorWindow.setObjectName("deviceSelectorWindow")
        deviceSelectorWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(deviceSelectorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deviceTW = QtWidgets.QTreeWidget(self.centralwidget)
        self.deviceTW.setObjectName("deviceTW")
        self.deviceTW.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.deviceTW)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.deviceSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.deviceSelectButton.setObjectName("deviceSelectButton")
        self.horizontalLayout.addWidget(self.deviceSelectButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.deviceExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.deviceExitButton.setObjectName("deviceExitButton")
        self.horizontalLayout.addWidget(self.deviceExitButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        deviceSelectorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deviceSelectorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        deviceSelectorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(deviceSelectorWindow)
        self.statusbar.setObjectName("statusbar")
        deviceSelectorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(deviceSelectorWindow)
        QtCore.QMetaObject.connectSlotsByName(deviceSelectorWindow)

    def retranslateUi(self, deviceSelectorWindow):
        _translate = QtCore.QCoreApplication.translate
        deviceSelectorWindow.setWindowTitle(_translate("deviceSelectorWindow", "MainWindow"))
        self.deviceSelectButton.setText(_translate("deviceSelectorWindow", "PushButton"))
        self.deviceExitButton.setText(_translate("deviceSelectorWindow", "PushButton"))

class deviceSelectorWindow(QtWidgets.QMainWindow, Ui_deviceSelectorWindow):
    def __init__(self, parent=None):
        super(deviceSelectorWindow, self).__init__(parent)
        self.setupUi(self)
        self.ExitTrue = False
        self.selectedList = []
        self.selectedIndex = 0
        self.deviceSelectButton.clicked.connect(self.selectDevice)
        self.deviceExitButton.clicked.connect(self.exitDeviceSelector)

    def exitDeviceSelector(self):
        self.ExitTrue = True
        self.close()

    def selectDevice(self):
        self.ExitTrue = True
        a = self.deviceTW.currentItem()
        c = [a.text(i) for i in range(a.columnCount())]
        indexNumber = int(c[0])
        self.selectedList = c
        self.selectedIndex = indexNumber
        self.close()

########### ADD THESE AT THE END OF THE __init__ FUNCTION ON class MainWindow
self.selectFeedLive.clicked.connect(self.getDevice)
self.deviceSelectorWindow = deviceSelectorWindow()
self.deviceSelectorWindow.selectedIndex = -1

########## ADD THIS FUNCTION IN THE class MainWindow AFTER THE getFiles(self): FUNC

def getDevice(self):
    p = pyaudio.PyAudio()
    self.fileView.clear()
    self.deviceSelectorWindow.deviceTW.clear()
    headers = list(p.get_device_info_by_index(0).keys())
    self.deviceSelectorWindow.deviceTW.setHeaderLabels(list(p.get_device_info_by_index(0).keys()))
    for x in range(0, p.get_device_count()):
        infoList = [str(i) for i in list(p.get_device_info_by_index(x).values())]
        QtWidgets.QTreeWidgetItem(self.deviceSelectorWindow.deviceTW, infoList)
    self.deviceSelectorWindow.deviceTW.setAlternatingRowColors(True)
    self.deviceSelectorWindow.show()
    while not self.deviceSelectorWindow.ExitTrue:
        QtTest.QTest.qWait(3000)
    for i in range(len(self.deviceSelectorWindow.selectedList)):
        newStr = headers[i] + " : " + self.deviceSelectorWindow.selectedList[i]
        self.fileView.append(newStr)



######### CHANGE THIS IN THE LIVE AUDIO PART OF goFunc: FUNC IN MainWindow
chosen_device_index = self.deviceSelectorWindow.selectedIndex