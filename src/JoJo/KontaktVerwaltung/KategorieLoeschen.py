# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KategorieLoeschenDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Kategorie_loeschen(object):
    def setupUi(self, Kategorie_loeschen):
        if not Kategorie_loeschen.objectName():
            Kategorie_loeschen.setObjectName(u"Kategorie_loeschen")
        Kategorie_loeschen.resize(400, 300)
        self.KategorienComboBox = QComboBox(Kategorie_loeschen)
        self.KategorienComboBox.setObjectName(u"KategorienComboBox")
        self.KategorienComboBox.setGeometry(QRect(40, 80, 291, 22))
        self.label_2 = QLabel(Kategorie_loeschen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 301, 16))
        self.buttonBox = QDialogButtonBox(Kategorie_loeschen)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 230, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.LoeschenButton = QPushButton(Kategorie_loeschen)
        self.LoeschenButton.setObjectName(u"LoeschenButton")
        self.LoeschenButton.setGeometry(QRect(180, 230, 75, 24))

        self.retranslateUi(Kategorie_loeschen)

        QMetaObject.connectSlotsByName(Kategorie_loeschen)
    # setupUi

    def retranslateUi(self, Kategorie_loeschen):
        Kategorie_loeschen.setWindowTitle(QCoreApplication.translate("Kategorie_loeschen", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Kategorie_loeschen", u"Kategorie ausw\u00e4hlen:", None))
        self.LoeschenButton.setText(QCoreApplication.translate("Kategorie_loeschen", u"L\u00f6schen", None))
    # retranslateUi

