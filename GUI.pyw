# Bandar Abullah 1855415
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegularExpression, QTimer
from PyQt5.QtGui import QRegularExpressionValidator, QIcon, QCursor
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


def give_color_to_status(index, result):
    # the student is accepted and won the competition among other students
    if index < 15 and result > 0.0:
        return QtGui.QBrush(QtCore.Qt.green)
    # the student has passed the requirements but failed in the competition of 16 or more students
    elif index >= 15 and result > 0.0:
        return QtGui.QBrush(QtCore.Qt.yellow)
    # not acceptable student for any reason
    return QtGui.QBrush(QtCore.Qt.red)


class Ui_MainWindow(object):
    def __init__(self):
        self.sorting_female = dict()
        self.sorting_male = dict()
        self.semester = []
        self.edu_info = dict()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("img/logo.jpg"))
        MainWindow.setFixedSize(1322, 873)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cancel_b = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_b.setGeometry(QtCore.QRect(1100, 190, 211, 41))
        self.cancel_b.setStyleSheet("QPushButton {\n"
                                    "    background-color:#ff8c8e;\n"
                                    "    border-radius:7px;\n"
                                    "    border:1px solid #ff8c8e;\n"
                                    "    display:inline-block;\n"
                                    "    cursor:hand;\n"
                                    "    color:#ffffff;\n"
                                    "    font-family:Arial;\n"
                                    "    font-size:17px;\n"
                                    "    padding:10px 20px;\n"
                                    "    text-decoration:none;\n"
                                    "    text-shadow:0px 1px 0px #2f6627;\n"
                                    "}\n"
                                    "QPushButton:hover {   \n"
                                    "background-color:#cc0000;\n"
                                    "}\n"
                                    "QPushButton:active {   \n"
                                    "    position:relative;\n"
                                    "    top:1px;\n"
                                    "}\n"
                                    "QPushButton:pressed{background-color: white; color:black;}")
        self.cancel_b.setObjectName("cancel_b")
        self.submit_b = QtWidgets.QPushButton(self.centralwidget)
        self.submit_b.setGeometry(QtCore.QRect(570, 760, 201, 51))
        self.submit_b.setStyleSheet("QPushButton {\n"
                                    "    background-color:#44c767;\n"
                                    "    border-radius:7px;\n"
                                    "    border:1px solid #18ab29;\n"
                                    "    display:inline-block;\n"
                                    "    cursor:pointer;\n"
                                    "    color:#ffffff;\n"
                                    "    font-family:Arial;\n"
                                    "    font-size:17px;\n"
                                    "    padding:16px 31px;\n"
                                    "    text-decoration:none;\n"
                                    "    text-shadow:0px 1px 0px #2f6627;\n"
                                    "}\n"
                                    "QPushButton:hover {   \n"
                                    "background-color:#5cbf2a;\n"
                                    "}\n"
                                    "QPushButton:active {   \n"
                                    "    position:relative;\n"
                                    "    top:3px;\n"
                                    "}\n"
                                    "QPushButton:pressed{background-color: white; color:black;}")
        self.cancel_b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_b.setObjectName("submit_b")
        self.submit_b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.name_le.setGeometry(QtCore.QRect(10, 140, 361, 31))
        self.name_le.setStyleSheet("\n"
                                   "QLineEdit{ background-color:rgb(202, 255, 227);\n"
                                   "border: 2px solid gray;\n"
                                   "border-radius: 7px;\n"
                                   "padding: 0 8px;\n"
                                   "selection-background-color: darkgray;\n"
                                   "font-size: 16px;}\n"
                                   "QLineEdit:focus {  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                   "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);}")
        self.name_le.setObjectName("name_le")
        self.id_le = QtWidgets.QLineEdit(self.centralwidget)
        self.id_le.setGeometry(QtCore.QRect(380, 140, 351, 31))
        self.id_le.setStyleSheet("\n"
                                 "QLineEdit{ background-color:rgb(202, 255, 227);\n"
                                 "border: 2px solid gray;\n"
                                 "border-radius: 7px;\n"
                                 "padding: 0 8px;\n"
                                 "selection-background-color: darkgray;\n"
                                 "font-size: 16px;}\n"
                                 "QLineEdit:focus {  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                 "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);}")
        self.id_le.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.id_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.id_le.setObjectName("id_le")
        self.gpa_le = QtWidgets.QLineEdit(self.centralwidget)
        self.gpa_le.setGeometry(QtCore.QRect(740, 140, 161, 31))
        self.gpa_le.setStyleSheet("\n"
                                  "QLineEdit{ background-color:rgb(202, 255, 227);\n"
                                  "border: 2px solid gray;\n"
                                  "border-radius: 7px;\n"
                                  "padding: 0 8px;\n"
                                  "selection-background-color: darkgray;\n"
                                  "font-size: 16px;}\n"
                                  "QLineEdit:focus {  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                  "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                  "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);}")
        self.gpa_le.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.gpa_le.setObjectName("gpa_le")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, -20, 871, 151))
        self.label_2.setObjectName("label_2")
        self.subject_list = QtWidgets.QComboBox(self.centralwidget)
        self.subject_list.setGeometry(QtCore.QRect(10, 200, 361, 31))
        self.subject_list.setStyleSheet("QComboBox {\n"
                                        "background-color:rgb(202, 255, 227);\n"
                                        "border: 2px solid gray;\n"
                                        "border-radius: 7px;\n"
                                        "    padding: 1px 18px 1px 3px;\n"
                                        "    min-width: 6em;\n"
                                        "color: gray;font-size: 16px;}\n"
                                        "\n"
                                        "QComboBox:editable {\n"
                                        "    background: white;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                        "  \n"
                                        "}\n"
                                        "\n"
                                        "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                        "QComboBox:!editable:on {\n"
                                        "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                        "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                        "color: black;}\n"
                                        "\n"
                                        "QComboBox:on { /* shift the text when the popup opens */\n"
                                        "    padding-top: 3px;\n"
                                        "    padding-left: 4px;\n"
                                        "color: black;}\n"
                                        "\n"
                                        "QComboBox::drop-down {\n"
                                        "    subcontrol-origin: padding;\n"
                                        "    subcontrol-position: top right;\n"
                                        "    width: 15px;\n"
                                        "color: black;\n"
                                        "    border-left-width: 1px;\n"
                                        "    border-left-color: darkgray;\n"
                                        "    border-left-style: solid; /* just a single line */\n"
                                        "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                        "    border-bottom-right-radius: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                        "    top: 1px;\n"
                                        "    left: 1px;\n"
                                        "color: black;}\n")
        self.subject_list.setObjectName("subject_list")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.subject_list.addItem("")
        self.grade_le = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_le.setGeometry(QtCore.QRect(380, 200, 351, 31))
        self.grade_le.setStyleSheet("\n"
                                    "QLineEdit{ background-color:rgb(202, 255, 227);\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 7px;\n"
                                    "padding: 0 8px;\n"
                                    "selection-background-color: darkgray;\n"
                                    "font-size: 16px;}\n"
                                    "QLineEdit:focus {  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                    "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);}")
        self.grade_le.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.grade_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.grade_le.setObjectName("grade_le")
        self.semester_list = QtWidgets.QComboBox(self.centralwidget)
        self.semester_list.setGeometry(QtCore.QRect(740, 200, 341, 31))
        self.semester_list.setStyleSheet("QComboBox {\n"
                                         "background-color:rgb(202, 255, 227);\n"
                                         "border: 2px solid gray;\n"
                                         "border-radius: 7px;\n"
                                         "    padding: 1px 18px 1px 3px;\n"
                                         "    min-width: 6em;\n"
                                         "color:gray;font-size: 16px;}\n"
                                         "\n"
                                         "QComboBox:editable {\n"
                                         "    background: white;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                         "  background-color:rgb(202, 255, 227);\n"
                                         "}\n"
                                         "\n"
                                         "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                         "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                         "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                         "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox:on { /* shift the text when the popup opens */\n"
                                         "    padding-top: 3px;\n"
                                         "    padding-left: 4px;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::drop-down {\n"
                                         "    subcontrol-origin: padding;\n"
                                         "    subcontrol-position: top right;\n"
                                         "    width: 15px;\n"
                                         "\n"
                                         "    border-left-width: 1px;\n"
                                         "    border-left-color: darkgray;\n"
                                         "    border-left-style: solid; /* just a single line */\n"
                                         "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                         "    border-bottom-right-radius: 3px;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::down-arrow {\n"
                                         "    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                         "    top: 1px;\n"
                                         "    left: 1px;\n"
                                         "}")
        self.semester_list.setObjectName("semester_list")
        self.semester_list.addItem("")
        self.semester_list.addItem("")
        self.semester_list.addItem("")
        self.add_b = QtWidgets.QPushButton(self.centralwidget)
        self.add_b.setGeometry(QtCore.QRect(1100, 140, 211, 41))
        self.add_b.setStyleSheet("QPushButton {\n"
                                 "    background-color:#44c767;\n"
                                 "    border-radius:7px;\n"
                                 "    background-radius:7px;"
                                 "    border:1px solid #18ab29;\n"
                                 "    display:inline-block;\n"
                                 "    cursor:pointer;\n"
                                 "    color:#ffffff;\n"
                                 "    font-family:Arial;\n"
                                 "    font-size:17px;\n"
                                 "    padding:10px 20px;\n"
                                 "    text-decoration:none;\n"
                                 "    text-shadow:0px 1px 0px #2f6627;\n"
                                 "}\n"
                                 "QPushButton:hover {   \n"
                                 "background-color:green;"
                                 "\n"
                                 "}\n"
                                 "QPushButton:active {   \n"
                                 "    position:relative;\n"
                                 "    top:1px;\n"
                                 "}\n"
                                 "QPushButton:pressed{background-color: white; color:black;}")
        self.add_b.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.add_b.setObjectName("add_b")
        self.error_d = QtWidgets.QLabel(self.centralwidget)
        self.error_d.setGeometry(QtCore.QRect(10, 176, 1071, 20))
        self.error_d.setStyleSheet("color :red;")
        self.error_d.setText("")
        self.error_d.setObjectName("error_d")
        self.error_up = QtWidgets.QLabel(self.centralwidget)
        self.error_up.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.error_up.setStyleSheet("color :red;")
        self.error_up.setText("")
        self.error_up.setObjectName("error_up")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 250, 1301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(910, 140, 171, 31))
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "background-color:rgb(202, 255, 227);\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 7px;\n"
                                    "    padding: 1px 18px 1px 3px;\n"
                                    "    min-width: 6em;\n"
                                    "color:gray;font-size: 16px;}\n"
                                    "\n"
                                    "QComboBox:editable {\n"
                                    "    background: white;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                    "  background-color:rgb(202, 255, 227);\n"
                                    "}\n"
                                    "\n"
                                    "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                    "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                    "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:on { /* shift the text when the popup opens */\n"
                                    "    padding-top: 3px;\n"
                                    "    padding-left: 4px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    subcontrol-origin: padding;\n"
                                    "    subcontrol-position: top right;\n"
                                    "    width: 15px;\n"
                                    "\n"
                                    "    border-left-width: 1px;\n"
                                    "    border-left-color: darkgray;\n"
                                    "    border-left-style: solid; /* just a single line */\n"
                                    "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                    "    border-bottom-right-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                    "    top: 1px;\n"
                                    "    left: 1px;\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(680, 350, 631, 361))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.male_l = QtWidgets.QLabel(self.centralwidget)
        self.male_l.setGeometry(QtCore.QRect(170, 280, 231, 51))
        self.male_l.setStyleSheet("\n"
                                  "background-color:rgb(202, 255, 227);\n"
                                  "border: 2px solid gray;\n"
                                  "border-radius: 7px;\n"
                                  "padding: 0 8px;\n"
                                  "selection-background-color: darkgray;\n"
                                  "font: 75 22pt \"Times New Roman\";\n"
                                  "")
        self.male_l.setObjectName("male_l")
        self.female_l = QtWidgets.QLabel(self.centralwidget)
        self.female_l.setGeometry(QtCore.QRect(880, 280, 231, 51))
        self.female_l.setStyleSheet("\n"
                                    "background-color:rgb(202, 255, 227);\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 7px;\n"
                                    "padding: 0 8px;\n"
                                    "selection-background-color: darkgray;\n"
                                    "font: 75 22pt \"Times New Roman\";\n"
                                    "")
        self.female_l.setObjectName("female_l")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 350, 631, 361))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionclean_all_and_restart = QtWidgets.QAction(MainWindow)
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_guidline = QtWidgets.QAction(MainWindow)
        self.action_theApp = QtWidgets.QAction(MainWindow)
        self.actionclean_all_and_restart.setShortcutVisibleInContextMenu(True)
        self.action_guidline.setShortcutVisibleInContextMenu(True)
        self.action_quit.setShortcutVisibleInContextMenu(True)
        self.actionclean_all_and_restart.setObjectName(
            "actionclean_all_and_restart")
        self.menuFile.addAction(self.actionclean_all_and_restart)
        self.menuFile.addAction(self.action_quit)
        self.menuAbout.addAction(self.action_guidline)
        self.menuAbout.addAction(self.action_theApp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "FCIT Transferring Students"))
        self.cancel_b.setText(_translate("MainWindow", "Clear"))
        self.submit_b.setText(_translate("MainWindow", "Submit"))
        self.name_le.setPlaceholderText(_translate("MainWindow", "Name"))
        self.id_le.setPlaceholderText(_translate("MainWindow", "ID"))
        self.gpa_le.setPlaceholderText(_translate("MainWindow", "GPA"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><img src=img/FCIT.jpg></p></body></html>"))
        self.subject_list.setItemText(0, _translate("MainWindow", "Subject"))
        self.subject_list.setItemText(1, _translate("MainWindow", "CPIT 110"))
        self.subject_list.setItemText(2, _translate("MainWindow", "CPIT 201"))
        self.subject_list.setItemText(3, _translate("MainWindow", "CPIT 221"))
        self.subject_list.setItemText(4, _translate("MainWindow", "CPCS 202"))
        self.subject_list.setItemText(5, _translate("MainWindow", "CPCS 203"))
        self.subject_list.setItemText(6, _translate("MainWindow", "ELI 104"))
        self.subject_list.setItemText(7, _translate("MainWindow", "MATH 110"))
        self.grade_le.setPlaceholderText(_translate("MainWindow", "Grade"))
        self.semester_list.setItemText(0, _translate("MainWindow", "Semester"))
        self.add_b.setText(_translate("MainWindow", "Add"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gender"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Female"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "GPA"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Weighted ratio"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.male_l.setText(_translate("MainWindow",
                                       "<html><head/><body><p  ><span style=\" font-size:12pt;\"> <img src=img/male.png> </span></p></body></html>"))

        self.female_l.setText(_translate("MainWindow",
                                         "<html><head/><body><p ><span style=\" font-size:12pt;\"><img src=img/female.png></span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "GPA"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Weighted ratio"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Information"))
        self.tableWidget.setStyleSheet("font:Times New Roman;")
        self.tableWidget_2.setStyleSheet("font:Times New Roman;")
        self.actionclean_all_and_restart.setText(
            _translate("MainWindow", "Clear all and restart"))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.actionclean_all_and_restart.setShortcut(
            _translate("MainWindow", "Shift+F5"))
        self.action_guidline.setText(
            _translate("MainWindow", "Guidelines     "))
        self.action_guidline.setShortcut(_translate("MainWindow", "F2"))
        self.action_theApp.setText(_translate("MainWindow", "About"))
        self.action_quit.setShortcut(_translate("MainWindow", "Alt+F4"))

        self.add_b.clicked.connect(self.student_info)
        self.cancel_b.clicked.connect(self.clear)
        # allow only string in name field
        self.name_le.setValidator(QRegularExpressionValidator(
            QRegularExpression("[a-zA-Z][a-zA-Z ]+")))
        # allow only decimal number from 0 to 5
        self.gpa_le.setValidator(QRegularExpressionValidator(
            QRegularExpression("^(5|([0-4]?(\.[0-9]?[0-9])?))$")))
        # allow only numbers from 0 to 100
        self.grade_le.setValidator(QRegularExpressionValidator(
            QRegularExpression("^[0-9]$|^[1-9][0-9]$|^(100)$")))
        self.submit_b.clicked.connect(self.submit)
        self.submit_b.setEnabled(False)
        self.subject_list.setEnabled(False)
        self.semester_list.setEnabled(False)
        self.grade_le.setEnabled(False)
        self.tableWidget.setColumnWidth(2, 108)
        self.tableWidget_2.setColumnWidth(2, 108)
        # delete the placeholder in combobox which does not have a place holder by default
        self.subject_list.view().pressed.connect(
            lambda: self.placeholder(self.subject_list, "Subject"))
        self.comboBox.view().pressed.connect(
            lambda: self.placeholder(self.comboBox, "Gender"))
        self.semester_list.view().pressed.connect(
            lambda: self.placeholder(self.semester_list, "Semester"))
        # id can holds numeric values only
        self.id_le.setValidator(QtGui.QIntValidator())
        self.id_le.editingFinished.connect(self.add_semesters_based_on_id)
        self.gpa_le.editingFinished.connect(lambda: self.show_message(
            "GPA below 3.75 is not accepted !\n\nDo you have a permission from college council ?", "Confirmation",
            "q") if float(self.gpa_le.text()) < 3.75 else None)
        self.menuFile.setStyleSheet(
            "QMenu::item:selected {background-color: rgb(52,73,94);}")
        self.menuAbout.setStyleSheet(
            "QMenu::item:selected {background-color: rgb(52,73,94);}")
        self.action_quit.triggered.connect(lambda: sys.exit(0))
        self.action_guidline.triggered.connect(lambda: self.show_message("1.Enter your name in the first field.\n"
                                                                         "2.Enter your ID correctly (Semesters are generated automatically based on this year and your ID , make sure you enter your ID correctly )\n"
                                                                         "3.Semesters ,subjects and grades cannot be entered or modified before completing name ,id and GPA\n"
                                                                         "4.Submit button cannot be clicked before adding subjects .\n"
                                                                         "5.Once you click Submit you can add another student immediately.\n"
                                                                         "6.Any subject you add will be automaticly removed from the list in order to prevent duplicated subjects\n"
                                                                         "7.Duplicated ID is not acceptable\n"
                                                                         "8.You can add as many students as you want there is no limit.\n"
                                                                         "9.Clear button will just erase the fields not the tables. \n"
                                                                         "10.To clean tables and fields go to File -> clean and restart, or simply use the shortcut | shift+F5  |\n\n\n"
                                                                         "RESULT explanation:\n"
                                                                         "1.Student who satisfy all the requirement and win the competition among other students will appear in GREEN \'Status section\'\n"
                                                                         "2.Student who satisfy all the requirement but fail in the competition will appear in YELLOW \'Status section\'\n"
                                                                         "3.Student who did not satisfy all the requirement will appear in RED ‘Status section\n"
                                                                         "4.Student with GPA lower than 3.75 but have permeation from college council will appear in YELLOW \'GPA section\'\n\n\n"
                                                                         "Thanks For Using FCIT Transferring Students System\n "
                                                                         "", "Guidelines", "About"))
        self.action_theApp.triggered.connect(lambda: self.show_message('=' * 10 + ' FCIT Transferring Students System ' + '=' * 10+"\n\nThis System was created by "
                                                                       "Bandar Abdullah \n"
                                                                       "Student ID:1855415\n"
                                                                       "Academic major:CS\n"
                                                                       "E-mail:OfficialAlrooqi@gmail.com\n"
                                                                       "Phone:+966566498426", "About", "About"))
        self.actionclean_all_and_restart.triggered.connect(lambda: self.show_message(
            "Are you sure you want to restart the program ?\nThis will erase all the data!", "Warning", ""))

    def show_message(self, text, title, q):
        if q == "q":
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("img/logo.jpg"))
            reply = QMessageBox.question(msgBox, title,
                                         text,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                self.clear()
                MainWindow.setFocus()
        elif q == "id":
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("img/logo.jpg"))
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(text)
            msgBox.setWindowTitle(title)
            msgBox.setStandardButtons(QMessageBox.Ok)
            self.id_le.clear()
            msgBox.exec()
        elif q == 'About':
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("img/logo.jpg"))
            msgBox.setText(text)
            msgBox.setWindowTitle(title)
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("img/logo.jpg"))
            reply = QMessageBox.question(msgBox, title,
                                         text,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.clear()
                self.tableWidget.setRowCount(0)
                self.tableWidget_2.setRowCount(0)
                self.sorting_female.clear()
                self.sorting_male.clear()
                MainWindow.setFocus()

    def placeholder(self, combo, text):
        r = ("QComboBox {\n"
             "background-color:rgb(202, 255, 227);\n"
             "border: 2px solid gray;\n"
             "border-radius: 10px;\n"
             "    padding: 1px 18px 1px 3px;\n"
             "    min-width: 6em;\n"
             "color: gray;font-size: 16px;}\n"
             "\n"
             "QComboBox:editable {\n"
             "    background: white;\n"
             "}\n"
             "\n"
             "QComboBox:!editable, QComboBox::drop-down:editable {\n"
             "  \n"
             "}\n"
             "QComboBox:on { /* shift the text when the popup opens */\n"
             "    padding-top: 3px;\n"
             "    padding-left: 4px;\n"
             "color: black;}\n"
             "\n"
             "QComboBox::drop-down {\n"
             "    subcontrol-origin: padding;\n"
             "    subcontrol-position: top right;\n"
             "    width: 15px;\n"
             "color: black;\n"
             "    border-left-width: 1px;\n"
             "    border-left-color: darkgray;\n"
             "    border-left-style: solid; /* just a single line */\n"
             "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
             "    border-bottom-right-radius: 3px;\n"
             "}\n"
             "\n"
             "\n"
             "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
             "    top: 1px;\n"
             "    left: 1px;\n"
             "color: black;}\n")
        if text == "r" and combo == self.subject_list:
            combo.setStyleSheet(r)
        elif text == "r" and combo == self.semester_list:
            combo.clear()
            combo.addItem("Semester")
            combo.setStyleSheet(r)
        elif text == "r" and combo == self.comboBox:
            combo.clear()
            combo.addItems(["Gender", "Male", "Female"])
            combo.setCurrentIndex(0)
            combo.setStyleSheet(r)
        elif combo.itemText(0) == text:
            print(combo.itemText(0))
            combo.removeItem(0)
            combo.setStyleSheet("QComboBox {\n"
                                "background-color:rgb(202, 255, 227);\n"
                                "border: 2px solid gray;\n"
                                "border-radius: 7px;\n"
                                "    padding: 1px 18px 1px 3px;\n"
                                "    min-width: 6em;\n"
                                "color: black;font-size: 16px;}\n"
                                "\n"
                                "QComboBox:editable {\n"
                                "    background: white;\n"
                                "}\n"
                                "\n"
                                "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                "  \n"
                                "}\n"
                                "QComboBox:on { /* shift the text when the popup opens */\n"
                                "    padding-top: 3px;\n"
                                "    padding-left: 4px;\n"
                                "color: black;}\n"
                                "\n"
                                "QComboBox::drop-down {\n"
                                "    subcontrol-origin: padding;\n"
                                "    subcontrol-position: top right;\n"
                                "    width: 15px;\n"
                                "color: black;\n"
                                "    border-left-width: 1px;\n"
                                "    border-left-color: darkgray;\n"
                                "    border-left-style: solid; /* just a single line */\n"
                                "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                "    border-bottom-right-radius: 3px;\n"
                                "}\n"
                                "\n"
                                "\n"
                                "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                "    top: 1px;\n"
                                "    left: 1px;\n"
                                "color: black;}\n")

    @property
    def accepted(self):
        first_condition = False
        second_condition = False
        third_condition = False
        sort = sorted(self.edu_info.items(),
                      key=lambda x: (x[1])[1], reverse=True)
        for i in sort:
            if i[0] == "CPIT 110" and int((i[1])[0]) >= 80:
                first_condition = True
            elif (i[0] == "CPCS 202" and int((i[1])[0]) >= 75) or (i[0] == "CPCS 203" and int((i[1])[0]) >= 75):
                first_condition = True
                second_condition = True
            elif i[0] == "MATH 110" and int((i[1])[0]) >= 85:
                second_condition = True
            elif (i[0] == "ELI 104" and int((i[1])[0]) >= 85) or (i[0] == "CPIT 201" and int((i[1])[0]) >= 80) or (
                    i[0] == "CPIT 221" and int((i[1])[0]) >= 80):
                third_condition = True

        return first_condition and second_condition and third_condition

    def ratio(self):
        if not self.accepted:
            return 0.0
        try:
            sum_grades = 0.0
            sum_units = 0
            # used to calculate both (MATH and CPIT 100 or CPCS 202 or CPCS 203) and (ELI 104 or CPIT 201 or CPIT 221)
            check_twice = 0
            # sorting subjects based on what the student studied last in order to calculate his/her ratio
            sort_rational = sorted(self.edu_info.items(),
                                   key=lambda x: (x[1])[1], reverse=True)

            for i in sort_rational:
                if i == "":
                    continue
                if check_twice == 1:
                    break
                if i[0] == "MATH 110" and int((i[1])[0]) >= 85:
                    for j in sort_rational:
                        if j == "":
                            continue
                        if j[0] == "CPIT 110" and int((j[1])[0]) >= 80:
                            sum_grades += int((i[1])[0]) * \
                                3 + int((j[1])[0]) * 3
                            sum_units += 6
                            sort_rational[sort_rational.index(i)] = ""
                            check_twice += 1

                elif i[0] == "CPIT 110" and int((i[1])[0]) >= 80:
                    for j in sort_rational:
                        if j == "":
                            continue
                        if j[0] == "MATH 110" and int((j[1])[0]) >= 85:
                            sum_grades += int((i[1])[0]) * \
                                3 + int((j[1])[0]) * 3
                            sum_units += 6
                            sort_rational[sort_rational.index(i)] = ""
                            check_twice += 1
                elif i[0] == "CPCS 202" and int((i[1])[0]) >= 75:
                    sum_grades += int((i[1])[0]) * 3
                    sum_units += 3
                    sort_rational[sort_rational.index(i)] = ""
                    check_twice += 1
                elif i[0] == "CPCS 203" and int((i[1])[0]) >= 75:
                    sum_grades += int((i[1])[0]) * 3
                    sum_units += 3
                    sort_rational[sort_rational.index(i)] = ""
                    check_twice += 1

            for j in sort_rational:
                if j == "":
                    continue
                if check_twice == 2:
                    break
                if j[0] == "ELI 104" and int((j[1])[0]) >= 85:
                    sum_grades += int((j[1])[0]) * 2
                    sum_units += 2
                    check_twice += 1
                elif j[0] == "CPIT 221" and int((j[1])[0]) >= 80:
                    sum_grades += int((j[1])[0]) * 3
                    sum_units += 3
                    check_twice += 1
                elif j[0] == "CPIT 201" and int((j[1])[0]) >= 80:
                    sum_grades += int((j[1])[0]) * 3
                    sum_units += 3
                    check_twice += 1
            return sum_grades / sum_units if check_twice == 2 else 0.0
        except Exception as k:
            print(k)
            self.clear()

    def submit(self):
        try:
            if self.submit_b.isEnabled():
                self.submit_b.setEnabled(False)
            if self.comboBox.currentText() == "Male":
                self.tableWidget.setRowCount(0)
                self.sorting_male[str(self.id_le.text())] = (
                    self.name_le.text(), self.gpa_le.text(), self.ratio())
                done = sorted(self.sorting_male.items(),
                              key=lambda x: (x[1])[2], reverse=True)
                for i in done:
                    _translate = QtCore.QCoreApplication.translate
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, 0, QTableWidgetItem((i[1])[0]))
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, 1, QTableWidgetItem((i[0])))
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, 2, QTableWidgetItem((i[1])[1]))
                    # student with GPA below than 3.75 will have yellow background on their GPA
                    if float((i[1])[1]) < 3.75:
                        self.tableWidget.item(self.tableWidget.rowCount() - 1, 2).setBackground(
                            give_color_to_status(16, 1))
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QTableWidgetItem
                                             ("{:.2f}".format((i[1])[2]) if (i[1])[2] > 0.0 else str("-")))
                    self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4,
                                             QTableWidgetItem("Accepted" if (i[1])[2] > 0.0 and done.index(i) < 15
                                                              else "Not Accepted"))
                    self.tableWidget.item(self.tableWidget.rowCount() - 1, 4).setBackground(
                        give_color_to_status(done.index(i), (i[1])[2]))
            else:
                self.tableWidget_2.setRowCount(0)
                self.sorting_female[str(self.id_le.text())] = (
                    self.name_le.text(), self.gpa_le.text(), self.ratio())
                done_female = sorted(self.sorting_female.items(
                ), key=lambda x: (x[1])[2], reverse=True)
                for i in done_female:
                    _translate = QtCore.QCoreApplication.translate
                    self.tableWidget_2.setRowCount(
                        self.tableWidget_2.rowCount() + 1)
                    self.tableWidget_2.setItem(
                        self.tableWidget_2.rowCount() - 1, 0, QTableWidgetItem((i[1])[0]))
                    self.tableWidget_2.setItem(
                        self.tableWidget_2.rowCount() - 1, 1, QTableWidgetItem((i[0])))
                    self.tableWidget_2.setItem(
                        self.tableWidget_2.rowCount() - 1, 2, QTableWidgetItem((i[1])[1]))
                    # student with GPA below than 3.75 will have yellow background on their GPA
                    if float((i[1])[1]) < 3.75:
                        self.tableWidget_2.item(self.tableWidget.rowCount() - 1, 2).setBackground(
                            give_color_to_status(16, 1))
                    self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 3, QTableWidgetItem
                                               ("{:.2f}".format((i[1])[2]) if (i[1])[2] > 0.0 else str("-")))
                    self.tableWidget_2.setItem(self.tableWidget_2.rowCount() - 1, 4,
                                               QTableWidgetItem(
                                                   "Accepted" if (i[1])[2] > 0.0 and done_female.index(i) < 15
                                                   else "Not Accepted"))
                    self.tableWidget_2.item(self.tableWidget_2.rowCount() - 1, 4).setBackground(
                        give_color_to_status(done_female.index(i), (i[1])[2]))
            self.clear()
        except Exception as show:
            print(show)
            self.clear()

    def student_info(self):
        if self.name_le.text() == "":
            self.error_up.setText("*Please enter your name ")
            self.error_up.setStyleSheet("color:red;")
            self.error_up.adjustSize()
            self.name_le.setFocus()
            QTimer.singleShot(2000, lambda: self.error_up.clear())
        elif self.id_le.text() == "":
            self.error_up.setText("*Please enter your ID ")
            self.error_up.setStyleSheet("color:red;")
            self.error_up.adjustSize()
            self.id_le.setFocus()
            QTimer.singleShot(2000, lambda: self.error_up.clear())
        elif self.gpa_le.text() == "":
            self.error_up.setText("*Please enter your GPA ")
            self.error_up.setStyleSheet("color:red;")
            self.error_up.adjustSize()
            self.gpa_le.setFocus()
            QTimer.singleShot(2000, lambda: self.error_up.clear())
        elif self.comboBox.currentText() == "Gender":
            self.error_up.setText("*Please select your Gender ")
            self.error_up.setStyleSheet("color:red;")
            self.error_up.adjustSize()
            self.comboBox.setFocus()
            QTimer.singleShot(2000, lambda: self.error_up.clear())
        elif self.subject_list.currentText() == "Subject":
            self.error_d.setStyleSheet("color:red;")
            self.error_d.setText("*Please select a subject ")
            self.error_d.adjustSize()
            self.subject_list.setFocus()
            QTimer.singleShot(2000, lambda: self.error_d.clear())
        elif self.grade_le.text() == "":
            self.error_d.setStyleSheet("color:red;")
            self.error_d.setText(
                "*Please Enter your grade in {0}.. if you completed adding all the subjects you studied click submit".format(
                    self.subject_list.currentText()))
            self.error_d.adjustSize()
            self.grade_le.setFocus()
            QTimer.singleShot(5000, lambda: self.error_d.clear())
        elif self.semester_list.currentText() == "Semester":
            self.error_d.setStyleSheet("color:red;")
            self.error_d.setText("*Please select a semester")
            self.error_d.adjustSize()
            self.grade_le.setFocus()
            QTimer.singleShot(2000, lambda: self.error_d.clear())
        else:
            try:
                date = self.semester_list.currentText(
                )[0:4] + self.semester_list.currentText()[5]
                if date[4] == "S":
                    date = date[0:4] + "3"
                self.edu_info[self.subject_list.currentText()] = (
                    self.grade_le.text(), int(date))
                self.error_up.clear()
                self.error_d.clear()
                self.name_le.setReadOnly(True)
                self.id_le.setReadOnly(True)
                self.gpa_le.setReadOnly(True)
                self.grade_le.clear()
                self.subject_list.removeItem(self.subject_list.currentIndex())
                if len(self.subject_list) == 0:
                    self.add_b.setEnabled(False)
                self.submit_b.setEnabled(True)
            except Exception as k:
                print(k)
                self.clear()

    def clear(self):
        try:
            self.edu_info.clear()
            self.semester.clear()
            self.subject_list.clear()
            self.subject_list.addItem("Subject")
            self.subject_list.addItem("CPIT 110")
            self.subject_list.addItem("CPIT 201")
            self.subject_list.addItem("CPIT 221")
            self.subject_list.addItem("CPCS 202")
            self.subject_list.addItem("CPCS 203")
            self.subject_list.addItem("ELI 104")
            self.subject_list.addItem("MATH 110")
            self.placeholder(self.comboBox, "r")
            self.placeholder(self.semester_list, "r")
            self.placeholder(self.subject_list, "r")
            self.name_le.setReadOnly(False)
            self.id_le.setReadOnly(False)
            self.gpa_le.setReadOnly(False)
            self.subject_list.setEnabled(False)
            self.semester_list.setEnabled(False)
            self.grade_le.setEnabled(False)
            self.add_b.setEnabled(True)
            self.submit_b.setEnabled(False)
            self.name_le.clear()
            self.gpa_le.clear()
            self.id_le.clear()
            self.grade_le.clear()
        except Exception as k:
            print(k)
            self.clear()

    def add_semesters_based_on_id(self):
        try:
            import datetime
            now = datetime.datetime.now()
            # if the date is Hijri convert it .
            if str(datetime.datetime.now().year)[0] != '2':
                now = (float(datetime.datetime.now().year) * 0.97) + 622

            if len(self.id_le.text()) <= 3 or (self.id_le.text()[0] != "1" and int(self.id_le.text()[0]) != int(str(now.year)[2])):
                self.show_message("This is invalid ID !\n\nPlease try again using valid student ID\n\ne.g\'1855415,1655555,2012023",
                                  "Incorrect", "id")
                return
            if int(str(now.year)[2:4]) < int(self.id_le.text()[0:2]):
                self.show_message(
                    "You seemed to be a new student of KAU\n\nPlease try again later when you finish\nMATH 110, CPIT 110 and ELI 104 :)", "Oops", "id")
                return
            if self.id_le.text() in self.sorting_male or self.id_le.text() in self.sorting_female:
                self.show_message(
                    "Oops this ID is already in the system ..", "Oops", "")
                return
            self.semester_list.setEnabled(True)
            self.subject_list.setEnabled(True)
            self.grade_le.setEnabled(True)
            year_of_register = self.id_le.text()[0:2]
            self.semester_list.clear()
            self.semester_list.addItem("Semester")

            # if you run this program next year you will see new semesters added to the list :)
            while int(year_of_register) <= int(str(now.year)[2:4]):
                self.semester_list.addItem("20" + str(year_of_register) + "-1")
                self.semester_list.addItem("20" + str(year_of_register) + "-2")
                self.semester_list.addItem(
                    "20" + str(year_of_register) + "-Summer")
                year_of_register = int(year_of_register) + 1
            # because sometimes it happens you finished the first semester before the end of the year
            self.semester_list.addItem("20" + str(year_of_register) + "-1")
        except Exception as k:
            print(k)
            self.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
