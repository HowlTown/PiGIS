# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chenhaoliang/chl/大学课程作业等/大三下/GIS设计与应用/work1/PiGIS/ui/raw/_fieldTable.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FieldTable(object):
    def setupUi(self, FieldTable):
        FieldTable.setObjectName("FieldTable")
        FieldTable.resize(403, 300)
        self.gridLayout = QtWidgets.QGridLayout(FieldTable)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(FieldTable)
        self.widget.setMinimumSize(QtCore.QSize(0, 25))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addFieldButton = QtWidgets.QToolButton(self.widget)
        self.addFieldButton.setObjectName("addFieldButton")
        self.horizontalLayout_2.addWidget(self.addFieldButton)
        self.deleteFieldButton = QtWidgets.QToolButton(self.widget)
        self.deleteFieldButton.setObjectName("deleteFieldButton")
        self.horizontalLayout_2.addWidget(self.deleteFieldButton)
        self.saveButton = QtWidgets.QToolButton(self.widget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.toggleEditingCheckBox = QtWidgets.QCheckBox(self.widget)
        self.toggleEditingCheckBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toggleEditingCheckBox.setObjectName("toggleEditingCheckBox")
        self.horizontalLayout_2.addWidget(self.toggleEditingCheckBox)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.dataTable = QtWidgets.QTableWidget(FieldTable)
        self.dataTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(5)
        self.dataTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(2, 2, item)
        self.gridLayout.addWidget(self.dataTable, 1, 0, 1, 1)

        self.retranslateUi(FieldTable)
        self.addFieldButton.clicked.connect(FieldTable.add_field)
        self.deleteFieldButton.clicked.connect(FieldTable.delete_field)
        self.toggleEditingCheckBox.stateChanged['int'].connect(FieldTable.toggle_editing_changed)
        self.saveButton.clicked.connect(FieldTable.save)
        QtCore.QMetaObject.connectSlotsByName(FieldTable)

    def retranslateUi(self, FieldTable):
        _translate = QtCore.QCoreApplication.translate
        FieldTable.setWindowTitle(_translate("FieldTable", "Form"))
        self.addFieldButton.setText(_translate("FieldTable", "Add Field"))
        self.deleteFieldButton.setText(_translate("FieldTable", "Delete Field"))
        self.saveButton.setText(_translate("FieldTable", "Save"))
        self.toggleEditingCheckBox.setText(_translate("FieldTable", "Togle Editing"))
        item = self.dataTable.verticalHeaderItem(0)
        item.setText(_translate("FieldTable", "1"))
        item = self.dataTable.verticalHeaderItem(1)
        item.setText(_translate("FieldTable", "2"))
        item = self.dataTable.verticalHeaderItem(2)
        item.setText(_translate("FieldTable", "3"))
        item = self.dataTable.verticalHeaderItem(3)
        item.setText(_translate("FieldTable", "4"))
        item = self.dataTable.verticalHeaderItem(4)
        item.setText(_translate("FieldTable", "5"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("FieldTable", "列1"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("FieldTable", "新建列"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("FieldTable", "列2"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("FieldTable", "3"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("FieldTable", "test5"))
        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        item = self.dataTable.item(1, 1)
        item.setText(_translate("FieldTable", "test1"))
        item = self.dataTable.item(2, 2)
        item.setText(_translate("FieldTable", "test2"))
        self.dataTable.setSortingEnabled(__sortingEnabled)
