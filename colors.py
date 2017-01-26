# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui

from colorsUI import Ui_Dialog
''' Importa interfície gràfica '''

import conversors
''' Importa llibreria conversions '''


class Colors(QDialog, Ui_Dialog):
    # Atributs de la classe (privats)
    __red = 255
    __green = 255
    __blue = 255
    __Hred = 'FF'
    __Hgreen = 'FF'
    __Hblue = 'FF'

    def __init__(self):
        # Constructor de la classe
        super(Colors, self).__init__()
        # Constructor de la classe pare
        self.setupUi(self)

    def recalcula(self):
        self.__red = self.horizontalSlider.value()
        self.__green = self.horizontalSlider_2.value()
        self.__blue = self.horizontalSlider_3.value()
        self.__Hred = conversors.decToHex(self.horizontalSlider.value())
        self.__Hgreen = conversors.decToHex(self.horizontalSlider_2.value())
        self.__Hblue = conversors.decToHex(self.horizontalSlider_3.value())

        self.lineEdit.setText('#' + self.__Hred + self.__Hgreen + self.__Hblue)
        self.label.setStyleSheet('background-color: rgb(' + str(self.__red) + ',' +
            str(self.__green) + ',' + str(self.__blue) +'); border-radius: 10px; border: 1px solid #AAAA7F;')
        self.label_6.setText(str(self.__red))
        self.label_7.setText(str(self.__green))
        self.label_8.setText(str(self.__blue))

    def mostraPaleta(self):
        """ Crida al dialeg de color amb el color actual """
        auxcolor = QtGui.QColor()       # crea objecte color
        auxcolor.setRgb(self.__red, self.__green, self.__blue, 255)     # afegeix color actual
        color = QtGui.QColorDialog.getColor(auxcolor, self)
        self.getPaleta(color)

    def getPaleta(self, color):
        """ Actualitza els sliders """
        if color.isValid():
            self.horizontalSlider.setValue(color.red())
            self.horizontalSlider_2.setValue(color.green())
            self.horizontalSlider_3.setValue(color.blue())
            self.recalcula()

    def sortir(self):
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    finestra = Colors()
    finestra.show()
    sys.exit(app.exec_())

