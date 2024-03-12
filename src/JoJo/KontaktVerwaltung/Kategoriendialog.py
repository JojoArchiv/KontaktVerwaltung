# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kategoriedialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_KategorieAnlegenDialog(object):
    def setupUi(self, KategorieAnlegenDialog):
        if not KategorieAnlegenDialog.objectName():
            KategorieAnlegenDialog.setObjectName(u"KategorieAnlegenDialog")
        KategorieAnlegenDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(KategorieAnlegenDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(KategorieAnlegenDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 301, 16))
        self.lineEdit = QLineEdit(KategorieAnlegenDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 80, 331, 21))

        self.retranslateUi(KategorieAnlegenDialog)
        self.buttonBox.accepted.connect(KategorieAnlegenDialog.accept)
        self.buttonBox.rejected.connect(KategorieAnlegenDialog.reject)

        QMetaObject.connectSlotsByName(KategorieAnlegenDialog)
    # setupUi

    def retranslateUi(self, KategorieAnlegenDialog):
        KategorieAnlegenDialog.setWindowTitle(QCoreApplication.translate("KategorieAnlegenDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("KategorieAnlegenDialog", u"Bitte neuen Kategoriennamen eingeben:", None))
    # retranslateUi

