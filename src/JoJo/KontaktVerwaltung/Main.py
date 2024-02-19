'''
Created on 28.11.2023

@author: Jojo
'''
from JoJo.KontaktVerwaltung.Gui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLineEdit,\
    QTableWidget, QTableWidgetItem
import sys
from JoJo.KontaktVerwaltung.Services import KategorieRepository, DatabaseModule,\
    Page, KontakteRepository
from injector import inject, singleton, Injector



@singleton
class Controller():
    
    KEINE_KATEGORIE = "Kein Eintrag"
    TABLE_COLUMNS = 2
    
    @inject
    def __init__(self,
                 kategory_repository: KategorieRepository,
                 kontakte_repository: KontakteRepository):

        self.kategory_repository = kategory_repository
        self.kontakte_repository = kontakte_repository
        
    def execute_search(self,
                       page: Page,
                       searchFeld: QLineEdit,
                       kategorien_combo_box: QComboBox):
        
        page.search_string = searchFeld.text()
        selected_kategorienname = kategorien_combo_box.currentText()
        if selected_kategorienname != self.KEINE_KATEGORIE:
            page.kategory_filter = selected_kategorienname
        else:
            page.kategory_filter = None
        
        return self.kontakte_repository.get_page(page)
        
    def fill_tablewidget(self, page: Page, tablewidget: QTableWidget):
        
        tablewidget.setColumnCount(self.TABLE_COLUMNS)
        tablewidget.setRowCount(page.page_size)
        
        assert(page.page_size >= len(page.kontakt_list))

        for row in range(0, len(page.kontakt_list)):
            item_vornamen = QTableWidgetItem(page.kontakt_list[row].vornamen)
            item_nachname = QTableWidgetItem(page.kontakt_list[row].nachname)
            tablewidget.setItem(row, 0, item_vornamen)
            tablewidget.setItem(row, 1, item_nachname)

        for row in range(len(page.kontakt_list), page.page_size):
            item_vornamen = QTableWidgetItem("")
            item_nachname = QTableWidgetItem("")
            tablewidget.setItem(row, 0, item_vornamen)
            tablewidget.setItem(row, 1, item_nachname)
    
    def fetch_next_page(self, page: Page):
        
        return self.kontakte_repository.get_next_page(page)
    
    def fetch_previous_page(self, page:Page):
        
        return self.kontakte_repository.get_previous_page(page)
        
    def fill_kategorie_dropdown(self, kategorien_combo_box: QComboBox):

        kategorien_combo_box.addItem(self.KEINE_KATEGORIE)

        kategorien_liste = self.kategory_repository.find_all()
        for kategorie in kategorien_liste:
            kategorien_combo_box.addItem(kategorie.kategorienname)

        return kategorien_combo_box

@singleton
class MainGui(Ui_MainWindow, QMainWindow):
    
    @inject
    def __init__(self, controller: Controller)->None:
        
        self.page = Page()
        
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.controller = controller
        self.setupUi(self)

        self.controller.fill_kategorie_dropdown(self.KategorienComboBox)
        self.searchButton.pressed.connect(self.search)
        self.KategorienComboBox.setCurrentText(Controller.KEINE_KATEGORIE)
        self.controller.fill_tablewidget(self.page, self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(["Vorname", "Nachname"])
        self.NaechsteSeiteButton.pressed.connect(self.next_page)
        self.NaechsteSeiteButton.setEnabled(False)
        self.VorherigeSeiteButton.pressed.connect(self.previous_page)
        self.VorherigeSeiteButton.setEnabled(False)

    def search(self):
        
        self.page = self.controller.execute_search(Page(), self.searchFeld, self.KategorienComboBox)
        
        self.update_gui()
        
    def next_page(self):
        
        self.page = self.controller.fetch_next_page(self.page)

        self.update_gui()
        
    def previous_page(self):
        
        self.page = self.controller.fetch_previous_page(self.page)
        
        self.update_gui()

    def update_gui(self):
        
        self.NaechsteSeiteButton.setEnabled(not self.page.is_last_page())
        self.VorherigeSeiteButton.setEnabled(not self.page.is_first_page())
        self.controller.fill_tablewidget(self.page, self.tableWidget)
        
if __name__ == '__main__':
    
    injector = Injector([DatabaseModule])
    
    app = QApplication(sys.argv)
    
    gui = injector.get(MainGui)
    gui.show()
    
    app.exec()