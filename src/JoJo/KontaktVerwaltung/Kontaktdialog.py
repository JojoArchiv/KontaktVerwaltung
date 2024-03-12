# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Kontaktdialog.ui'
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
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_KontaktDialog(object):
    def setupUi(self, KontaktDialog):
        if not KontaktDialog.objectName():
            KontaktDialog.setObjectName(u"KontaktDialog")
        KontaktDialog.resize(584, 469)
        self.buttonBox = QDialogButtonBox(KontaktDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 430, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(KontaktDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 551, 401))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.VornamenInput = QLineEdit(self.layoutWidget)
        self.VornamenInput.setObjectName(u"VornamenInput")

        self.gridLayout.addWidget(self.VornamenInput, 0, 1, 1, 1)

        self.TelefonDropdown = QComboBox(self.layoutWidget)
        self.TelefonDropdown.setObjectName(u"TelefonDropdown")

        self.gridLayout.addWidget(self.TelefonDropdown, 5, 1, 1, 1)

        self.HausnummerInput = QLineEdit(self.layoutWidget)
        self.HausnummerInput.setObjectName(u"HausnummerInput")

        self.gridLayout.addWidget(self.HausnummerInput, 7, 1, 1, 1)

        self.PLZInput = QLineEdit(self.layoutWidget)
        self.PLZInput.setObjectName(u"PLZInput")

        self.gridLayout.addWidget(self.PLZInput, 9, 1, 1, 1)

        self.BankdatenInput = QLineEdit(self.layoutWidget)
        self.BankdatenInput.setObjectName(u"BankdatenInput")

        self.gridLayout.addWidget(self.BankdatenInput, 12, 1, 1, 1)

        self.TelefonnumerLoeschen = QPushButton(self.layoutWidget)
        self.TelefonnumerLoeschen.setObjectName(u"TelefonnumerLoeschen")

        self.gridLayout.addWidget(self.TelefonnumerLoeschen, 5, 2, 1, 1)

        self.TelefonHinzufuegen = QPushButton(self.layoutWidget)
        self.TelefonHinzufuegen.setObjectName(u"TelefonHinzufuegen")

        self.gridLayout.addWidget(self.TelefonHinzufuegen, 5, 3, 1, 1)

        self.Hausnummer = QLabel(self.layoutWidget)
        self.Hausnummer.setObjectName(u"Hausnummer")

        self.gridLayout.addWidget(self.Hausnummer, 7, 0, 1, 1)

        self.PLZ = QLabel(self.layoutWidget)
        self.PLZ.setObjectName(u"PLZ")

        self.gridLayout.addWidget(self.PLZ, 9, 0, 1, 1)

        self.Telefonnummer = QLabel(self.layoutWidget)
        self.Telefonnummer.setObjectName(u"Telefonnummer")

        self.gridLayout.addWidget(self.Telefonnummer, 5, 0, 1, 1)

        self.Spendeninformationen = QLabel(self.layoutWidget)
        self.Spendeninformationen.setObjectName(u"Spendeninformationen")

        self.gridLayout.addWidget(self.Spendeninformationen, 11, 0, 1, 1)

        self.KategorieHinzufuegen = QPushButton(self.layoutWidget)
        self.KategorieHinzufuegen.setObjectName(u"KategorieHinzufuegen")

        self.gridLayout.addWidget(self.KategorieHinzufuegen, 13, 3, 1, 1)

        self.Gender = QLabel(self.layoutWidget)
        self.Gender.setObjectName(u"Gender")

        self.gridLayout.addWidget(self.Gender, 3, 0, 1, 1)

        self.StrasseInput = QLineEdit(self.layoutWidget)
        self.StrasseInput.setObjectName(u"StrasseInput")

        self.gridLayout.addWidget(self.StrasseInput, 6, 1, 1, 1)

        self.Vornamen = QLabel(self.layoutWidget)
        self.Vornamen.setObjectName(u"Vornamen")

        self.gridLayout.addWidget(self.Vornamen, 0, 0, 1, 1)

        self.KategorieDropdown = QComboBox(self.layoutWidget)
        self.KategorieDropdown.setObjectName(u"KategorieDropdown")

        self.gridLayout.addWidget(self.KategorieDropdown, 13, 1, 1, 1)

        self.KategorieLoeschen = QPushButton(self.layoutWidget)
        self.KategorieLoeschen.setObjectName(u"KategorieLoeschen")

        self.gridLayout.addWidget(self.KategorieLoeschen, 13, 2, 1, 1)

        self.MailadresseInput = QLineEdit(self.layoutWidget)
        self.MailadresseInput.setObjectName(u"MailadresseInput")

        self.gridLayout.addWidget(self.MailadresseInput, 2, 1, 1, 1)

        self.Strasse = QLabel(self.layoutWidget)
        self.Strasse.setObjectName(u"Strasse")

        self.gridLayout.addWidget(self.Strasse, 6, 0, 1, 1)

        self.SpendenInput = QLineEdit(self.layoutWidget)
        self.SpendenInput.setObjectName(u"SpendenInput")

        self.gridLayout.addWidget(self.SpendenInput, 11, 1, 1, 1)

        self.Mailadresse = QLabel(self.layoutWidget)
        self.Mailadresse.setObjectName(u"Mailadresse")

        self.gridLayout.addWidget(self.Mailadresse, 2, 0, 1, 1)

        self.Land = QLabel(self.layoutWidget)
        self.Land.setObjectName(u"Land")

        self.gridLayout.addWidget(self.Land, 10, 0, 1, 1)

        self.LandInput = QLineEdit(self.layoutWidget)
        self.LandInput.setObjectName(u"LandInput")

        self.gridLayout.addWidget(self.LandInput, 10, 1, 1, 1)

        self.Bankdaten = QLabel(self.layoutWidget)
        self.Bankdaten.setObjectName(u"Bankdaten")

        self.gridLayout.addWidget(self.Bankdaten, 12, 0, 1, 1)

        self.Kategorie = QLabel(self.layoutWidget)
        self.Kategorie.setObjectName(u"Kategorie")

        self.gridLayout.addWidget(self.Kategorie, 13, 0, 1, 1)

        self.WohnortInput = QLineEdit(self.layoutWidget)
        self.WohnortInput.setObjectName(u"WohnortInput")

        self.gridLayout.addWidget(self.WohnortInput, 8, 1, 1, 1)

        self.NachnameInput = QLineEdit(self.layoutWidget)
        self.NachnameInput.setObjectName(u"NachnameInput")

        self.gridLayout.addWidget(self.NachnameInput, 1, 1, 1, 1)

        self.Wohnort = QLabel(self.layoutWidget)
        self.Wohnort.setObjectName(u"Wohnort")

        self.gridLayout.addWidget(self.Wohnort, 8, 0, 1, 1)

        self.Nachname = QLabel(self.layoutWidget)
        self.Nachname.setObjectName(u"Nachname")

        self.gridLayout.addWidget(self.Nachname, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.female = QRadioButton(self.groupBox)
        self.female.setObjectName(u"female")
        self.female.setGeometry(QRect(0, 0, 89, 20))
        self.male = QRadioButton(self.groupBox)
        self.male.setObjectName(u"male")
        self.male.setGeometry(QRect(90, 0, 89, 20))
        self.divers = QRadioButton(self.groupBox)
        self.divers.setObjectName(u"divers")
        self.divers.setGeometry(QRect(190, 0, 89, 20))
        self.unknown = QRadioButton(self.groupBox)
        self.unknown.setObjectName(u"unknown")
        self.unknown.setGeometry(QRect(290, 0, 89, 20))

        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 3)

        QWidget.setTabOrder(self.VornamenInput, self.NachnameInput)
        QWidget.setTabOrder(self.NachnameInput, self.MailadresseInput)
        QWidget.setTabOrder(self.MailadresseInput, self.female)
        QWidget.setTabOrder(self.female, self.male)
        QWidget.setTabOrder(self.male, self.divers)
        QWidget.setTabOrder(self.divers, self.unknown)
        QWidget.setTabOrder(self.unknown, self.TelefonDropdown)
        QWidget.setTabOrder(self.TelefonDropdown, self.TelefonnumerLoeschen)
        QWidget.setTabOrder(self.TelefonnumerLoeschen, self.TelefonHinzufuegen)
        QWidget.setTabOrder(self.TelefonHinzufuegen, self.StrasseInput)
        QWidget.setTabOrder(self.StrasseInput, self.HausnummerInput)
        QWidget.setTabOrder(self.HausnummerInput, self.WohnortInput)
        QWidget.setTabOrder(self.WohnortInput, self.PLZInput)
        QWidget.setTabOrder(self.PLZInput, self.LandInput)
        QWidget.setTabOrder(self.LandInput, self.SpendenInput)
        QWidget.setTabOrder(self.SpendenInput, self.BankdatenInput)
        QWidget.setTabOrder(self.BankdatenInput, self.KategorieDropdown)
        QWidget.setTabOrder(self.KategorieDropdown, self.KategorieLoeschen)
        QWidget.setTabOrder(self.KategorieLoeschen, self.KategorieHinzufuegen)

        self.retranslateUi(KontaktDialog)
        self.buttonBox.accepted.connect(KontaktDialog.accept)
        self.buttonBox.rejected.connect(KontaktDialog.reject)

        QMetaObject.connectSlotsByName(KontaktDialog)
    # setupUi

    def retranslateUi(self, KontaktDialog):
        KontaktDialog.setWindowTitle(QCoreApplication.translate("KontaktDialog", u"Dialog", None))
        self.TelefonnumerLoeschen.setText(QCoreApplication.translate("KontaktDialog", u"L\u00f6schen", None))
        self.TelefonHinzufuegen.setText(QCoreApplication.translate("KontaktDialog", u"Hinzuf\u00fcgen", None))
        self.Hausnummer.setText(QCoreApplication.translate("KontaktDialog", u"Hausnummer", None))
        self.PLZ.setText(QCoreApplication.translate("KontaktDialog", u"PLZ", None))
        self.Telefonnummer.setText(QCoreApplication.translate("KontaktDialog", u"Telefonnummern", None))
        self.Spendeninformationen.setText(QCoreApplication.translate("KontaktDialog", u"Spendeninformationen", None))
        self.KategorieHinzufuegen.setText(QCoreApplication.translate("KontaktDialog", u"Hinzuf\u00fcgen", None))
        self.Gender.setText(QCoreApplication.translate("KontaktDialog", u"Gender", None))
        self.Vornamen.setText(QCoreApplication.translate("KontaktDialog", u"Vornamen", None))
        self.KategorieLoeschen.setText(QCoreApplication.translate("KontaktDialog", u"L\u00f6schen", None))
        self.Strasse.setText(QCoreApplication.translate("KontaktDialog", u"Stra\u00dfe", None))
        self.Mailadresse.setText(QCoreApplication.translate("KontaktDialog", u"Mailadresse", None))
        self.Land.setText(QCoreApplication.translate("KontaktDialog", u"Land", None))
        self.Bankdaten.setText(QCoreApplication.translate("KontaktDialog", u"Bankdaten", None))
        self.Kategorie.setText(QCoreApplication.translate("KontaktDialog", u"Kategorie", None))
        self.Wohnort.setText(QCoreApplication.translate("KontaktDialog", u"Wohnort", None))
        self.Nachname.setText(QCoreApplication.translate("KontaktDialog", u"Nachname", None))
        self.groupBox.setTitle("")
        self.female.setText(QCoreApplication.translate("KontaktDialog", u"Frau", None))
        self.male.setText(QCoreApplication.translate("KontaktDialog", u"Mann", None))
        self.divers.setText(QCoreApplication.translate("KontaktDialog", u"Divers", None))
        self.unknown.setText(QCoreApplication.translate("KontaktDialog", u"Unbekannt", None))
    # retranslateUi

