# Form implementation generated from reading ui file 'sha1.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SHA1(object):
    def setupUi(self, SHA1):
        SHA1.setObjectName("SHA1")
        SHA1.resize(545, 452)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(SHA1)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab_widget = QtWidgets.QTabWidget(SHA1)
        self.tab_widget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_text = QtWidgets.QWidget()
        self.tab_text.setObjectName("tab_text")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_text)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.group_box_input = QtWidgets.QGroupBox(self.tab_text)
        self.group_box_input.setObjectName("group_box_input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_box_input)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_edit_input = QtWidgets.QTextEdit(self.group_box_input)
        self.text_edit_input.setObjectName("text_edit_input")
        self.verticalLayout.addWidget(self.text_edit_input)
        self.horizontalLayout.addWidget(self.group_box_input)
        self.tab_widget.addTab(self.tab_text, "")
        self.tab_document = QtWidgets.QWidget()
        self.tab_document.setObjectName("tab_document")
        self.tab_widget.addTab(self.tab_document, "")
        self.verticalLayout_6.addWidget(self.tab_widget)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.group_box_result = QtWidgets.QGroupBox(SHA1)
        self.group_box_result.setMaximumSize(QtCore.QSize(300, 16777215))
        self.group_box_result.setObjectName("group_box_result")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_box_result)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_edit_result = QtWidgets.QLineEdit(self.group_box_result)
        self.line_edit_result.setReadOnly(True)
        self.line_edit_result.setObjectName("line_edit_result")
        self.verticalLayout_3.addWidget(self.line_edit_result)
        self.vertical_layout_2.addWidget(self.group_box_result)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vertical_layout_2.addItem(spacerItem)
        self.horizontal_layout_1.addLayout(self.vertical_layout_2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem1)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.button_make = QtWidgets.QPushButton(SHA1)
        self.button_make.setMinimumSize(QtCore.QSize(100, 30))
        self.button_make.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_make.setObjectName("button_make")
        self.horizontal_layout_2.addWidget(self.button_make)
        self.vertical_layout_1.addLayout(self.horizontal_layout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vertical_layout_1.addItem(spacerItem2)
        self.horizontal_layout_1.addLayout(self.vertical_layout_1)
        self.verticalLayout_6.addLayout(self.horizontal_layout_1)

        self.retranslateUi(SHA1)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SHA1)

    def retranslateUi(self, SHA1):
        _translate = QtCore.QCoreApplication.translate
        SHA1.setWindowTitle(_translate("SHA1", "Form"))
        self.group_box_input.setTitle(_translate("SHA1", "Input text"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_text), _translate("SHA1", "Text"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_document), _translate("SHA1", "Document"))
        self.group_box_result.setTitle(_translate("SHA1", "Result"))
        self.button_make.setText(_translate("SHA1", "Make"))
