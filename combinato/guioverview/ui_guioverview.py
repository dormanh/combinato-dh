# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guioverview.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLabel.sizePolicy().hasHeightForWidth())
        self.labelLabel.setSizePolicy(sizePolicy)
        self.labelLabel.setObjectName("labelLabel")
        self.horizontalLayout.addWidget(self.labelLabel)
        self.lineEditLabel = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEditLabel.sizePolicy().hasHeightForWidth()
        )
        self.lineEditLabel.setSizePolicy(sizePolicy)
        self.lineEditLabel.setObjectName("lineEditLabel")
        self.horizontalLayout.addWidget(self.lineEditLabel)
        self.checkBoxInitH5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxInitH5.setObjectName("checkBoxInitH5")
        self.horizontalLayout.addWidget(self.checkBoxInitH5)
        self.checkBoxSetStates = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxSetStates.setChecked(True)
        self.checkBoxSetStates.setObjectName("checkBoxSetStates")
        self.horizontalLayout.addWidget(self.checkBoxSetStates)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tableViewChannels = QtWidgets.QTableView(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableViewChannels.sizePolicy().hasHeightForWidth()
        )
        self.tableViewChannels.setSizePolicy(sizePolicy)
        self.tableViewChannels.setFrameShape(QtWidgets.QFrame.Box)
        self.tableViewChannels.setAlternatingRowColors(True)
        self.tableViewChannels.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.tableViewChannels.setSortingEnabled(True)
        self.tableViewChannels.setObjectName("tableViewChannels")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxLeftImage = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxLeftImage.setObjectName("comboBoxLeftImage")
        self.verticalLayout.addWidget(self.comboBoxLeftImage)
        self.scrollAreaImage = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollAreaImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollAreaImage.setWidgetResizable(False)
        self.scrollAreaImage.setObjectName("scrollAreaImage")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 57, 599))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaImage.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaImage)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBoxRightImage = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBoxRightImage.setObjectName("comboBoxRightImage")
        self.verticalLayout_2.addWidget(self.comboBoxRightImage)
        self.scrollAreaImageRight = QtWidgets.QScrollArea(self.layoutWidget1)
        self.scrollAreaImageRight.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaImageRight.setWidgetResizable(False)
        self.scrollAreaImageRight.setObjectName("scrollAreaImageRight")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 186, 499))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaImageRight.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollAreaImageRight)
        self.verticalLayout_3.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Initialize_from_current_folder = QtWidgets.QAction(MainWindow)
        self.action_Initialize_from_current_folder.setObjectName(
            "action_Initialize_from_current_folder"
        )
        self.actionToggleExtract = QtWidgets.QAction(MainWindow)
        self.actionToggleExtract.setObjectName("actionToggleExtract")
        self.actionToggleSort = QtWidgets.QAction(MainWindow)
        self.actionToggleSort.setObjectName("actionToggleSort")
        self.action_Next_channel = QtWidgets.QAction(MainWindow)
        self.action_Next_channel.setObjectName("action_Next_channel")
        self.action_Previous_channel = QtWidgets.QAction(MainWindow)
        self.action_Previous_channel.setObjectName("action_Previous_channel")
        self.actionSave_actions_to_file = QtWidgets.QAction(MainWindow)
        self.actionSave_actions_to_file.setObjectName("actionSave_actions_to_file")
        self.actionOne_Down = QtWidgets.QAction(MainWindow)
        self.actionOne_Down.setObjectName("actionOne_Down")
        self.actionToggle_sort_negative = QtWidgets.QAction(MainWindow)
        self.actionToggle_sort_negative.setObjectName("actionToggle_sort_negative")
        self.actionToggle_sorted_positive = QtWidgets.QAction(MainWindow)
        self.actionToggle_sorted_positive.setObjectName("actionToggle_sorted_positive")
        self.actionToggle_sorted_negative = QtWidgets.QAction(MainWindow)
        self.actionToggle_sorted_negative.setObjectName("actionToggle_sorted_negative")
        self.menuActions.addAction(self.action_Initialize_from_current_folder)
        self.menuActions.addAction(self.actionToggleExtract)
        self.menuActions.addAction(self.actionToggleSort)
        self.menuActions.addAction(self.actionToggle_sort_negative)
        self.menuActions.addAction(self.action_Next_channel)
        self.menuActions.addAction(self.action_Previous_channel)
        self.menuActions.addAction(self.actionSave_actions_to_file)
        self.menuActions.addAction(self.actionToggle_sorted_positive)
        self.menuActions.addAction(self.actionToggle_sorted_negative)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelLabel.setText(_translate("MainWindow", "Label for sorted sessions:"))
        self.checkBoxInitH5.setText(
            _translate("MainWindow", "Initialize from h5-files")
        )
        self.checkBoxSetStates.setText(
            _translate("MainWindow", "Set states upon initialization")
        )
        self.menuActions.setTitle(_translate("MainWindow", "&Actions"))
        self.action_Initialize_from_current_folder.setText(
            _translate("MainWindow", "&Initialize from current folder")
        )
        self.action_Initialize_from_current_folder.setShortcut(
            _translate("MainWindow", "Ctrl+I")
        )
        self.actionToggleExtract.setText(_translate("MainWindow", "Toggle &extract"))
        self.actionToggleExtract.setShortcut(_translate("MainWindow", "E"))
        self.actionToggleSort.setText(_translate("MainWindow", "Toggle sort &positive"))
        self.actionToggleSort.setShortcut(_translate("MainWindow", "S"))
        self.action_Next_channel.setText(_translate("MainWindow", "&Next channel"))
        self.action_Next_channel.setShortcut(_translate("MainWindow", "Space"))
        self.action_Previous_channel.setText(
            _translate("MainWindow", "&Previous channel")
        )
        self.action_Previous_channel.setShortcut(_translate("MainWindow", "Shift+Up"))
        self.actionSave_actions_to_file.setText(
            _translate("MainWindow", "Save &actions to file")
        )
        self.actionOne_Down.setText(_translate("MainWindow", "One Down"))
        self.actionOne_Down.setShortcut(_translate("MainWindow", "Shift+Down"))
        self.actionToggle_sort_negative.setText(
            _translate("MainWindow", "Toggle sort &negative")
        )
        self.actionToggle_sort_negative.setShortcut(_translate("MainWindow", "Shift+S"))
        self.actionToggle_sorted_positive.setText(
            _translate("MainWindow", "Toggle sorted positive")
        )
        self.actionToggle_sorted_positive.setShortcut(_translate("MainWindow", "M"))
        self.actionToggle_sorted_negative.setText(
            _translate("MainWindow", "Toggle sorted negative")
        )
        self.actionToggle_sorted_negative.setShortcut(
            _translate("MainWindow", "Shift+M")
        )
