# Form implementation generated from reading ui file 'selected_file_widget.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SelectedFileWidget(object):
    def setupUi(self, SelectedFileWidget):
        SelectedFileWidget.setObjectName("SelectedFileWidget")
        SelectedFileWidget.resize(709, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectedFileWidget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_center = QtWidgets.QHBoxLayout()
        self.horizontal_layout_center.setObjectName("horizontal_layout_center")
        self.frame = QtWidgets.QFrame(SelectedFileWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icon = QtWidgets.QLabel(self.frame)
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout.addWidget(self.label_icon)
        self.label_file = QtWidgets.QLabel(self.frame)
        self.label_file.setObjectName("label_file")
        self.horizontalLayout.addWidget(self.label_file)
        spacerItem = QtWidgets.QSpacerItem(250, 17, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_close = QtWidgets.QPushButton(self.frame)
        self.button_close.setMinimumSize(QtCore.QSize(100, 30))
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.horizontal_layout_center.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontal_layout_center)

        self.retranslateUi(SelectedFileWidget)
        QtCore.QMetaObject.connectSlotsByName(SelectedFileWidget)

    def retranslateUi(self, SelectedFileWidget):
        _translate = QtCore.QCoreApplication.translate
        SelectedFileWidget.setWindowTitle(_translate("SelectedFileWidget", "Form"))
        self.label_file.setText(_translate("SelectedFileWidget", "file path"))
        self.button_close.setText(_translate("SelectedFileWidget", "Close"))
