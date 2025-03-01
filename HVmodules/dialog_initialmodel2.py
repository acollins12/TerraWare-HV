# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_initialmodel2.ui',
# licensing of 'dialog_initialmodel2.ui' applies.
#
# Created: Fri Dec 13 12:19:04 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_ModeloInicial(object):
    def setupUi(self, ModeloInicial):
        ModeloInicial.setObjectName("ModeloInicial")
        ModeloInicial.resize(300, 377)
        font = QtGui.QFont("MS Shell Dlg 2", 10.5)
        self.widget = QtWidgets.QWidget(ModeloInicial)
        self.widget.setFont(font)
        self.widget.setGeometry(QtCore.QRect(10, 10, 279, 284))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_pmin = QtWidgets.QLabel(self.widget)
        self.label_pmin.setObjectName("label_pmin")
        self.gridLayout.addWidget(self.label_pmin, 3, 0, 1, 1)
        self.label_ncapas = QtWidgets.QLabel(self.widget)
        self.label_ncapas.setObjectName("label_ncapas")
        self.gridLayout.addWidget(self.label_ncapas, 1, 0, 1, 1)
        self.label_smax = QtWidgets.QLabel(self.widget)
        self.label_smax.setObjectName("label_smax")
        self.gridLayout.addWidget(self.label_smax, 6, 0, 1, 1)
        self.doubleSpinBox_smax = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_smax.setDecimals(3)
        self.doubleSpinBox_smax.setMaximum(4000.0)
        self.doubleSpinBox_smax.setObjectName("doubleSpinBox_smax")
        self.gridLayout.addWidget(self.doubleSpinBox_smax, 6, 1, 1, 1)
        self.label_dmin = QtWidgets.QLabel(self.widget)
        self.label_dmin.setObjectName("label_dmin")
        self.gridLayout.addWidget(self.label_dmin, 7, 0, 1, 1)
        self.label_pmax = QtWidgets.QLabel(self.widget)
        self.label_pmax.setObjectName("label_pmax")
        self.gridLayout.addWidget(self.label_pmax, 4, 0, 1, 1)
        self.doubleSpinBox_dmin = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_dmin.setDecimals(3)
        self.doubleSpinBox_dmin.setMinimum(1000.0)
        self.doubleSpinBox_dmin.setMaximum(3500.0)
        self.doubleSpinBox_dmin.setObjectName("doubleSpinBox_dmin")
        self.gridLayout.addWidget(self.doubleSpinBox_dmin, 7, 1, 1, 1)
        self.label_dmax = QtWidgets.QLabel(self.widget)
        self.label_dmax.setObjectName("label_dmax")
        self.gridLayout.addWidget(self.label_dmax, 8, 0, 1, 1)
        self.checkBox_bsm = QtWidgets.QCheckBox()
        self.checkBox_bsm.setObjectName("checkBox_bsm")
        self.gridLayout.addWidget(self.checkBox_bsm, 9, 0, 1, 1)

        self.doubleSpinBox_dmax = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_dmax.setDecimals(3)
        self.doubleSpinBox_dmax.setMinimum(1000.0)
        self.doubleSpinBox_dmax.setMaximum(3500.0)
        self.doubleSpinBox_dmax.setObjectName("doubleSpinBox_dmax")
        self.gridLayout.addWidget(self.doubleSpinBox_dmax, 8, 1, 1, 1)
        self.doubleSpinBox_pmax = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_pmax.setDecimals(3)
        self.doubleSpinBox_pmax.setMaximum(0.5)
        self.doubleSpinBox_pmax.setObjectName("doubleSpinBox_pmax")
        self.gridLayout.addWidget(self.doubleSpinBox_pmax, 4, 1, 1, 1)
        self.spinBox_ncapas = QtWidgets.QSpinBox(self.widget)
        self.spinBox_ncapas.setMinimum(2)
        self.spinBox_ncapas.setObjectName("spinBox_ncapas")
        self.gridLayout.addWidget(self.spinBox_ncapas, 1, 1, 1, 1)
        self.doubleSpinBox_prof = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_prof.setDecimals(3)
        self.doubleSpinBox_prof.setMinimum(10.0)
        self.doubleSpinBox_prof.setMaximum(3000.0)
        self.doubleSpinBox_prof.setProperty("value", 10.0)
        self.doubleSpinBox_prof.setObjectName("doubleSpinBox_prof")
        self.gridLayout.addWidget(self.doubleSpinBox_prof, 2, 1, 1, 1)
        self.doubleSpinBox_smin = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_smin.setDecimals(3)
        self.doubleSpinBox_smin.setMaximum(4000.0)
        self.doubleSpinBox_smin.setObjectName("doubleSpinBox_smin")
        self.gridLayout.addWidget(self.doubleSpinBox_smin, 5, 1, 1, 1)
        self.doubleSpinBox_pmin = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_pmin.setDecimals(3)
        self.doubleSpinBox_pmin.setMaximum(0.5)
        self.doubleSpinBox_pmin.setObjectName("doubleSpinBox_pmin")
        self.gridLayout.addWidget(self.doubleSpinBox_pmin, 3, 1, 1, 1)
        self.label_prof = QtWidgets.QLabel(self.widget)
        self.label_prof.setObjectName("label_prof")
        self.gridLayout.addWidget(self.label_prof, 2, 0, 1, 1)
        self.label_smin = QtWidgets.QLabel(self.widget)
        self.label_smin.setObjectName("label_smin")
        self.gridLayout.addWidget(self.label_smin, 5, 0, 1, 1)
        self.label_firstthick = QtWidgets.QLabel(self.widget)
        self.label_firstthick.setObjectName("label_firstthick")
        self.gridLayout.addWidget(self.label_firstthick, 0, 0, 1, 1)
        self.doubleSpinBox_firstthick = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_firstthick.setObjectName("doubleSpinBox_firstthick")
        self.gridLayout.addWidget(self.doubleSpinBox_firstthick, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(ModeloInicial)
        self.widget1.setGeometry(QtCore.QRect(60, 310, 230, 58))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_loadmodel = QtWidgets.QPushButton(self.widget1)
        self.pushButton_loadmodel.setObjectName("pushButton_loadmodel")
        self.gridLayout_3.addWidget(self.pushButton_loadmodel, 0, 0, 1, 1)
        self.pushButton_info = QtWidgets.QPushButton(self.widget1)
        self.pushButton_info.setObjectName("pushButton_info")
        self.gridLayout_3.addWidget(self.pushButton_info, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(ModeloInicial)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ModeloInicial.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ModeloInicial.reject)
        QtCore.QMetaObject.connectSlotsByName(ModeloInicial)
        self.default()

    def default(self):
        self.doubleSpinBox_pmin.setValue(0.33)
        self.doubleSpinBox_pmax.setValue(0.45)
        self.doubleSpinBox_smin.setValue(125.0)
        self.doubleSpinBox_smax.setValue(400.0)
        self.doubleSpinBox_dmin.setValue(1000.0)
        self.doubleSpinBox_dmax.setValue(3000.0)
        self.spinBox_ncapas.setValue(16)
        self.doubleSpinBox_prof.setValue(100.0)
        self.doubleSpinBox_firstthick.setValue(2.0)
        self.checkBox_bsm.setChecked(1)



    def retranslateUi(self, ModeloInicial):
        ModeloInicial.setWindowTitle(QtWidgets.QApplication.translate("ModeloInicial", "Initial model", None, -1))
        self.label_pmin.setText(QtWidgets.QApplication.translate("ModeloInicial", "Poisson's ratio min", None, -1))
        self.label_ncapas.setText(QtWidgets.QApplication.translate("ModeloInicial", "Number of layers:", None, -1))
        self.label_smax.setText(QtWidgets.QApplication.translate("ModeloInicial", "S velocity max (m/s)", None, -1))
        self.label_dmin.setText(QtWidgets.QApplication.translate("ModeloInicial", "Density min (kg/m3)", None, -1))
        self.label_pmax.setText(QtWidgets.QApplication.translate("ModeloInicial", "Poisson's ratio max", None, -1))
        self.label_dmax.setText(QtWidgets.QApplication.translate("ModeloInicial", "Density max (kg/m3)", None, -1))
        self.label_prof.setText(QtWidgets.QApplication.translate("ModeloInicial", "Depth (m):", None, -1))
        self.label_smin.setText(QtWidgets.QApplication.translate("ModeloInicial", "S velocity min (m/s)", None, -1))
        self.label_firstthick.setText(QtWidgets.QApplication.translate("ModeloInicial", "First layer thickness:", None, -1))
        self.pushButton_loadmodel.setText(QtWidgets.QApplication.translate("ModeloInicial", "Load another model", None, -1))
        self.checkBox_bsm.setText(QtWidgets.QApplication.translate("ModeloInicial", "Basement", None, -1))
        self.pushButton_info.setText(QtWidgets.QApplication.translate("ModeloInicial", "Info", None, -1))
