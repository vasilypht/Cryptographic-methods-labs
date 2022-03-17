# Form implementation generated from reading ui file 'cardan_grille.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cardan_grille(object):
    def setupUi(self, cardan_grille):
        cardan_grille.setObjectName("cardan_grille")
        cardan_grille.resize(600, 412)
        self.verticalLayout = QtWidgets.QVBoxLayout(cardan_grille)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.group_box_stencil = QtWidgets.QGroupBox(cardan_grille)
        self.group_box_stencil.setObjectName("group_box_stencil")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.group_box_stencil)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.table_widget_stencil = QtWidgets.QTableWidget(self.group_box_stencil)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget_stencil.sizePolicy().hasHeightForWidth())
        self.table_widget_stencil.setSizePolicy(sizePolicy)
        self.table_widget_stencil.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.table_widget_stencil.setStyleSheet("")
        self.table_widget_stencil.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_widget_stencil.setAlternatingRowColors(True)
        self.table_widget_stencil.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.table_widget_stencil.setObjectName("table_widget_stencil")
        self.table_widget_stencil.setColumnCount(0)
        self.table_widget_stencil.setRowCount(0)
        self.table_widget_stencil.horizontalHeader().setVisible(True)
        self.table_widget_stencil.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget_stencil.horizontalHeader().setStretchLastSection(False)
        self.table_widget_stencil.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget_stencil.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_21.addWidget(self.table_widget_stencil)
        self.horizontal_layout_1.addWidget(self.group_box_stencil)
        self.group_box_input = QtWidgets.QGroupBox(cardan_grille)
        self.group_box_input.setObjectName("group_box_input")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.group_box_input)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.text_edit_input = QtWidgets.QTextEdit(self.group_box_input)
        self.text_edit_input.setStyleSheet("")
        self.text_edit_input.setObjectName("text_edit_input")
        self.verticalLayout_22.addWidget(self.text_edit_input)
        self.horizontal_layout_1.addWidget(self.group_box_input)
        self.verticalLayout.addLayout(self.horizontal_layout_1)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setContentsMargins(8, 0, -1, -1)
        self.horizontal_layout_2.setSpacing(12)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.button_gen_stencil = QtWidgets.QPushButton(cardan_grille)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_gen_stencil.sizePolicy().hasHeightForWidth())
        self.button_gen_stencil.setSizePolicy(sizePolicy)
        self.button_gen_stencil.setMinimumSize(QtCore.QSize(100, 30))
        self.button_gen_stencil.setObjectName("button_gen_stencil")
        self.horizontal_layout_2.addWidget(self.button_gen_stencil)
        self.button_clean_stencil = QtWidgets.QPushButton(cardan_grille)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clean_stencil.sizePolicy().hasHeightForWidth())
        self.button_clean_stencil.setSizePolicy(sizePolicy)
        self.button_clean_stencil.setMinimumSize(QtCore.QSize(100, 30))
        self.button_clean_stencil.setObjectName("button_clean_stencil")
        self.horizontal_layout_2.addWidget(self.button_clean_stencil)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_2.addItem(spacerItem)
        self.combo_box_trash = QtWidgets.QComboBox(cardan_grille)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_box_trash.sizePolicy().hasHeightForWidth())
        self.combo_box_trash.setSizePolicy(sizePolicy)
        self.combo_box_trash.setObjectName("combo_box_trash")
        self.combo_box_trash.addItem("")
        self.combo_box_trash.addItem("")
        self.horizontal_layout_2.addWidget(self.combo_box_trash)
        self.combo_box_mode = QtWidgets.QComboBox(cardan_grille)
        self.combo_box_mode.setObjectName("combo_box_mode")
        self.combo_box_mode.addItem("")
        self.combo_box_mode.addItem("")
        self.horizontal_layout_2.addWidget(self.combo_box_mode)
        self.verticalLayout.addLayout(self.horizontal_layout_2)
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setContentsMargins(8, -1, -1, -1)
        self.horizontal_layout_3.setSpacing(12)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.label_dim_stencil = QtWidgets.QLabel(cardan_grille)
        self.label_dim_stencil.setObjectName("label_dim_stencil")
        self.horizontal_layout_3.addWidget(self.label_dim_stencil)
        self.spin_box_dim_stencil = QtWidgets.QSpinBox(cardan_grille)
        self.spin_box_dim_stencil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spin_box_dim_stencil.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box_dim_stencil.setMinimum(2)
        self.spin_box_dim_stencil.setMaximum(100)
        self.spin_box_dim_stencil.setObjectName("spin_box_dim_stencil")
        self.horizontal_layout_3.addWidget(self.spin_box_dim_stencil)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_3.addItem(spacerItem1)
        self.button_make = QtWidgets.QPushButton(cardan_grille)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_make.sizePolicy().hasHeightForWidth())
        self.button_make.setSizePolicy(sizePolicy)
        self.button_make.setMinimumSize(QtCore.QSize(100, 30))
        self.button_make.setObjectName("button_make")
        self.horizontal_layout_3.addWidget(self.button_make)
        self.verticalLayout.addLayout(self.horizontal_layout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.group_box_preview = QtWidgets.QGroupBox(cardan_grille)
        self.group_box_preview.setObjectName("group_box_preview")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.group_box_preview)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.table_widget_preview = QtWidgets.QTableWidget(self.group_box_preview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget_preview.sizePolicy().hasHeightForWidth())
        self.table_widget_preview.setSizePolicy(sizePolicy)
        self.table_widget_preview.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_widget_preview.setAlternatingRowColors(True)
        self.table_widget_preview.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.table_widget_preview.setObjectName("table_widget_preview")
        self.table_widget_preview.setColumnCount(0)
        self.table_widget_preview.setRowCount(0)
        self.table_widget_preview.horizontalHeader().setVisible(True)
        self.table_widget_preview.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget_preview.horizontalHeader().setStretchLastSection(False)
        self.table_widget_preview.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget_preview.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_25.addWidget(self.table_widget_preview)
        self.horizontalLayout_4.addWidget(self.group_box_preview)
        self.group_box_output = QtWidgets.QGroupBox(cardan_grille)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_box_output.sizePolicy().hasHeightForWidth())
        self.group_box_output.setSizePolicy(sizePolicy)
        self.group_box_output.setObjectName("group_box_output")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.group_box_output)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.text_edit_output = QtWidgets.QTextEdit(self.group_box_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit_output.sizePolicy().hasHeightForWidth())
        self.text_edit_output.setSizePolicy(sizePolicy)
        self.text_edit_output.setReadOnly(True)
        self.text_edit_output.setObjectName("text_edit_output")
        self.verticalLayout_24.addWidget(self.text_edit_output)
        self.horizontalLayout_4.addWidget(self.group_box_output)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(cardan_grille)
        QtCore.QMetaObject.connectSlotsByName(cardan_grille)

    def retranslateUi(self, cardan_grille):
        _translate = QtCore.QCoreApplication.translate
        cardan_grille.setWindowTitle(_translate("cardan_grille", "Form"))
        self.group_box_stencil.setTitle(_translate("cardan_grille", "Stencil"))
        self.group_box_input.setTitle(_translate("cardan_grille", "Input text"))
        self.button_gen_stencil.setText(_translate("cardan_grille", "Generate Stencil"))
        self.button_clean_stencil.setText(_translate("cardan_grille", "Clean stencil"))
        self.combo_box_trash.setItemText(0, _translate("cardan_grille", "With trash"))
        self.combo_box_trash.setItemText(1, _translate("cardan_grille", "Without trash"))
        self.combo_box_mode.setItemText(0, _translate("cardan_grille", "Encrypt"))
        self.combo_box_mode.setItemText(1, _translate("cardan_grille", "Decrypt"))
        self.label_dim_stencil.setText(_translate("cardan_grille", "Dimension of the small lattice:"))
        self.button_make.setText(_translate("cardan_grille", "Make"))
        self.group_box_preview.setTitle(_translate("cardan_grille", "Preview"))
        self.group_box_output.setTitle(_translate("cardan_grille", "Output text"))
