import unittest
from unittest.mock import MagicMock
from JoJo.KontaktVerwaltung.Services import KategorieRepository,\
    KontakteRepository, Page
from JoJo.KontaktVerwaltung.Domain import Kategorie, Kontakt, GenderTypes
from mock.mock import Mock, call
from JoJo.KontaktVerwaltung.Main import Controller
from PySide6.QtWidgets import QComboBox, QApplication, QTableWidget,\
    QTableWidgetItem, QLineEdit, QDialog, QRadioButton


class MainMockTest(unittest.TestCase):

    app = None

    @classmethod
    def setUpClass(cls):
        
        MainMockTest.app = QApplication()
        
    @classmethod
    def tearDownClass(cls)->None:
        
        del MainMockTest.app
        
    def setUp(self):
        
        self.kategorien_combo_box = QComboBox()
        self.searchFeld = MagicMock()
        
        self.page = Page()
        
        self.kategorie_repository = MagicMock(KategorieRepository)
        self.kontakte_repository = MagicMock(KontakteRepository)
        self.controller = Controller(self.kategorie_repository, self.kontakte_repository)
        
        kategorie1 = Kategorie()
        kategorie1.kategorienname="Spender_in"
        kategorie2 = Kategorie()
        kategorie2.kategorienname="Fördermitglied"
        kategorie3 = Kategorie()
        kategorie3.kategorienname="Studierende"
        kategorie4 = Kategorie()
        kategorie4.kategorienname="Mitarbeitende"
        kategorie5 = Kategorie()
        kategorie5.kategorienname="Referent_innen"
        
        self.kategorie_repository.find_all.return_value = \
            [kategorie1, kategorie2, kategorie3,
             kategorie4, kategorie5]

        
    def tearDown(self):
        pass

    def test_find_all(self):
        
        self.controller.fill_kategorie_dropdown(self.kategorien_combo_box, add_kein_eintrag=True)
        self.assertEqual(6, self.kategorien_combo_box.count())
        self.assertEqual(self.kategorien_combo_box.itemText(0), "Kein Eintrag")
        self.assertEqual(self.kategorien_combo_box.itemText(5), "Referent_innen")
        
    def test_search_with_kategorie(self):
        
        KATEGORIE_TEXT = "Spender_in"
        self.searchFeld.text("Müller")
        
        self.controller.fill_kategorie_dropdown(self.kategorien_combo_box)
        self.kategorien_combo_box.setCurrentText(KATEGORIE_TEXT)
        
        self.controller.execute_search(self.page, self.searchFeld, self.kategorien_combo_box)
        self.kontakte_repository.get_page.assert_called_once()
        self.assertEqual(self.page.kategory_filter, KATEGORIE_TEXT)
    
    def test_search_without_kategorie(self):
        
        self.searchFeld.text("Müller")
        
        self.controller.fill_kategorie_dropdown(self.kategorien_combo_box, add_kein_eintrag=True)
        #self.kategorien_combo_box.setCurrentText(Controller.KEINE_KATEGORIE)

        self.controller.execute_search(self.page, self.searchFeld, self.kategorien_combo_box)
        self.kontakte_repository.get_page.assert_called_once()
        self.assertEqual(self.page.kategory_filter, None)
  
    def test_fill_tablewidget(self):
        
        kontakt1 = Kontakt()
        kontakt1.vornamen="Lutz"
        kontakt1.nachname="Müller"
        kontakt2 = Kontakt()
        kontakt2.vornamen = "Lisa"
        kontakt2.nachname = "Schulz"
        
        page = Page()
        page.kontakt_list = [kontakt1, kontakt2, kontakt2,
                             kontakt1, kontakt2]
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")
        
        tablewidget = QTableWidget()

        tablewidget.setColumnCount(Controller.TABLE_COLUMNS)
        tablewidget.setRowCount(page.page_size)

        for row in range(0, page.page_size):
            for column in range(0, Controller.TABLE_COLUMNS):
                item = QTableWidgetItem("X")
                tablewidget.setItem(row, column, item)

        self.controller.fill_tablewidget(page, tablewidget)
        
        selected_item = tablewidget.item(3, 0).text()
        self.assertEqual(selected_item, kontakt1.vornamen)
        selected_item2 = tablewidget.item(4,1).text()
        self.assertEqual(selected_item2, kontakt2.nachname)
        
        for row in range(0, page.page_size):
            for column in range(0, Controller.TABLE_COLUMNS):
                self.assertNotEqual(tablewidget.item(row, column).text() , "X")

    def test_fill_tabelwidget_with_2_kontakte(self):
        
        kontakt1 = Kontakt()
        kontakt1.vornamen="Lutz"
        kontakt1.nachname="Müller"
        kontakt2 = Kontakt()
        kontakt2.vornamen = "Lisa"
        kontakt2.nachname = "Schulz"
        
        page = Page()
        page.kontakt_list = [kontakt1, kontakt2]
        self.assertEqual(page.kontakt_list[0].nachname, "Müller")
        
        tablewidget = QTableWidget()
        
        self.controller.fill_tablewidget(page, tablewidget)
        
        selected_item = tablewidget.item(0, 0).text()
        self.assertTrue(selected_item is not None)
        self.assertEqual(selected_item, kontakt1.vornamen)
        selected_item2 = tablewidget.item(1,1).text()
        self.assertEqual(selected_item2, kontakt2.nachname)
        
    def test_save_new_kategorie(self):
        
        self.lineEdit = MagicMock()
        
        self.lineEdit("Kategorie 1")
        self.controller.save_kategorie(self.lineEdit, self.kategorien_combo_box)
        self.kategorie_repository.create.assert_called_once()
        
    def test_delete_kategorie(self):
        
        self.kategorien_combo_box = MagicMock()
        
        self.kategorien_combo_box.currentText.return_value = "Kategorie 1"
        self.controller.delete_kategorie(self.kategorien_combo_box)
        self.kategorie_repository.delete_by_name.assert_called_once_with("Kategorie 1")
        
    def test_kategorie_bearbeiten(self):
        
        self.kategorien_combo_box = MagicMock()
        self.lineEdit = MagicMock()
        
        self.controller.bearbeite_kategorie(self.kategorien_combo_box, self.lineEdit)
        
    def test_kontakt_anlegen(self):
        
        text_inputs = {"nachname": QLineEdit(text="nachname"),
                "vornamen": QLineEdit(text="vornamen"),
                "mailadresse": QLineEdit(text="mailadresse"),
            }

        adresse_inputs = {
                "strasse": QLineEdit(text="strasse"),
                "hausnummer": QLineEdit(text="hausnummer"),
                "wohnort": QLineEdit(text="wohnort"),
                "plz": QLineEdit(text="plz"),
                "land": QLineEdit(text="land")
            }
        
        rb1 = QRadioButton()
        rb1.setChecked(True)
        rb1.gender = GenderTypes.MALE
        rb2 = QRadioButton()
        rb2.setChecked(False)
        rb2.gender = GenderTypes.FEMALE
        
        kontakt = Kontakt()
        kontakt.id = 42
        self.kontakte_repository.create.return_value = kontakt
            
        self.controller.kontakt_anlegen(text_inputs, adresse_inputs, [rb1, rb2])
        self.kontakte_repository.create.assert_called_once_with(nachname='nachname',
                                                                vornamen='vornamen',
                                                                mailadresse='mailadresse',
                                                                gender=GenderTypes.MALE)
        
        self.kontakte_repository.createAdresse.assert_called_once_with(strasse='strasse',
                                                                hausnummer='hausnummer',
                                                                wohnort='wohnort',
                                                                plz='plz',
                                                                land='land',
                                                                kontakt=kontakt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()