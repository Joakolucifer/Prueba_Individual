from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_VentanaSecundaria(object):
    def setupUi(self, VentanaSecundaria):
        VentanaSecundaria.setObjectName("VentanaSecundaria")
        VentanaSecundaria.resize(688,311)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=VentanaSecundaria)
        self.verticalLayout.setGeometry(QtCore.QRect(0, 0, 661, 311))
        self.verticalLayout.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        

    def retranslateUi(self, VentanaSecundaria):
        _translate = QtCore.QCoreApplication.translate
        VentanaSecundaria.setWindowTitle(_translate("VentanaSecundaria", "VentanaSecundaria"))
        self.label.setText(_translate("VentanaSecundaria", "Datos Guardados"))
        self.pushButton.setText(_translate("VentanaSecundaria", "Guardar Mascota"))
        