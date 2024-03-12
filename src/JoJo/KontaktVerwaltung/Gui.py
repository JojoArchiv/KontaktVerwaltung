# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(547, 543)
        self.actionKategorie_anlegen = QAction(MainWindow)
        self.actionKategorie_anlegen.setObjectName(u"actionKategorie_anlegen")
        self.actionKategorie_bearbeiten = QAction(MainWindow)
        self.actionKategorie_bearbeiten.setObjectName(u"actionKategorie_bearbeiten")
        self.actionKategorie_l_schen = QAction(MainWindow)
        self.actionKategorie_l_schen.setObjectName(u"actionKategorie_l_schen")
        self.actionKontakt_anlegen = QAction(MainWindow)
        self.actionKontakt_anlegen.setObjectName(u"actionKontakt_anlegen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchFeld = QLineEdit(self.centralwidget)
        self.searchFeld.setObjectName(u"searchFeld")

        self.horizontalLayout.addWidget(self.searchFeld)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.KategorienComboBox = QComboBox(self.centralwidget)
        self.KategorienComboBox.setObjectName(u"KategorienComboBox")

        self.verticalLayout.addWidget(self.KategorienComboBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.NaechsteSeiteButton = QPushButton(self.centralwidget)
        self.NaechsteSeiteButton.setObjectName(u"NaechsteSeiteButton")

        self.verticalLayout_2.addWidget(self.NaechsteSeiteButton)

        self.VorherigeSeiteButton = QPushButton(self.centralwidget)
        self.VorherigeSeiteButton.setObjectName(u"VorherigeSeiteButton")

        self.verticalLayout_2.addWidget(self.VorherigeSeiteButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 547, 22))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuBearbeiten = QMenu(self.menubar)
        self.menuBearbeiten.setObjectName(u"menuBearbeiten")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuBearbeiten.menuAction())
        self.menuBearbeiten.addAction(self.actionKategorie_anlegen)
        self.menuBearbeiten.addSeparator()
        self.menuBearbeiten.addAction(self.actionKategorie_bearbeiten)
        self.menuBearbeiten.addSeparator()
        self.menuBearbeiten.addAction(self.actionKategorie_l_schen)
        self.menuBearbeiten.addSeparator()
        self.menuBearbeiten.addAction(self.actionKontakt_anlegen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionKategorie_anlegen.setText(QCoreApplication.translate("MainWindow", u"Kategorie anlegen", None))
        self.actionKategorie_bearbeiten.setText(QCoreApplication.translate("MainWindow", u"Kategorie bearbeiten", None))
        self.actionKategorie_l_schen.setText(QCoreApplication.translate("MainWindow", u"Kategorie l\u00f6schen", None))
        self.actionKontakt_anlegen.setText(QCoreApplication.translate("MainWindow", u"Kontakt anlegen", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))
        self.NaechsteSeiteButton.setText(QCoreApplication.translate("MainWindow", u"n\u00e4chste Seite", None))
        self.VorherigeSeiteButton.setText(QCoreApplication.translate("MainWindow", u"vorherige Seite", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuBearbeiten.setTitle(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
    # retranslateUi

