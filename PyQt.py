# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQUTdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import numpy as np
import scipy.io.wavfile as wav
import math as m
import pyaudio
import struct

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
        self.saveOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setObjectName("saveOutputButton")
        self.horizontalLayout_2.addWidget(self.saveOutputButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
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
        self.saveOutputButton.setText(_translate("MainWindow", "Save Output"))

class Ui_ImageWindow(object):
    def setupUi(self, ImageWindow):
        ImageWindow.setObjectName("ImageWindow")
        ImageWindow.resize(524, 438)
        self.centralwidget = QtWidgets.QWidget(ImageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("labsel")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.waveGraph = pg.PlotWidget()
        # self.waveGraph.setText("")
        # self.waveGraph.setPixmap(QtGui.QPixmap("Q:/ACPATTERNS/Rokakaka_close-up.png"))
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.waveGraph.plot(hour, temperature)
        self.waveGraph.setObjectName("WaveGraph")
        self.horizontalLayout.addWidget(self.waveGraph)
        pg.setConfigOptions(imageAxisOrder='row-major')
        pg.mkQApp()
        self.SpectroGraph = pg.GraphicsLayoutWidget()
        self.horizontalLayout.addWidget(self.SpectroGraph)
        self.widget2 = QtWidgets.QWidget(self.splitter)
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #############################################################################
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.Save_Wave = QtWidgets.QCheckBox(self.widget2)
        # self.Save_Wave.setObjectName("Save_Wave")
        # self.horizontalLayout_2.addWidget(self.Save_Wave)
        # self.Save_Spectro = QtWidgets.QCheckBox(self.widget2)
        # self.Save_Spectro.setObjectName("Save_Spectro")
        # self.horizontalLayout_2.addWidget(self.Save_Spectro)
        # self.verticalLayout.addLayout(self.horizontalLayout_2)
        #############################################################################
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pauseResumeButton = QtWidgets.QPushButton(self.widget2)
        self.pauseResumeButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pauseResumeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.exitButton = QtWidgets.QPushButton(self.widget2)
        self.exitButton.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.exitButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addWidget(self.splitter)
        ImageWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ImageWindow)
        self.statusbar.setObjectName("statusbar")
        ImageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageWindow)

    def retranslateUi(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("ImageWindow", "MainWindow"))
        self.label.setText(_translate("ImageWindow", "Label"))
        # self.Save_Wave.setText(_translate("ImageWindow", "Save Wave Image"))
        # self.Save_Spectro.setText(_translate("ImageWindow", "Save Spectrogram"))
        self.pauseResumeButton.setText(_translate("ImageWindow", "Pause"))
        self.exitButton.setText(_translate("ImageWindow", "Exit"))

class graphWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(graphWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)


class ImageWindow(QtWidgets.QMainWindow, Ui_ImageWindow):

    def __init__(self, parent=None):
        super(ImageWindow, self).__init__(parent)
        self.setupUi(self)
        self.ExitTrue = False
        self.PauseTrue = False
        # self.pauseResumeButton.clicked.connect(self.PauseImageWindow)
        self.exitButton.clicked.connect(self.ExitImageWindow)
        self.spectroData = np.array([[1, 2], [3, 4]])
        self.t = np.array([1,2,3,4])
        self.f = np.array([1,2,3,4])
        self.DisplaySpectrogram(self.t, self.f, self.spectroData)



    def DisplaySpectrogram(self, t, f, spectro):
        self.SpectroGraph.clear()
        self.p1 = self.SpectroGraph.addPlot()
        self.img = pg.ImageItem()
        self.p1.addItem(self.img)
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.img)
        self.SpectroGraph.addItem(self.hist)
        self.hist.setLevels(np.min(spectro), np.max(spectro))
        self.hist.gradient.restoreState(
            {'mode': 'rgb',
             'ticks': [(0.5, (0, 182, 188, 255)),
                       (1.0, (246, 111, 0, 255)),
                       (0.0, (75, 0, 113, 255))]})
        self.img.setImage(spectro)
        self.img.scale(t[-1] / np.size(spectro, axis=1),
                       f[-1] / np.size(spectro, axis=0))
        # Limit panning/zooming to the spectrogram
        self.p1.setLimits(xMin=0, xMax=t[-1], yMin=0, yMax=f[-1])
        # Add labels to the axis
        self.p1.setLabel('bottom', "Time", units='s')
        # If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
        self.p1.setLabel('left', "Frequency", units='Hz')

    def ExitImageWindow(self):
        self.ExitTrue = True
        self.close()

    def PauseImageWindow(self):
        _translate = QtCore.QCoreApplication.translate
        if self.PauseTrue:
            self.PauseTrue = False
            self.pauseResumeButton.setText(_translate("ImageWindow", "Pause"))
            print("true oops")
            print(self.PauseTrue)
        else:
            self.PauseTrue = True
            self.pauseResumeButton.setText(_translate("ImageWindow", "Resume"))
            print("false oops")
            print(self.PauseTrue)

    def SpeedUpProcess(self):
        _translate = QtCore.QCoreApplication.translate
        if self.PauseTrue:
            self.PauseTrue = False
            self.pauseResumeButton.setText(_translate("ImageWindow", "Speed Up"))
            print("true")
            print(self.PauseTrue)
        else:
            self.PauseTrue = True
            self.pauseResumeButton.setText(_translate("ImageWindow", "Slow Down"))
            print("false")
            print(self.PauseTrue)

    def UpdateLabel(self, label="Default"):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ImageWindow", label))






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    names = []
    allWav = True
    name = ""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ImageWindow = ImageWindow()
        self.graphWindow = graphWindow()
        self.setupUi(self)
        self.goButton.clicked.connect(self.goFunc)
        self.openFilesShort.clicked.connect(self.getFiles)
        self.ClassificationList = []
        self.saveOutputButton.clicked.connect(self.saveOutput)

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

    def saveOutput(self):
        self.name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File as...")

        ####################################################################
        #### classification list is under self.ClassificationList       ####
        #### do what you want to save the file under the name self.name ####
        ####################################################################

    def goFunc(self):
        self.ImageWindow.show()
        self.ClassificationList = []



        #####################
        #### SHORT AUDIO ####
        #####################
        #If short audio is checked, do this
        if self.shortAudioRadio.isChecked():

            #Error detector: not a wav file or no files selected
            if self.allWav == False:
                self.labelView.setText("ERROR: Some files are not in .wav format")
                return
            elif self.names == []:
                self.labelView.setText("ERROR: No files selected")
                return

            #Initializing button states for this itteration of short audio. False means the button has not been clicked before
            self.ImageWindow.PauseTrue = False
            self.ImageWindow.ExitTrue = False

            #Renaming the pause button to be "speed up" to skip the 3 second wait after every file is processed
            self.ImageWindow.pauseResumeButton.clicked.disconnect()
            _translate = QtCore.QCoreApplication.translate
            self.ImageWindow.pauseResumeButton.setText(_translate("ImageWindow", "Speed Up"))
            self.ImageWindow.pauseResumeButton.clicked.connect(self.ImageWindow.SpeedUpProcess)

            #Global variables for spectrogram generation
            pts_fft = 1024
            spectro = np.zeros((256, 216))


            # Change fnames out for self.names
            for name in self.names:

                #If exiting the graphing window in any way, this will prevent the code from looping unintentionally
                if self.ImageWindow.ExitTrue or (not self.ImageWindow.isVisible()):
                    print("Exited out of graphing window")
                    return

                #Read short audio file
                fs, dat = wav.read(name)  # read in .wav file

                # this section performs a check to see if the .wav file is stereo (2-channels)
                # and averages the 2 to a single channel if that is the case
                # can be commented out if all the files are now mono format
                if len(np.shape(dat)) == 2:
                    print("")
                    dat = dat.astype(float)
                    dat = (dat[:, 0] + dat[:, 1]) // 2
                    dat = dat.astype('int16')

                #Honestly I don't know. Ask Sam
                dat = np.pad(dat, (0, pts_fft - len(dat) % pts_fft))

                #Making sure every audio file is exactly 5 seconds long
                fiveSeconds = fs * 5
                dat = dat[0:fiveSeconds]

                #Creating a graph for the actual wave
                WavY = dat
                WavX = np.array(range(len(WavY)))
                self.ImageWindow.waveGraph.setYRange(np.min(WavY), np.max(WavY))
                self.ImageWindow.waveGraph.plot(WavX, WavY, clear=True)
                self.ImageWindow.update()

                # generate window
                window = np.hamming(pts_fft)

                # compute spectrograms and load into spectro field
                for i in range(len(dat) // pts_fft):
                    a = np.fft.fft(dat[i:i + pts_fft] * window)
                    b = abs(a[0:pts_fft // 4])
                    b = 20 * np.log10(b)
                    spectro[:, i] = b
                f = np.arange(0, fs / 4, fs / pts_fft)
                t = np.arange(0, (fs * 5 // pts_fft + 1) * pts_fft / (fs), pts_fft / fs)

                #Displaying the spectrogram in the spectrogram graph
                self.ImageWindow.DisplaySpectrogram(t,f,spectro)

                #############################################################
                ###### PUT THE NEURAL NETWORK CLASSIFICATION STUFF HERE #####
                #############################################################

                newLabel = "test" #Put the classification of the audio file here
                self.ClassificationList.append(newLabel)
                self.ImageWindow.UpdateLabel(newLabel)
                self.labelView.append(newLabel)


                #This line ensures that the graph updating above will take place
                QtGui.QGuiApplication.processEvents()

                #Will wait 3 seconds every file unless the speed up (PauseButton) is pressed.
                if not self.ImageWindow.PauseTrue:
                    QtTest.QTest.qWait(3000)
                else:
                    continue

            # while True:
            #     # If Exit button or the image window closes for some reason, exit the loop.
            #     if self.ImageWindow.ExitTrue or (not self.ImageWindow.isVisible()):
            #         print("button clicked")
            #         return
            #
            #     # If Pause button is pressed, skip this iteration of the loop
            #     # and wait 3 seconds to see if resume is pushed
            #     if self.ImageWindow.PauseTrue:
            #         print("operation paused")
            #         QtTest.QTest.qWait(3000)
            #         continue

                #currently for testing
                # SpectroX.append(T)
                # T += 1
                # Y = random.randint(1,20)
                # SpectroY.append(Y)

                # self.ImageWindow.waveGraph.plot(WavX, WavY, clear = True)
                # self.ImageWindow.update()
                # QtGui.QGuiApplication.processEvents()
                # QtTest.QTest.qWait(3000)


        ####################
        #### LONG AUDIO ####
        ####################
        # If long audio is checked, do this
        elif self.longAudioRadio.isChecked():
            # Error detector: not a wav file or no files selected
            if self.allWav == False:
                self.labelView.setText("ERROR: Some files are not in .wav format")
                return
            elif self.names == []:
                self.labelView.setText("ERROR: No files selected")
                return

            # Initializing button states for this itteration of short audio. False means the button has not been clicked before
            self.ImageWindow.PauseTrue = False
            self.ImageWindow.ExitTrue = False

            # Renaming the pause button to be "speed up" to skip the 3 second wait after every file is processed
            self.ImageWindow.pauseResumeButton.clicked.disconnect()
            _translate = QtCore.QCoreApplication.translate
            self.ImageWindow.pauseResumeButton.setText(_translate("ImageWindow", "Speed Up"))
            self.ImageWindow.pauseResumeButton.clicked.connect(self.ImageWindow.SpeedUpProcess)

            # Global variables for spectrogram generation
            pts_fft = 1024
            spectro = np.zeros((256, 216))

            # Change fnames out for self.names
            for name in self.names:

                # If exiting the graphing window in any way, this will prevent the code from looping unintentionally
                if self.ImageWindow.ExitTrue or (not self.ImageWindow.isVisible()):
                    print("Exited out of graphing window")
                    return

                # Read short audio file
                fs, dat = wav.read(name)  # read in .wav file

                # this section performs a check to see if the .wav file is stereo (2-channels)
                # and averages the 2 to a single channel if that is the case
                # can be commented out if all the files are now mono format
                if len(np.shape(dat)) == 2:
                    print("")
                    dat = dat.astype(float)
                    dat = (dat[:, 0] + dat[:, 1]) // 2
                    dat = dat.astype('int16')

                # Honestly I don't know. Ask Sam
                dat = np.pad(dat, (0, pts_fft - len(dat) % pts_fft))

                # Making sure every audio file is exactly 5 seconds long
                testing_length = m.ceil(len(dat)/fs - 4)
                for i in range(testing_length):
                    if self.ImageWindow.ExitTrue or (not self.ImageWindow.isVisible()):
                        print("Exited out of graphing window")
                        return
                    newInit = fs * i
                    newEnd = fs * (i + 5)
                    newDat = dat[newInit:newEnd]
                    if len(newDat) / fs != 5.0:
                        newDat = np.pad(newDat, (0, fs * 5 - len(newDat)), 'constant', constant_values=(0, 0))

                    # Creating a graph for the actual wave
                    WavY = newDat
                    test = range(len(WavY))
                    test = [i/fs for i in test]
                    WavX = np.array(test)
                    self.ImageWindow.waveGraph.setYRange(np.min(WavY), np.max(WavY))
                    self.ImageWindow.waveGraph.plot(WavX, WavY, clear=True)
                    self.ImageWindow.update()

                    # generate window
                    window = np.hamming(pts_fft)
                    # compute spectrograms and load into spectro field
                    for k in range(len(newDat) // pts_fft):
                        a = np.fft.fft(newDat[k:k + pts_fft] * window)
                        b = abs(a[0:pts_fft // 4])
                        b = 20 * np.log10(b)
                        spectro[:, k] = b
                    f = np.arange(0, fs / 4, fs / pts_fft)
                    t = np.arange(0, (fs * 5 // pts_fft + 1) * pts_fft / (fs), pts_fft / fs)

                    # Displaying the spectrogram in the spectrogram graph
                    self.ImageWindow.DisplaySpectrogram(t, f, spectro)

                    #############################################################
                    ###### PUT THE NEURAL NETWORK CLASSIFICATION STUFF HERE #####
                    #############################################################

                    newLabel = "test"  # Put the classification of the audio file here
                    intoFile = name + " at timestamp " + str(i) + " seconds is " + newLabel
                    print(intoFile)
                    self.ClassificationList.append(newLabel)
                    self.ImageWindow.UpdateLabel(newLabel)
                    self.labelView.append(newLabel)

                    # This line ensures that the graph updating above will take place
                    QtGui.QGuiApplication.processEvents()

                    # Will wait 3 seconds every file unless the speed up (PauseButton) is pressed.
                    if not self.ImageWindow.PauseTrue:
                        QtTest.QTest.qWait(3000)
                    else:
                        continue

        ####################
        #### LIVE AUDIO ####
        ####################
        # If short audio is checked, do this
        elif self.liveAudioRadio.isChecked():

            self.ImageWindow.PauseTrue = False
            self.ImageWindow.ExitTrue = False
            # self.ImageWindow.pauseResumeButton.clicked.disconnect()
            self.ImageWindow.pauseResumeButton.clicked.connect(self.ImageWindow.PauseImageWindow)
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 44100

            p = pyaudio.PyAudio()

            chosen_device_index = -1
            for x in range(0, p.get_device_count()):
                info = p.get_device_info_by_index(x)
                # print p.get_device_info_by_index(x)
                if info["name"] == "pulse":
                    chosen_device_index = info["index"]
                    print("Chosen index: ", chosen_device_index)

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input_device_index=chosen_device_index,
                            input=True,
                            output=True,
                            frames_per_buffer=CHUNK
                            )
            BUFFER = np.zeros(RATE * 5, dtype='int')
            WavX = np.array(range(len(BUFFER)))

            pts_fft = 1024
            spectro = np.zeros((256, 216))
            k1 = 0
            firstSpectro = False
            time = 0
            time2 = 0
            while True:
                if self.ImageWindow.ExitTrue or (not self.ImageWindow.isVisible()):
                    print("Exited out of graphing window")
                    return
                if self.ImageWindow.PauseTrue:
                    QtGui.QGuiApplication.processEvents()
                    print("Paused")
                    continue
                chunk = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
                chunky = list(chunk)
                BUFFER = np.roll(BUFFER, -CHUNK)
                BUFFER[RATE * 5 - CHUNK:] = chunky
                self.ImageWindow.waveGraph.setYRange(np.min(BUFFER), np.max(BUFFER))
                self.ImageWindow.waveGraph.plot(WavX, BUFFER, clear=True)
                self.ImageWindow.update()

                # generate window
                window = np.hamming(pts_fft)
                k1 += CHUNK
                # compute spectrograms and load into spectro field
                f = np.arange(0, RATE / 4, RATE / pts_fft)
                t = np.arange(0, (RATE * 5 // pts_fft + 1) * pts_fft / (RATE), pts_fft / RATE)
                if k1 >= RATE*5 and not firstSpectro:
                    firstSpectro = True
                    for i in range(len(BUFFER) // pts_fft):
                        a = np.fft.fft(BUFFER[i:i + pts_fft] * window)
                        b = abs(a[0:pts_fft // 4])
                        b = 20 * np.log10(b)
                        spectro[:, i] = b

                    time = k1 / RATE

                    k1 = 0
                    # Displaying the spectrogram in the spectrogram graph
                    self.ImageWindow.DisplaySpectrogram(t, f, spectro)

                    #############################################################
                    ###### PUT THE NEURAL NETWORK CLASSIFICATION STUFF HERE #####
                    #############################################################

                    newLabel = "car_horn"  # Put the classification of the audio file here
                    intoFile = "Identified " + newLabel + " at 0-" + str(m.floor(time)) + " seconds."
                    self.ClassificationList.append(intoFile)
                    self.ImageWindow.UpdateLabel(newLabel)
                    self.labelView.append(intoFile)


                elif k1 >= RATE and firstSpectro:
                    for i in range(len(BUFFER) // pts_fft):
                        a = np.fft.fft(BUFFER[i:i + pts_fft] * window)
                        b = abs(a[0:pts_fft // 4])
                        b = 20 * np.log10(b)
                        spectro[:, i] = b

                    time = time + 1
                    time2 = time2 + 1
                    k1 = k1 - RATE

                    # Displaying the spectrogram in the spectrogram graph
                    self.ImageWindow.DisplaySpectrogram(t, f, spectro)

                    #############################################################
                    ###### PUT THE NEURAL NETWORK CLASSIFICATION STUFF HERE #####
                    #############################################################

                    newLabel = "car_horn"  # Put the classification of the audio file here
                    intoFile = "Identified " + newLabel + " at " + str(time2) + "-" + str(m.floor(time)) + " seconds."
                    self.ClassificationList.append(intoFile)
                    self.ImageWindow.UpdateLabel(newLabel)
                    self.labelView.append(intoFile)





                QtGui.QGuiApplication.processEvents()

            # DO LIVE AUDIO FUNC
            print("live is pressed")


    # def newSpectroImage(self, path="Q:/Guns/not_this.jpg"):
    #     spectroPiximap = QtGui.QPixmap(path)
    #     spectroPiximap = spectroPiximap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
    #     self.ImageWindow.Spectro_Image.setPixmap(spectroPiximap)
    #
    # def newWaveImage(self, path="Q:/Guns/not_this.jpg"):
    #     wavePiximap = QtGui.QPixmap(path)
    #     wavePiximap = wavePiximap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
    #     self.ImageWindow.wavePhoto.setPixmap(wavePiximap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())