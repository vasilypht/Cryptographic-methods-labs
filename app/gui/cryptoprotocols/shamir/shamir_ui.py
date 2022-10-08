# Form implementation generated from reading ui file 'shamir.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Shamir(object):
    def setupUi(self, Shamir):
        Shamir.setObjectName("Shamir")
        Shamir.resize(660, 365)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Shamir)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.group_box_options = QtWidgets.QGroupBox(Shamir)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_box_options.sizePolicy().hasHeightForWidth())
        self.group_box_options.setSizePolicy(sizePolicy)
        self.group_box_options.setMaximumSize(QtCore.QSize(400, 16777215))
        self.group_box_options.setObjectName("group_box_options")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.group_box_options)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.form_layout_options = QtWidgets.QFormLayout()
        self.form_layout_options.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.form_layout_options.setContentsMargins(4, -1, 4, -1)
        self.form_layout_options.setObjectName("form_layout_options")
        self.label_key_size = QtWidgets.QLabel(self.group_box_options)
        self.label_key_size.setObjectName("label_key_size")
        self.form_layout_options.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_key_size)
        self.spin_box_key_size = QtWidgets.QSpinBox(self.group_box_options)
        self.spin_box_key_size.setMinimum(50)
        self.spin_box_key_size.setMaximum(10000)
        self.spin_box_key_size.setProperty("value", 1024)
        self.spin_box_key_size.setDisplayIntegerBase(10)
        self.spin_box_key_size.setObjectName("spin_box_key_size")
        self.form_layout_options.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spin_box_key_size)
        self.label_public_key_p = QtWidgets.QLabel(self.group_box_options)
        self.label_public_key_p.setObjectName("label_public_key_p")
        self.form_layout_options.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_public_key_p)
        self.line_edit_public_key_p = QtWidgets.QLineEdit(self.group_box_options)
        self.line_edit_public_key_p.setObjectName("line_edit_public_key_p")
        self.form_layout_options.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_public_key_p)
        self.label_alice = QtWidgets.QLabel(self.group_box_options)
        self.label_alice.setObjectName("label_alice")
        self.form_layout_options.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_alice)
        self.label_alice_public_key = QtWidgets.QLabel(self.group_box_options)
        self.label_alice_public_key.setObjectName("label_alice_public_key")
        self.form_layout_options.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_alice_public_key)
        self.line_edit_alice_public_key = QtWidgets.QLineEdit(self.group_box_options)
        self.line_edit_alice_public_key.setObjectName("line_edit_alice_public_key")
        self.form_layout_options.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_alice_public_key)
        self.label_alice_private_key = QtWidgets.QLabel(self.group_box_options)
        self.label_alice_private_key.setObjectName("label_alice_private_key")
        self.form_layout_options.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_alice_private_key)
        self.line_edit_alice_private_key = QtWidgets.QLineEdit(self.group_box_options)
        self.line_edit_alice_private_key.setObjectName("line_edit_alice_private_key")
        self.form_layout_options.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_alice_private_key)
        self.label_bob = QtWidgets.QLabel(self.group_box_options)
        self.label_bob.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_bob.setObjectName("label_bob")
        self.form_layout_options.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_bob)
        self.label_bob_public_key = QtWidgets.QLabel(self.group_box_options)
        self.label_bob_public_key.setObjectName("label_bob_public_key")
        self.form_layout_options.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_bob_public_key)
        self.label_bob_private_key = QtWidgets.QLabel(self.group_box_options)
        self.label_bob_private_key.setObjectName("label_bob_private_key")
        self.form_layout_options.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_bob_private_key)
        self.line_edit_bob_private_key = QtWidgets.QLineEdit(self.group_box_options)
        self.line_edit_bob_private_key.setObjectName("line_edit_bob_private_key")
        self.form_layout_options.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_bob_private_key)
        self.line_edit_bob_public_key = QtWidgets.QLineEdit(self.group_box_options)
        self.line_edit_bob_public_key.setObjectName("line_edit_bob_public_key")
        self.form_layout_options.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_bob_public_key)
        self.verticalLayout_2.addLayout(self.form_layout_options)
        self.vertical_layout_3.addWidget(self.group_box_options)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vertical_layout_3.addItem(spacerItem)
        self.horizontal_layout_2.addLayout(self.vertical_layout_3)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.group_box_stats = QtWidgets.QGroupBox(Shamir)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_box_stats.sizePolicy().hasHeightForWidth())
        self.group_box_stats.setSizePolicy(sizePolicy)
        self.group_box_stats.setMinimumSize(QtCore.QSize(0, 0))
        self.group_box_stats.setMaximumSize(QtCore.QSize(16777215, 800))
        self.group_box_stats.setObjectName("group_box_stats")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_box_stats)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_edit_stats = QtWidgets.QTextEdit(self.group_box_stats)
        self.text_edit_stats.setObjectName("text_edit_stats")
        self.verticalLayout.addWidget(self.text_edit_stats)
        self.vertical_layout_2.addWidget(self.group_box_stats)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vertical_layout_2.addItem(spacerItem1)
        self.horizontal_layout_2.addLayout(self.vertical_layout_2)
        self.verticalLayout_6.addLayout(self.horizontal_layout_2)
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_1.addItem(spacerItem2)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setSpacing(10)
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setSpacing(10)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.button_make = QtWidgets.QPushButton(Shamir)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_make.sizePolicy().hasHeightForWidth())
        self.button_make.setSizePolicy(sizePolicy)
        self.button_make.setMinimumSize(QtCore.QSize(100, 30))
        self.button_make.setObjectName("button_make")
        self.horizontal_layout_3.addWidget(self.button_make)
        self.button_options = QtWidgets.QPushButton(Shamir)
        self.button_options.setMinimumSize(QtCore.QSize(30, 30))
        self.button_options.setText("")
        self.button_options.setObjectName("button_options")
        self.horizontal_layout_3.addWidget(self.button_options)
        self.vertical_layout_1.addLayout(self.horizontal_layout_3)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vertical_layout_1.addItem(spacerItem3)
        self.horizontal_layout_1.addLayout(self.vertical_layout_1)
        self.verticalLayout_6.addLayout(self.horizontal_layout_1)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_6.addItem(spacerItem4)

        self.retranslateUi(Shamir)
        QtCore.QMetaObject.connectSlotsByName(Shamir)

    def retranslateUi(self, Shamir):
        _translate = QtCore.QCoreApplication.translate
        Shamir.setWindowTitle(_translate("Shamir", "Form"))
        self.group_box_options.setTitle(_translate("Shamir", "Options"))
        self.label_key_size.setText(_translate("Shamir", "Key size (bits):"))
        self.label_public_key_p.setText(_translate("Shamir", "Public key p:"))
        self.label_alice.setText(_translate("Shamir", " - Alice - "))
        self.label_alice_public_key.setText(_translate("Shamir", "Public key:"))
        self.label_alice_private_key.setText(_translate("Shamir", "Private key:"))
        self.label_bob.setText(_translate("Shamir", " - Bob - "))
        self.label_bob_public_key.setText(_translate("Shamir", "Public key:"))
        self.label_bob_private_key.setText(_translate("Shamir", "Private key:"))
        self.group_box_stats.setTitle(_translate("Shamir", "Statistics"))
        self.button_make.setText(_translate("Shamir", "Make"))
