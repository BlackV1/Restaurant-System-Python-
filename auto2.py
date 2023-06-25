from datetime import datetime

import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QListWidgetItem, QTableWidgetItem


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1921, 1080)
        MainWindow.setStyleSheet("font: 63 8pt \"Yu Gothic UI Semibold\";\n"
                                 "background-color: rgb(101, 112, 136);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, -30, 1931, 1121))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.password_input = QtWidgets.QLineEdit(self.tab)
        self.password_input.setGeometry(QtCore.QRect(850, 540, 281, 61))
        self.password_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_input.setObjectName("password_input")

        self.username_input = QtWidgets.QLineEdit(self.tab)
        self.username_input.setGeometry(QtCore.QRect(850, 460, 281, 61))
        self.username_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.username_input.setMaxLength(2)

        self.username_label = QtWidgets.QLabel(self.tab)
        self.username_label.setGeometry(QtCore.QRect(740, 470, 71, 41))
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 12pt \"MS Shell Dlg 2\";")
        self.username_label.setObjectName("username_label")

        self.password_label = QtWidgets.QLabel(self.tab)
        self.password_label.setGeometry(QtCore.QRect(740, 540, 71, 41))
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 12pt \"MS Shell Dlg 2\";")
        self.password_label.setObjectName("password_label")

        self.error_label = QtWidgets.QLabel(self.tab)
        self.error_label.setGeometry(QtCore.QRect(850, 600, 400, 41))
        self.error_label.setStyleSheet("backgroung-color: rgb(101, 112, 136);\n"
                                       "color: rgb(101, 112, 136);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")
        self.error_label.setObjectName("error_label")

        self.Button7 = QtWidgets.QPushButton(self.tab)
        self.Button7.setGeometry(QtCore.QRect(1160, 380, 61, 51))
        self.Button7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button7.setObjectName("Button7")

        self.Button5 = QtWidgets.QPushButton(self.tab)
        self.Button5.setGeometry(QtCore.QRect(1230, 440, 61, 51))
        self.Button5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button5.setObjectName("Button5")

        self.Button4 = QtWidgets.QPushButton(self.tab)
        self.Button4.setGeometry(QtCore.QRect(1160, 440, 61, 51))
        self.Button4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button4.setObjectName("Button4")

        self.Button9 = QtWidgets.QPushButton(self.tab)
        self.Button9.setGeometry(QtCore.QRect(1300, 380, 61, 51))
        self.Button9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button9.setObjectName("Button9")

        self.Button8 = QtWidgets.QPushButton(self.tab)
        self.Button8.setGeometry(QtCore.QRect(1230, 380, 61, 51))
        self.Button8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button8.setObjectName("Button8")

        self.Button3 = QtWidgets.QPushButton(self.tab)
        self.Button3.setGeometry(QtCore.QRect(1300, 500, 61, 51))
        self.Button3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button3.setObjectName("Button3")

        self.Button2 = QtWidgets.QPushButton(self.tab)
        self.Button2.setGeometry(QtCore.QRect(1230, 500, 61, 51))
        self.Button2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button2.setObjectName("Button2")

        self.Button6 = QtWidgets.QPushButton(self.tab)
        self.Button6.setGeometry(QtCore.QRect(1300, 440, 61, 51))
        self.Button6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button6.setObjectName("Button6")

        self.Button1 = QtWidgets.QPushButton(self.tab)
        self.Button1.setGeometry(QtCore.QRect(1160, 500, 61, 51))
        self.Button1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button1.setObjectName("Button1")

        self.Button0 = QtWidgets.QPushButton(self.tab)
        self.Button0.setGeometry(QtCore.QRect(1230, 560, 61, 51))
        self.Button0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button0.setObjectName("Button0")

        self.ButtonSignIn = QtWidgets.QPushButton(self.tab)
        self.ButtonSignIn.setGeometry(QtCore.QRect(1160, 560, 61, 51))
        self.ButtonSignIn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonSignIn.setObjectName("ButtonSignIn")

        self.ButtonDelete = QtWidgets.QPushButton(self.tab)
        self.ButtonDelete.setGeometry(QtCore.QRect(1300, 560, 61, 51))
        self.ButtonDelete.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonDelete.setObjectName("ButtonDelete")

        self.closeButton = QtWidgets.QPushButton(self.tab)
        self.closeButton.setGeometry(QtCore.QRect(1690, 850, 200, 81))
        self.closeButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")
        self.closeButton.setCheckable(False)
        self.closeButton.setObjectName("closeButton")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(840, 130, 301, 171))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: italic 40pt \"Monotype Corsiva\";")
        self.label.setObjectName("label")

        self.tabWidget.addTab(self.tab, "")

        # /////////////////////////////////////////////////////////

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label2 = QtWidgets.QLabel(self.tab_2)
        self.label2.setGeometry(QtCore.QRect(30, 800, 301, 171))
        font2 = QtGui.QFont()
        font2.setFamily("Monotype Corsiva")
        font2.setPointSize(40)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        self.label2.setFont(font2)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: italic 40pt \"Monotype Corsiva\";")
        self.label2.setObjectName("label2")

        self.createOrder = QtWidgets.QPushButton(self.tab_2)
        self.createOrder.setGeometry(QtCore.QRect(10, 20, 201, 91))
        self.createOrder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.createOrder.setObjectName("createOrder")

        self.editOrder = QtWidgets.QPushButton(self.tab_2)
        self.editOrder.setGeometry(QtCore.QRect(230, 20, 201, 91))
        self.editOrder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.editOrder.setObjectName("editOrder")

        self.StopList = QtWidgets.QPushButton(self.tab_2)
        self.StopList.setGeometry(QtCore.QRect(460, 20, 201, 91))
        self.StopList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StopList.setObjectName("StopList")

        self.closedReceipts = QtWidgets.QPushButton(self.tab_2)
        self.closedReceipts.setGeometry(QtCore.QRect(690, 20, 201, 91))
        self.closedReceipts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.closedReceipts.setObjectName("closedReceipts")

        self.employeeSettings = QtWidgets.QPushButton(self.tab_2)
        self.employeeSettings.setGeometry(QtCore.QRect(240, 370, 201, 91))
        self.employeeSettings.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employeeSettings.setObjectName("employeeSettings")

        self.employeeInfo = QtWidgets.QPushButton(self.tab_2)
        self.employeeInfo.setGeometry(QtCore.QRect(10, 370, 201, 91))
        self.employeeInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employeeInfo.setObjectName("employeeInfo")

        self.exitButton = QtWidgets.QPushButton(self.tab_2)
        self.exitButton.setGeometry(QtCore.QRect(1690, 850, 171, 81))
        self.exitButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.exitButton.setCheckable(False)
        self.exitButton.setObjectName("exitButton")

        self.shiftReport = QtWidgets.QPushButton(self.tab_2)
        self.shiftReport.setGeometry(QtCore.QRect(1670, 160, 201, 91))
        self.shiftReport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.shiftReport.setObjectName("shiftReport")

        self.closeShift = QtWidgets.QPushButton(self.tab_2)
        self.closeShift.setGeometry(QtCore.QRect(1670, 40, 201, 91))
        self.closeShift.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.closeShift.setObjectName("closeShift")

        self.tabWidget.addTab(self.tab_2, "")

        # /////////////////////////////////////////////////////////

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.printOrder = QtWidgets.QPushButton(self.tab_3)
        self.printOrder.setGeometry(QtCore.QRect(1000, 800, 201, 91))
        self.printOrder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.printOrder.setObjectName("printOrder")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTimeEdit.setGeometry(QtCore.QRect(50, 40, 131, 31))
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.summ_label = QtWidgets.QLabel(self.tab_3)
        self.summ_label.setGeometry(QtCore.QRect(50, 800, 250, 50))
        self.summ_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.summ_label.setObjectName("error_label")

        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(50, 80, 810, 691))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Наименование блюда', 'Количество', 'Цена'])
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 200)

        self.backButton = QtWidgets.QPushButton(self.tab_3)
        self.backButton.setGeometry(QtCore.QRect(1690, 850, 171, 81))
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.backButton.setCheckable(False)
        self.backButton.setObjectName("exitButton")

        self.Button7_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button7_3.setGeometry(QtCore.QRect(1500, 80, 61, 51))
        self.Button7_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button7_3.setObjectName("Button7_3")

        self.Button8_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button8_3.setGeometry(QtCore.QRect(1570, 80, 61, 51))
        self.Button8_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button8_3.setObjectName("Button8_3")

        self.Button9_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button9_3.setGeometry(QtCore.QRect(1640, 80, 61, 51))
        self.Button9_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button9_3.setObjectName("Button9_3")

        self.Button4_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button4_3.setGeometry(QtCore.QRect(1500, 140, 61, 51))
        self.Button4_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button4_3.setObjectName("Button4_3")

        self.Button5_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button5_3.setGeometry(QtCore.QRect(1570, 140, 61, 51))
        self.Button5_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button5_3.setObjectName("Button5_3")

        self.Button6_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button6_3.setGeometry(QtCore.QRect(1640, 140, 61, 51))
        self.Button6_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button6_3.setObjectName("Button6_3")

        self.Button3_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button3_3.setGeometry(QtCore.QRect(1640, 200, 61, 51))
        self.Button3_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button3_3.setObjectName("Button3_3")

        self.Button2_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button2_3.setGeometry(QtCore.QRect(1570, 200, 61, 51))
        self.Button2_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button2_3.setObjectName("Button2_3")

        self.Button1_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button1_3.setGeometry(QtCore.QRect(1500, 200, 61, 51))
        self.Button1_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button1_3.setObjectName("Button1_3")

        self.Button0_3 = QtWidgets.QPushButton(self.tab_3)
        self.Button0_3.setGeometry(QtCore.QRect(1570, 260, 61, 51))
        self.Button0_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button0_3.setObjectName("Button0_3")

        self.ButtonDelete2 = QtWidgets.QPushButton(self.tab_3)
        self.ButtonDelete2.setGeometry(QtCore.QRect(1720, 320, 61, 51))
        self.ButtonDelete2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonDelete2.setObjectName("ButtonDelete2")

        self.quantityLine = QtWidgets.QLineEdit(self.tab_3)
        self.quantityLine.setGeometry(QtCore.QRect(1500, 320, 201, 51))
        self.quantityLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantityLine.setText("")
        self.quantityLine.setObjectName("quantityLine")

        # Создаем список результатов
        self.result_list = QtWidgets.QListWidget(self.tab_3)
        self.result_list.setGeometry(QtCore.QRect(940, 200, 541, 300))
        self.result_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")

        self.searchLine = QtWidgets.QLineEdit(self.tab_3)
        self.searchLine.setGeometry(QtCore.QRect(940, 80, 541, 71))
        self.searchLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchLine.setText("")
        self.searchLine.setObjectName("searchLine")

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        # ///////////////////////////////////////////////
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.tableWidget2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget2.setGeometry(QtCore.QRect(50, 80, 810, 691))
        self.tableWidget2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.setColumnCount(4)
        header = self.tableWidget2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget2.setHorizontalHeaderLabels(['Ф.И.О.', 'Должность', 'Логин', 'Пароль'])

        self.backToMenuButton = QtWidgets.QPushButton(self.tab_4)
        self.backToMenuButton.setGeometry(QtCore.QRect(1690, 850, 171, 81))
        self.backToMenuButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 10pt \"MS Shell Dlg 2\";\n"
                                            "font: 12pt \"MS Shell Dlg 2\";")
        self.backToMenuButton.setCheckable(False)
        self.backToMenuButton.setObjectName("backToMenuButton")

        # ////////////////////////////////////////

        self.tab_edit_order = QtWidgets.QWidget()
        self.tab_edit_order.setObjectName("tab_edit_order")
        self.tabWidget.addTab(self.tab_edit_order, "")

        self.backToMenuButton2 = QtWidgets.QPushButton(self.tab_edit_order)
        self.backToMenuButton2.setGeometry(QtCore.QRect(1690, 850, 171, 81))
        self.backToMenuButton2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";\n"
                                             "font: 12pt \"MS Shell Dlg 2\";")
        self.backToMenuButton2.setCheckable(False)
        self.backToMenuButton2.setObjectName("backToMenuButton2")

        self.order_list = QtWidgets.QListWidget(self.tab_edit_order)
        self.order_list.setGeometry(QtCore.QRect(940, 550, 541, 300))
        self.order_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")

        self.result_list_edit = QtWidgets.QListWidget(self.tab_edit_order)
        self.result_list_edit.setGeometry(QtCore.QRect(940, 200, 541, 300))
        self.result_list_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";")

        self.summ_label_edit = QtWidgets.QLabel(self.tab_edit_order)
        self.summ_label_edit.setGeometry(QtCore.QRect(50, 800, 250, 50))
        self.summ_label_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "font: 12pt \"MS Shell Dlg 2\";")
        self.summ_label_edit.setObjectName("summ_label_edit")

        self.Button7_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button7_edit.setGeometry(QtCore.QRect(1500, 80, 61, 51))
        self.Button7_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button7_edit.setObjectName("Button7_edit")

        self.Button8_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button8_edit.setGeometry(QtCore.QRect(1570, 80, 61, 51))
        self.Button8_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button8_edit.setObjectName("Button8_edit")

        self.Button9_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button9_edit.setGeometry(QtCore.QRect(1640, 80, 61, 51))
        self.Button9_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button9_edit.setObjectName("Button9_edit")

        self.Button4_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button4_edit.setGeometry(QtCore.QRect(1500, 140, 61, 51))
        self.Button4_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button4_edit.setObjectName("Button4_3")

        self.Button5_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button5_edit.setGeometry(QtCore.QRect(1570, 140, 61, 51))
        self.Button5_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button5_edit.setObjectName("Button5_edit")

        self.Button6_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button6_edit.setGeometry(QtCore.QRect(1640, 140, 61, 51))
        self.Button6_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button6_edit.setObjectName("Button6_edit")

        self.Button3_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button3_edit.setGeometry(QtCore.QRect(1640, 200, 61, 51))
        self.Button3_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button3_edit.setObjectName("Button3_edit")

        self.Button2_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button2_edit.setGeometry(QtCore.QRect(1570, 200, 61, 51))
        self.Button2_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button2_edit.setObjectName("Button2_edit")

        self.Button1_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button1_edit.setGeometry(QtCore.QRect(1500, 200, 61, 51))
        self.Button1_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button1_edit.setObjectName("Button1_edit")

        self.Button0_edit = QtWidgets.QPushButton(self.tab_edit_order)
        self.Button0_edit.setGeometry(QtCore.QRect(1570, 260, 61, 51))
        self.Button0_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button0_edit.setObjectName("Button0_edit")

        self.ButtonDelete4 = QtWidgets.QPushButton(self.tab_edit_order)
        self.ButtonDelete4.setGeometry(QtCore.QRect(1720, 320, 61, 51))
        self.ButtonDelete4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonDelete4.setObjectName("ButtonDelete2")

        self.quantityLineEdit = QtWidgets.QLineEdit(self.tab_edit_order)
        self.quantityLineEdit.setGeometry(QtCore.QRect(1500, 320, 201, 51))
        self.quantityLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantityLineEdit.setText("")
        self.quantityLineEdit.setObjectName("quantityLineEdit")

        self.searchLineEdit = QtWidgets.QLineEdit(self.tab_edit_order)
        self.searchLineEdit.setGeometry(QtCore.QRect(940, 80, 541, 71))
        self.searchLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchLineEdit.setText("")
        self.searchLineEdit.setObjectName("searchLineEdit")

        self.tableWidget_edit = QtWidgets.QTableWidget(self.tab_edit_order)
        self.tableWidget_edit.setGeometry(QtCore.QRect(50, 80, 810, 691))
        self.tableWidget_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget_edit.setColumnCount(3)
        self.tableWidget_edit.setHorizontalHeaderLabels(['Наименование блюда', 'Количество', 'Цена'])
        self.tableWidget_edit.setColumnWidth(0, 300)
        self.tableWidget_edit.setColumnWidth(1, 300)
        self.tableWidget_edit.setColumnWidth(2, 200)

        self.EditOrderButton = QtWidgets.QPushButton(self.tab_edit_order)
        self.EditOrderButton.setGeometry(QtCore.QRect(1690, 700, 171, 81))
        self.EditOrderButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EditOrderButton.setCheckable(False)
        self.EditOrderButton.setObjectName("EditOrderButton")

        self.DeleteChangedDishButton = QtWidgets.QPushButton(self.tab_edit_order)
        self.DeleteChangedDishButton.setGeometry(QtCore.QRect(1690, 600, 171, 81))
        self.DeleteChangedDishButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DeleteChangedDishButton.setCheckable(False)
        self.DeleteChangedDishButton.setObjectName("DeleteChangedDishButton")

        self.PrintAndCloseOrder = QtWidgets.QPushButton(self.tab_edit_order)
        self.PrintAndCloseOrder.setGeometry(QtCore.QRect(690, 800, 171, 81))
        self.PrintAndCloseOrder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PrintAndCloseOrder.setCheckable(False)
        self.PrintAndCloseOrder.setObjectName("PrintAndCloseOrder")
        MainWindow.setCentralWidget(self.centralwidget)

        # /////////////////////////////////////////////////////////

        self.tab_stop = QtWidgets.QWidget()
        self.tab_stop.setObjectName("tab_Stop_List")

        self.tableWidget3 = QtWidgets.QTableWidget(self.tab_stop)
        self.tableWidget3.setGeometry(QtCore.QRect(50, 80, 810, 691))
        self.tableWidget3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget3.setColumnCount(2)
        self.tableWidget3.setHorizontalHeaderLabels(['Наименование блюда', 'Количество'])
        self.tableWidget3.setColumnWidth(0, 400)
        self.tableWidget3.setColumnWidth(1, 400)

        self.backButton2 = QtWidgets.QPushButton(self.tab_stop)
        self.backButton2.setGeometry(QtCore.QRect(1690, 850, 171, 81))
        self.backButton2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")
        self.backButton2.setCheckable(False)
        self.backButton2.setObjectName("exitButton")

        self.Button7_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button7_4.setGeometry(QtCore.QRect(1500, 80, 61, 51))
        self.Button7_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button7_4.setObjectName("Button7_3")

        self.Button8_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button8_4.setGeometry(QtCore.QRect(1570, 80, 61, 51))
        self.Button8_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button8_4.setObjectName("Button8_3")

        self.Button9_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button9_4.setGeometry(QtCore.QRect(1640, 80, 61, 51))
        self.Button9_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button9_4.setObjectName("Button9_3")

        self.Button4_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button4_4.setGeometry(QtCore.QRect(1500, 140, 61, 51))
        self.Button4_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button4_4.setObjectName("Button4_3")

        self.Button5_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button5_4.setGeometry(QtCore.QRect(1570, 140, 61, 51))
        self.Button5_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button5_4.setObjectName("Button5_3")

        self.Button6_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button6_4.setGeometry(QtCore.QRect(1640, 140, 61, 51))
        self.Button6_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button6_4.setObjectName("Button6_3")

        self.Button3_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button3_4.setGeometry(QtCore.QRect(1640, 200, 61, 51))
        self.Button3_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button3_4.setObjectName("Button3_3")

        self.Button2_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button2_4.setGeometry(QtCore.QRect(1570, 200, 61, 51))
        self.Button2_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button2_4.setObjectName("Button2_3")

        self.Button1_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button1_4.setGeometry(QtCore.QRect(1500, 200, 61, 51))
        self.Button1_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button1_4.setObjectName("Button1_3")

        self.Button0_4 = QtWidgets.QPushButton(self.tab_stop)
        self.Button0_4.setGeometry(QtCore.QRect(1570, 260, 61, 51))
        self.Button0_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button0_4.setObjectName("Button0_3")

        self.ButtonDelete3 = QtWidgets.QPushButton(self.tab_stop)
        self.ButtonDelete3.setGeometry(QtCore.QRect(1720, 320, 61, 51))
        self.ButtonDelete3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonDelete3.setObjectName("ButtonDelete2")

        self.ButtonClearStopList = QtWidgets.QPushButton(self.tab_stop)
        self.ButtonClearStopList.setGeometry(QtCore.QRect(50, 800, 250, 50))
        self.ButtonClearStopList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButtonClearStopList.setObjectName("ButtonClearStopList")

        self.quantityLine2 = QtWidgets.QLineEdit(self.tab_stop)
        self.quantityLine2.setGeometry(QtCore.QRect(1500, 320, 201, 51))
        self.quantityLine2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantityLine2.setText("")
        self.quantityLine2.setObjectName("quantityLine2")

        # Создаем список результатов
        self.result_list2 = QtWidgets.QListWidget(self.tab_stop)
        self.result_list2.setGeometry(QtCore.QRect(940, 200, 541, 300))
        self.result_list2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")

        self.searchLine2 = QtWidgets.QLineEdit(self.tab_stop)
        self.searchLine2.setGeometry(QtCore.QRect(940, 80, 541, 71))
        self.searchLine2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchLine2.setText("")
        self.searchLine2.setObjectName("searchLine2")

        self.tabWidget.addTab(self.tab_stop, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Логин"))
        self.password_label.setText(_translate("MainWindow", "Пароль"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Введите логин: "))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Введите пароль: "))
        self.error_label.setText(_translate("MainWindow", "Неправильный логин или пароль"))

        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button0.setText(_translate("MainWindow", "0"))

        self.Button0.clicked.connect(lambda: self.input_autorization(0))
        self.Button1.clicked.connect(lambda: self.input_autorization(1))
        self.Button2.clicked.connect(lambda: self.input_autorization(2))
        self.Button3.clicked.connect(lambda: self.input_autorization(3))
        self.Button4.clicked.connect(lambda: self.input_autorization(4))
        self.Button5.clicked.connect(lambda: self.input_autorization(5))
        self.Button6.clicked.connect(lambda: self.input_autorization(6))
        self.Button7.clicked.connect(lambda: self.input_autorization(7))
        self.Button8.clicked.connect(lambda: self.input_autorization(8))
        self.Button9.clicked.connect(lambda: self.input_autorization(9))

        self.ButtonSignIn.setText(_translate("MainWindow", "Войти"))
        self.closeButton.setText(_translate("MainWindow", "Выход из программы"))
        self.ButtonDelete.setText(_translate("MainWindow", "Удалить"))
        self.ButtonDelete2.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Rest-System"))
        self.label2.setText(_translate("MainWindow", "Rest-System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Autorization"))
        self.createOrder.setText(_translate("MainWindow", "Создать заказ"))
        self.editOrder.setText(_translate("MainWindow", "Редактировать заказ"))
        self.EditOrderButton.setText(_translate("MainWindow", "Завершить изменения"))
        self.PrintAndCloseOrder.setText(_translate("MainWindow", "Печать чека\nЗакрытие заказа"))
        self.DeleteChangedDishButton.setText(_translate("MainWindow", "Удалить позицию"))
        self.StopList.setText(_translate("MainWindow", "Стоп - лист"))
        self.closedReceipts.setText(_translate("MainWindow", "Закрытые чеки"))
        self.employeeSettings.setText(_translate("MainWindow", "Настройки персонала"))
        self.employeeInfo.setText(_translate("MainWindow", "Информация о персонале"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.shiftReport.setText(_translate("MainWindow", "Отчёт за смену"))
        self.closeShift.setText(_translate("MainWindow", "Закрыть смену"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MainMenu"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Наименование блюда"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Кол-во"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        __sortingEnabled2 = self.tableWidget2.isSortingEnabled()
        self.tableWidget2.setSortingEnabled(False)
        self.tableWidget2.setSortingEnabled(__sortingEnabled)

        __sortingEnabled3 = self.tableWidget_edit.isSortingEnabled()
        self.tableWidget_edit.setSortingEnabled(False)
        self.tableWidget_edit.setSortingEnabled(__sortingEnabled)

        self.Button7_3.setText(_translate("MainWindow", "7"))
        self.Button8_3.setText(_translate("MainWindow", "8"))
        self.Button9_3.setText(_translate("MainWindow", "9"))
        self.Button4_3.setText(_translate("MainWindow", "4"))
        self.Button5_3.setText(_translate("MainWindow", "5"))
        self.Button6_3.setText(_translate("MainWindow", "6"))
        self.Button3_3.setText(_translate("MainWindow", "3"))
        self.Button2_3.setText(_translate("MainWindow", "2"))
        self.Button1_3.setText(_translate("MainWindow", "1"))
        self.Button0_3.setText(_translate("MainWindow", "0"))

        self.Button7_4.setText(_translate("MainWindow", "7"))
        self.Button8_4.setText(_translate("MainWindow", "8"))
        self.Button9_4.setText(_translate("MainWindow", "9"))
        self.Button4_4.setText(_translate("MainWindow", "4"))
        self.Button5_4.setText(_translate("MainWindow", "5"))
        self.Button6_4.setText(_translate("MainWindow", "6"))
        self.Button3_4.setText(_translate("MainWindow", "3"))
        self.Button2_4.setText(_translate("MainWindow", "2"))
        self.Button1_4.setText(_translate("MainWindow", "1"))
        self.Button0_4.setText(_translate("MainWindow", "0"))

        self.Button7_edit.setText(_translate("MainWindow", "7"))
        self.Button8_edit.setText(_translate("MainWindow", "8"))
        self.Button9_edit.setText(_translate("MainWindow", "9"))
        self.Button4_edit.setText(_translate("MainWindow", "4"))
        self.Button5_edit.setText(_translate("MainWindow", "5"))
        self.Button6_edit.setText(_translate("MainWindow", "6"))
        self.Button3_edit.setText(_translate("MainWindow", "3"))
        self.Button2_edit.setText(_translate("MainWindow", "2"))
        self.Button1_edit.setText(_translate("MainWindow", "1"))
        self.Button0_edit.setText(_translate("MainWindow", "0"))

        self.ButtonDelete3.setText(_translate("MainWindow", "Очистить"))
        self.ButtonDelete4.setText(_translate("MainWindow", "Очистить"))
        self.backButton.setText(_translate("MainWindow", "Назад"))
        self.ButtonClearStopList.setText(_translate("MainWindow", "Очистить стоп-лист"))
        self.backButton2.setText(_translate("MainWindow", "Назад"))
        self.backToMenuButton.setText(_translate("MainWindow", "Назад"))
        self.backToMenuButton2.setText(_translate("MainWindow", "Назад"))
        self.summ_label.setText(_translate("MainWindow", "Сумма: "))
        self.summ_label_edit.setText(_translate("MainWindow", "Сумма: "))
        self.printOrder.setText(_translate("MainWindow", "Создать"))

        self.Button0_3.clicked.connect(lambda: self.input_quantity(0))
        self.Button1_3.clicked.connect(lambda: self.input_quantity(1))
        self.Button2_3.clicked.connect(lambda: self.input_quantity(2))
        self.Button3_3.clicked.connect(lambda: self.input_quantity(3))
        self.Button4_3.clicked.connect(lambda: self.input_quantity(4))
        self.Button5_3.clicked.connect(lambda: self.input_quantity(5))
        self.Button6_3.clicked.connect(lambda: self.input_quantity(6))
        self.Button7_3.clicked.connect(lambda: self.input_quantity(7))
        self.Button8_3.clicked.connect(lambda: self.input_quantity(8))
        self.Button9_3.clicked.connect(lambda: self.input_quantity(9))

        self.Button0_4.clicked.connect(lambda: self.input_stop_quantity(0))
        self.Button1_4.clicked.connect(lambda: self.input_stop_quantity(1))
        self.Button2_4.clicked.connect(lambda: self.input_stop_quantity(2))
        self.Button3_4.clicked.connect(lambda: self.input_stop_quantity(3))
        self.Button4_4.clicked.connect(lambda: self.input_stop_quantity(4))
        self.Button5_4.clicked.connect(lambda: self.input_stop_quantity(5))
        self.Button6_4.clicked.connect(lambda: self.input_stop_quantity(6))
        self.Button7_4.clicked.connect(lambda: self.input_stop_quantity(7))
        self.Button8_4.clicked.connect(lambda: self.input_stop_quantity(8))
        self.Button9_4.clicked.connect(lambda: self.input_stop_quantity(9))

        self.Button0_edit.clicked.connect(lambda: self.input_edit_quantity(0))
        self.Button1_edit.clicked.connect(lambda: self.input_edit_quantity(1))
        self.Button2_edit.clicked.connect(lambda: self.input_edit_quantity(2))
        self.Button3_edit.clicked.connect(lambda: self.input_edit_quantity(3))
        self.Button4_edit.clicked.connect(lambda: self.input_edit_quantity(4))
        self.Button5_edit.clicked.connect(lambda: self.input_edit_quantity(5))
        self.Button6_edit.clicked.connect(lambda: self.input_edit_quantity(6))
        self.Button7_edit.clicked.connect(lambda: self.input_edit_quantity(7))
        self.Button8_edit.clicked.connect(lambda: self.input_edit_quantity(8))
        self.Button9_edit.clicked.connect(lambda: self.input_edit_quantity(9))

        self.backButton2.clicked.connect(self.switch_to_MainMenu)
        self.quantityLine.setPlaceholderText(_translate("MainWindow", "Введите количество: "))
        self.searchLine.setPlaceholderText(_translate("MainWindow", "Введите название блюда: "))

        self.quantityLine2.setPlaceholderText(_translate("MainWindow", "Введите количество: "))
        self.searchLine2.setPlaceholderText(_translate("MainWindow", "Введите название блюда: "))
        self.quantityLineEdit.setPlaceholderText(_translate("MainWindow", "Введите количество: "))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Введите название блюда: "))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "CreateOrder"))

        self.printOrder.clicked.connect(self.create_order)
        self.PrintAndCloseOrder.clicked.connect(self.print_and_close_order)
        self.DeleteChangedDishButton.clicked.connect(self.remove_row)
        self.EditOrderButton.clicked.connect(self.finish_edit)
        self.ButtonDelete4.clicked.connect(self.clear_quantity_search_edit_line)
        self.editOrder.clicked.connect(self.switch_to_editOrder)
        self.exitButton.clicked.connect(self.switch_to_Autorization)
        self.closeButton.clicked.connect(self.exit)
        self.ButtonDelete3.clicked.connect(self.clear_stop_quantity_line)
        self.backButton.clicked.connect(self.switch_to_MainMenu)
        self.ButtonDelete.clicked.connect(self.clear_auto_input)
        self.createOrder.clicked.connect(self.switch_to_CreateOrder)
        self.employeeInfo.clicked.connect(self.get_position)
        self.backToMenuButton.clicked.connect(self.switch_Employees_to_MainMenu)
        self.backToMenuButton2.clicked.connect(self.switch_editTab_to_MainMenu)
        self.shiftReport.clicked.connect(self.get_shift_report)
        self.closeShift.clicked.connect(self.close_shift)
        self.ButtonClearStopList.clicked.connect(self.clear_stop_list)
        self.StopList.clicked.connect(self.switch_to_StopList)
        self.ButtonDelete2.clicked.connect(self.clear_quantity_line)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MainMenu"))
        self.password_input.setEchoMode(QLineEdit.Password)  # скрываем пароль звездочками
        self.ButtonSignIn.clicked.connect(self.check_login)  # обработчик нажатия на кнопку

        self.sum = 0

        self.order_count = 0
        self.orders = {}

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='$MercF1$Team#',
            db='restaurant'
        )

        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='$MercF1$Team#',
            db='restaurant',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # Создаем курсор для выполнения запросов
        self.cursor = self.conn.cursor()

        self.itemText = ""

        self.searchLine.textChanged.connect(self.search_database)
        self.result_list.itemClicked.connect(self.add_to_table)

        self.searchLine2.textChanged.connect(self.search_stop_database)
        self.result_list2.itemClicked.connect(self.add_to_stop_table)

        self.searchLineEdit.textChanged.connect(self.search_edit_database)
        self.order_list.itemClicked.connect(self.show_order_to_edit)
        self.result_list_edit.itemClicked.connect(self.add_to_edit_table)

    def search_database(self):
        # Очищаем список результатов перед началом нового поиска
        self.result_list.clear()

        # Извлекаем данные из базы данных
        query = "SELECT name, price FROM menu WHERE name LIKE %s"
        value = "%" + self.searchLine.text() + "%"
        self.cursor.execute(query, (value,))
        results = self.cursor.fetchall()

        # Выводим результаты в список
        for result in results:
            self.result_list.addItem(result['name'])

    def search_edit_database(self):
        # Очищаем список результатов перед началом нового поиска
        self.result_list_edit.clear()

        # Извлекаем данные из базы данных
        query = "SELECT name, price FROM menu WHERE name LIKE %s"
        value = "%" + self.searchLineEdit.text() + "%"
        self.cursor.execute(query, (value,))
        results = self.cursor.fetchall()

        # Выводим результаты в список
        for result in results:
            self.result_list_edit.addItem(result['name'])

    def search_stop_database(self):
        # Очищаем список результатов перед началом нового поиска
        self.result_list2.clear()

        # Извлекаем данные из базы данных
        query = "SELECT name FROM menu WHERE name LIKE %s"
        value = "%" + self.searchLine2.text() + "%"
        self.cursor.execute(query, (value,))
        results = self.cursor.fetchall()

        # Выводим результаты в список
        for result in results:
            self.result_list2.addItem(result['name'])

    def check_login(self):
        # получаем логин и пароль из полей ввода
        username = self.username_input.text()
        password = self.password_input.text()

        # соединение с базой данных MySQL
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='$MercF1$Team#',
            db='restaurant',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # тип курсора для возврата результатов в виде словаря
        )

        try:
            with conn.cursor() as cursor:
                # выполнение SQL-запроса для поиска пользователя
                sql = "SELECT employees.full_name, position.position FROM employees JOIN position ON " \
                      "employees.position=position.id WHERE employees.username=%s AND employees.password=%s"
                cursor.execute(sql, (username, password))
                user = cursor.fetchone()

                if user is not None:
                    position = user['position']
                    full_name = user['full_name']
                    self.current_position = position
                    self.waiter_name = full_name
                    self.switch_to_MainMenu()
                else:
                    self.auto_error()
        finally:
            # закрытие соединения с базой данных
            conn.close()

    def get_position(self):
        if self.current_position == "Администратор":
            self.tabWidget.setCurrentIndex(3)
            row_count = self.tableWidget2.rowCount()
            self.tableWidget2.insertRow(row_count)
            if row_count < self.tableWidget2.rowCount():
                conn = pymysql.connect(host='localhost', user='root', password='$MercF1$Team#', db='restaurant')

                # создание объекта cursor
                cursor = conn.cursor()

                # выполнение запроса
                query = (
                    "SELECT employees.full_name, position.position, employees.username, employees.password FROM "
                    "employees " \
                    "JOIN position ON employees.position = position.id")
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()

                # обработка результатов запроса
                for i, row in enumerate(results):
                    name = row[0]
                    position = row[1]
                    login = row[2]
                    password = row[3]
                    self.tableWidget2.insertRow(row_count + i)
                    self.tableWidget2.setItem(row_count + i, 0, QtWidgets.QTableWidgetItem(name))
                    self.tableWidget2.setItem(row_count + i, 1, QtWidgets.QTableWidgetItem(position))
                    self.tableWidget2.setItem(row_count + i, 2, QtWidgets.QTableWidgetItem(login))
                    self.tableWidget2.setItem(row_count + i, 3, QtWidgets.QTableWidgetItem(password))
                self.tableWidget2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        else:
            self.error_message()

    def clear_quantity_line(self):
        self.quantityLine.clear()
        self.searchLine.clear()

    def clear_quantity_search_edit_line(self):
        self.quantityLineEdit.clear()
        self.searchLineEdit.clear()

    def clear_stop_list(self):
        if self.current_position == "Администратор":
            msg_box = QMessageBox()
            msg_box.setText("Вы уверены, что хотите очистить стоп-лист?")
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = msg_box.exec_()

            if result == QMessageBox.Yes:
                self.tableWidget3.clearContents()
                self.tableWidget3.setRowCount(0)
                self.quantityLine2.clear()
                self.result_list2.clear()
                self.searchLine2.clear()
            else:
                pass
        else:
            self.error_message()

    def clear_stop_quantity_line(self):
        self.quantityLine2.clear()
        self.searchLine2.clear()

    def error_message(self):
        error_message_box = QMessageBox()
        error_message_box.setIcon(QMessageBox.Critical)
        error_message_box.setWindowTitle("Ошибка доступа")
        error_message_box.setText("У Вас нет доступа к этой информации.")
        error_message_box.exec_()

    def print_and_close_order(self):
        if self.tableWidget_edit.rowCount() != 0:

            print("-------------------Заказ", self.order_count, "-----------------------\n"
                  , "Официант: ", self.waiter_name
                  , "\n--------------------------------------"
                  , f"\nВремя: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"{'Наименование':<30} {'Количество':<15} {'Цена':<10}")

            # Выводим значения в каждой строке таблицы
            for row in range(self.tableWidget_edit.rowCount()):
                price = self.tableWidget_edit.item(row, 2).text()
                name = self.tableWidget_edit.item(row, 0).text()
                quantity = self.tableWidget_edit.item(row, 1).text()
                print(f"{name:<30} {quantity:<15} {price:<10}")

            print("\n--------------------------------------\n", self.summ_label.text()
                  , "\n--------------------------------------\n"
                  ,
                  "Вознаграждение официанту приветствуется\nно всегда остаётся на Ваше усмотрение.\n----------------------------------------------\n\n\n")

            self.switch_editTab_to_MainMenu()

        else:
            error_message_box = QMessageBox()
            error_message_box.setIcon(QMessageBox.Critical)
            error_message_box.setWindowTitle("Ошибка")
            error_message_box.setText("Заказ пуст\nДля начала выберите заказ, завершите все изменения, которые у вас были, а затем можете распечатать чек и закрыть заказ")
            error_message_box.exec_()

    def create_order(self):
        self.tabWidget.setCurrentIndex(1)
        order_list = []
        for row in range(self.tableWidget.rowCount()):
            name = self.tableWidget.item(row, 0).text()
            quantity = int(self.tableWidget.item(row, 1).text())
            price = float(self.tableWidget.item(row, 2).text())
            order_list.append((name, quantity, price))

        self.order_count += 1
        self.orders[self.waiter_name, self.order_count, datetime.now().strftime('%d-%m-%Y %H:%M:%S')] = order_list

        print(self.orders)

        print("-------------------Заказ", self.order_count, "-----------------------\n"
              , "Официант: ", self.waiter_name
              , "\n--------------------------------------")
        print(f"{'Наименование':<30} {'Количество':<15} {'Цена':<10}")

        # Выводим значения в каждой строке таблицы
        for row in range(self.tableWidget.rowCount()):
            price = self.tableWidget.item(row, 2).text()
            name = self.tableWidget.item(row, 0).text()
            quantity = self.tableWidget.item(row, 1).text()
            print(f"{name:<30} {quantity:<15} {price:<10}")

        print("\n--------------------------------------\n", self.summ_label.text())
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.quantityLine.clear()
        self.result_list.clear()
        self.searchLine.clear()
        self.summ_label.setText(f"Общая сумма: ")

    def finish_edit(self):
        self.tabWidget.setCurrentIndex(1)
        self.key_value = None
        for key, values in self.orders.items():
            if f"{key}: {values}" == self.itemText:
                self.key_value = key
                self.orders[key].clear()
                break
        order_list = []
        for row in range(self.tableWidget_edit.rowCount()):
            name = self.tableWidget_edit.item(row, 0).text()
            quantity = int(self.tableWidget_edit.item(row, 1).text())
            price = float(self.tableWidget_edit.item(row, 2).text())
            order_list.append((name, quantity, price))
        self.orders.update({f"{self.key_value}": order_list})
        self.switch_editTab_to_MainMenu()

    def close_shift(self):
        if self.current_position == "Администратор":
            msg_box = QMessageBox()
            msg_box.setText("Вы уверены, что хотите закрыть смену?")
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            result = msg_box.exec_()

            if result == QMessageBox.Yes:
                self.switch_to_Autorization()
                for key, value in self.orders.items():
                    for i in value:
                        self.sum += float(i[2])
                print("-----------------------------Смена "
                      "закрыта---------------------------\n-----------------------------\nИнформация о "
                      "смене\n-----------------------------\n")
                print("Количество заказов: ", self.order_count)
                print("Общая сумма за смену: ", self.sum)
                self.sum = 0
                self.orders.clear()
            else:
                pass
        else:
            self.error_message()

    def get_shift_report(self):
        if self.current_position == "Администратор":
            for key, value in self.orders.items():
                for i in value:
                    self.sum += float(i[2])
            print("Количество заказов: ", self.order_count)
            print("Общая сумма за смену: ", self.sum)
            self.sum = 0
        else:
            self.error_message()

    def switch_to_MainMenu(self):
        self.summ_label.setText(f"Общая сумма: ")
        self.result_list.clear()
        self.tabWidget.setCurrentIndex(1)

    def switch_to_StopList(self):
        self.tabWidget.setCurrentIndex(5)

    def switch_editTab_to_MainMenu(self):
        self.tabWidget.setCurrentIndex(1)
        self.tableWidget_edit.clearContents()
        self.tableWidget_edit.setRowCount(0)
        self.order_list.clear()
        self.quantityLineEdit.clear()
        self.searchLineEdit.clear()
        self.result_list_edit.clear()
        self.summ_label_edit.setText(f"Общая сумма: ")

    def switch_to_editOrder(self):
        self.tabWidget.setCurrentIndex(4)
        for key, value in self.orders.items():
            if value == []:
                pass
            else:
                item = QListWidgetItem(f"{key}: {value}")
                self.order_list.addItem(item)

    def switch_Employees_to_MainMenu(self):
        self.tabWidget.setCurrentIndex(1)
        self.tableWidget2.clearContents()
        self.tableWidget2.setRowCount(0)

    def switch_to_CreateOrder(self):
        self.tabWidget.setCurrentIndex(2)

    def input_autorization(self, num):
        username_length = len(self.username_input.text())
        if username_length == self.username_input.maxLength():
            self.password_input.insert(str(num))
        else:
            self.username_input.insert(str(num))

    def input_stop_quantity(self, num):
        self.quantityLine2.insert(str(num))

    def input_quantity(self, num):
        self.quantityLine.insert(str(num))

    def input_edit_quantity(self, num):
        self.quantityLineEdit.insert(str(num))

    def switch_to_Autorization(self):
        self.tabWidget.setCurrentIndex(0)
        self.clear_auto_input()
        self.error_label.setStyleSheet("backgroung-color: rgb(101, 112, 136);\n"
                                       "color: rgb(101, 112, 136);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")

    def clear_auto_input(self):
        self.password_input.clear()
        self.username_input.clear()

    def exit(self):
        msg_box = QMessageBox()
        msg_box.setText("Вы уверены, что выйти из программы?\nВсе данные будут удалены.")
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_box.exec_()

        if result == QMessageBox.Yes:
            exit()
        else:
            pass

    def auto_error(self):
        self.error_label.setStyleSheet("backgroung-color: rgb(255, 255, 255);\n"
                                       "color: rgb(255, 0, 0);\n"
                                       "font: 12pt \"MS Shell Dlg 2\";")

    def add_to_stop_table(self, item):
        row_count = self.tableWidget3.rowCount()
        self.tableWidget3.insertRow(row_count)
        if row_count < self.tableWidget3.rowCount():
            # Получает данные из базы данных
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM menu WHERE name = %s", (item.text(),))
            result = cursor.fetchone()
            name = result['name']
            cursor.close()

            # Записывает данные в таблицу
            self.tableWidget3.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget3.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(self.quantityLine2.text())))

    def show_order_to_edit(self, item):
        row = self.tableWidget_edit.rowCount()
        self.tableWidget_edit.insertRow(row)
        self.itemText = item.text()
        for key, values in self.orders.items():
            if f"{key}: {values}" == self.itemText:
                max_items = len(self.orders[key])
                self.tableWidget_edit.setRowCount(max_items)
                for value in values:
                    # Создаем QTableWidgetItem для каждого значения
                    item1 = QTableWidgetItem(value[0])
                    item2 = QTableWidgetItem(str(value[1]))
                    item3 = QTableWidgetItem(str(value[2]))

                    # Устанавливаем созданные QTableWidgetItem в соответствующие ячейки таблицы
                    self.tableWidget_edit.setItem(row, 0, item1)
                    self.tableWidget_edit.setItem(row, 1, item2)
                    self.tableWidget_edit.setItem(row, 2, item3)

                    row += 1
                for row in range(self.tableWidget_edit.rowCount() - 1, -1, -1):
                    empty = True
                    for column in range(self.tableWidget_edit.columnCount()):
                        item = self.tableWidget_edit.item(row, column)
                        if item is not None and item.text():
                            empty = False
                            break

                    if empty:
                        self.tableWidget_edit.removeRow(row)

        total_price = 0
        for rows in range(self.tableWidget_edit.rowCount()):
            item = self.tableWidget_edit.item(rows, 2)
            if item:
                total_price += float(item.text())
        self.summ_label_edit.setText(f"Общая сумма: {total_price}")

    def remove_row(self):
        selected_row = self.tableWidget_edit.currentRow()
        if selected_row != -1:
            msg_box = QMessageBox()
            msg_box.setText("Подтвердите удаление позиции в заказе")
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = msg_box.exec_()

            if result == QMessageBox.Yes:
                self.tableWidget_edit.removeRow(selected_row)
            else:
                pass
        else:
            error_message_box = QMessageBox()
            error_message_box.setIcon(QMessageBox.Critical)
            error_message_box.setWindowTitle("Ошибка")
            error_message_box.setText("Пожалуйста, выберите позицию в заказе.")
            error_message_box.exec_()

    def add_to_edit_table(self, item):
        row_count = self.tableWidget_edit.rowCount()
        self.tableWidget_edit.insertRow(row_count)
        if row_count < self.tableWidget_edit.rowCount() and bool(self.quantityLineEdit.text()) and row_count != 0:
            # Получает данные из базы данных
            cursor = self.conn.cursor()
            cursor.execute("SELECT name, price FROM menu WHERE name = %s", (item.text(),))
            result = cursor.fetchone()
            name = result['name']
            price = result['price']
            cursor.close()

            # Записывает данные в таблицу
            self.tableWidget_edit.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget_edit.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(self.quantityLineEdit.text())))
            self.tableWidget_edit.setItem(row_count, 2,
                                          QtWidgets.QTableWidgetItem(str(price * int(self.quantityLineEdit.text()))))

            total_price = 0
            for row in range(self.tableWidget_edit.rowCount()):
                item = self.tableWidget_edit.item(row, 2)
                if item:
                    total_price += float(item.text())
            self.summ_label_edit.setText(f"Общая сумма: {total_price}")
        else:
            if row_count == 0:
                self.tableWidget_edit.removeRow(row_count)
                error_message_box = QMessageBox()
                error_message_box.setIcon(QMessageBox.Critical)
                error_message_box.setWindowTitle("Ошибка")
                error_message_box.setText("Пожалуйста, выберите сначала заказ, который Вы хотите изменить.")
                error_message_box.exec_()
            else:
                self.tableWidget_edit.removeRow(row_count)
                error_message_box = QMessageBox()
                error_message_box.setIcon(QMessageBox.Critical)
                error_message_box.setWindowTitle("Ошибка")
                error_message_box.setText("Пожалуйста, введите количество.")
                error_message_box.exec_()

    def add_to_table(self, item):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        if row_count < self.tableWidget.rowCount() and bool(self.quantityLine.text()):
            # Получает данные из базы данных
            cursor = self.conn.cursor()
            cursor.execute("SELECT name, price FROM menu WHERE name = %s", (item.text(),))
            result = cursor.fetchone()
            name = result['name']
            price = result['price']
            cursor.close()

            # Записывает данные в таблицу
            self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(self.quantityLine.text())))
            self.tableWidget.setItem(row_count, 2,
                                     QtWidgets.QTableWidgetItem(str(price * int(self.quantityLine.text()))))
            total_price = 0
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 2)
                if item:
                    total_price += float(item.text())
            self.summ_label.setText(f"Общая сумма: {total_price}")
        else:
            self.tableWidget.removeRow(row_count)
            error_message_box = QMessageBox()
            error_message_box.setIcon(QMessageBox.Critical)
            error_message_box.setWindowTitle("Ошибка")
            error_message_box.setText("Пожалуйста, введите количество.")
            error_message_box.exec_()


def add_to_table(self, item):
    # Получает текущее количество строк в таблице
    row_count = self.tableWidget.rowCount()
    # Добавляет новую строку
    self.tableWidget.insertRow(row_count)

    # Получает данные из базы данных
    cursor = self.conn.cursor()
    cursor.execute("SELECT name, price FROM menu WHERE name = %s", (item[0],))
    result = cursor.fetchone()
    name = result[0]
    price = result[1]
    cursor.close()

    # Устанавливает значения в ячейки таблицы
    self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))
    self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(self.quantitySpinBox.value())))
    self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(price * self.quantitySpinBox.value())))


def add_to_edit_table(self, item):
    # Получает текущее количество строк в таблице
    row_count = self.tableWidget_edit.rowCount()
    # Добавляет новую строку
    self.tableWidget_edit.insertRow(row_count)

    # Получает данные из базы данных
    cursor = self.conn.cursor()
    cursor.execute("SELECT name, price FROM menu WHERE name = %s", (item[0],))
    result = cursor.fetchone()
    name = result[0]
    price = result[1]
    cursor.close()

    # Устанавливает значения в ячейки таблицы
    self.tableWidget_edit.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))
    self.tableWidget_edit.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(self.quantitySpinBox.value())))
    self.tableWidget_edit.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(price * self.quantitySpinBox.value())))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    conn.close()
