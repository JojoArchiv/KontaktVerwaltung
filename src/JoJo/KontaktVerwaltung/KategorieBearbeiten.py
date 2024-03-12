# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KategorieBearbeitenDialog.ui'
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
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Kategorie_bearbeiten(object):
    def setupUi(self, Kategorie_bearbeiten):
        if not Kategorie_bearbeiten.objectName():
            Kategorie_bearbeiten.setObjectName(u"Kategorie_bearbeiten")
        Kategorie_bearbeiten.resize(400, 300)
        self.SpeichernAbbrechen = QDialogButtonBox(Kategorie_bearbeiten)
        self.SpeichernAbbrechen.setObjectName(u"SpeichernAbbrechen")
        self.SpeichernAbbrechen.setGeometry(QRect(30, 240, 341, 32))
        self.SpeichernAbbrechen.setOrientation(Qt.Horizontal)
        self.SpeichernAbbrechen.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.SpeichernAbbrechen.setCenterButtons(False)
        self.KategorienComboBox = QComboBox(Kategorie_bearbeiten)
        self.KategorienComboBox.setObjectName(u"KategorienComboBox")
        self.KategorienComboBox.setGeometry(QRect(40, 80, 291, 22))
        self.label_2 = QLabel(Kategorie_bearbeiten)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 301, 16))
        self.lineEdit = QLineEdit(Kategorie_bearbeiten)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 150, 291, 21))
        self.label_3 = QLabel(Kategorie_bearbeiten)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 301, 16))

        self.retranslateUi(Kategorie_bearbeiten)
        self.SpeichernAbbrechen.accepted.connect(Kategorie_bearbeiten.accept)
        self.SpeichernAbbrechen.rejected.connect(Kategorie_bearbeiten.reject)

        QMetaObject.connectSlotsByName(Kategorie_bearbeiten)
    # setupUi

    def retranslateUi(self, Kategorie_bearbeiten):
        Kategorie_bearbeiten.setWindowTitle(QCoreApplication.translate("Kategorie_bearbeiten", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.SpeichernAbbrechen.setToolTip(QCoreApplication.translate("Kategorie_bearbeiten", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.SpeichernAbbrechen.setWhatsThis(QCoreApplication.translate("Kategorie_bearbeiten", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Kategorie_bearbeiten", u"Kategorie ausw\u00e4hlen:", None))
        self.label_3.setText(QCoreApplication.translate("Kategorie_bearbeiten", u"Neuer Name:", None))
    # retranslateUi

