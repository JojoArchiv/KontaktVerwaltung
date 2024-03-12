# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KategorieAuswaehlenDialog.ui'
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
    QDialogButtonBox, QLabel, QSizePolicy, QWidget)

class Ui_KategorieAuswaehlen(object):
    def setupUi(self, KategorieAuswaehlen):
        if not KategorieAuswaehlen.objectName():
            KategorieAuswaehlen.setObjectName(u"KategorieAuswaehlen")
        KategorieAuswaehlen.resize(399, 162)
        self.CancelOK = QDialogButtonBox(KategorieAuswaehlen)
        self.CancelOK.setObjectName(u"CancelOK")
        self.CancelOK.setGeometry(QRect(30, 100, 341, 32))
        self.CancelOK.setOrientation(Qt.Horizontal)
        self.CancelOK.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.KategorieComboBox = QComboBox(KategorieAuswaehlen)
        self.KategorieComboBox.setObjectName(u"KategorieComboBox")
        self.KategorieComboBox.setGeometry(QRect(30, 50, 341, 26))
        self.AuswahlLabel = QLabel(KategorieAuswaehlen)
        self.AuswahlLabel.setObjectName(u"AuswahlLabel")
        self.AuswahlLabel.setGeometry(QRect(30, 20, 341, 18))

        self.retranslateUi(KategorieAuswaehlen)
        self.CancelOK.accepted.connect(KategorieAuswaehlen.accept)
        self.CancelOK.rejected.connect(KategorieAuswaehlen.reject)

        QMetaObject.connectSlotsByName(KategorieAuswaehlen)
    # setupUi

    def retranslateUi(self, KategorieAuswaehlen):
        KategorieAuswaehlen.setWindowTitle(QCoreApplication.translate("KategorieAuswaehlen", u"Dialog", None))
        self.AuswahlLabel.setText(QCoreApplication.translate("KategorieAuswaehlen", u"Kategorie ausw\u00e4hlen:", None))
    # retranslateUi

