'''
Created on 28.11.2023

@author: Jojo
'''
from JoJo.KontaktVerwaltung.Gui import Ui_MainWindow
from JoJo.KontaktVerwaltung.Kategoriendialog import Ui_KategorieAnlegenDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLineEdit, \
    QTableWidget, QTableWidgetItem, QDialog, QDialogButtonBox, QRadioButton, \
    QGroupBox, QAbstractItemView
import sys
from JoJo.KontaktVerwaltung.Services import KategorieRepository, DatabaseModule, \
    Page, KontakteRepository, KategorieExistiertBereits
from injector import inject, singleton, Injector
from JoJo.KontaktVerwaltung.KategorieLoeschen import Ui_Kategorie_loeschen
from JoJo.KontaktVerwaltung.KategorieBearbeiten import Ui_Kategorie_bearbeiten
from JoJo.KontaktVerwaltung.Kontaktdialog import Ui_KontaktDialog
from JoJo.KontaktVerwaltung.Domain import GenderTypes, Kontakt


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
            item_vornamen.kontakt = page.kontakt_list[row]
            item_nachname = QTableWidgetItem(page.kontakt_list[row].nachname)
            item_nachname.kontakt = page.kontakt_list[row]
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
        
    def fill_kategorie_dropdown(self, kategorien_combo_box: QComboBox, add_kein_eintrag:bool=False):

        kategorien_combo_box.clear()
        if add_kein_eintrag:
            kategorien_combo_box.addItem(self.KEINE_KATEGORIE)
        kategorien_liste = self.kategory_repository.find_all()
        for kategorie in kategorien_liste:
            kategorien_combo_box.addItem(kategorie.kategorienname)

        return kategorien_combo_box
    
    def save_kategorie(self,
                       lineEdit: QLineEdit,
                       kategorien_combo_box: QComboBox):
        
        new_kategorie = lineEdit.text()
        if new_kategorie.strip() == "":
            return
        
        try:
            self.kategory_repository.create(kategorienname=new_kategorie)
        except KategorieExistiertBereits:
            pass
        else:
            self.fill_kategorie_dropdown(kategorien_combo_box)
            
    def delete_kategorie(self, kategorien_combo_box: QComboBox):

        selected_kategorie = kategorien_combo_box.currentText()
        
        return self.kategory_repository.delete_by_name(selected_kategorie)
        
        kategorien_combo_box.clear()
        self.fill_kategorie_dropdown(kategorien_combo_box, add_kein_eintrag=True)
        
    def bearbeite_kategorie(self, kategorien_combo_box: QComboBox, lineEdit: QLineEdit):
        
        selected_kategorienname = kategorien_combo_box.currentText()
        selected_kategorie = self.kategory_repository.get_by_kategorienname(selected_kategorienname)
        new_kategorienname = lineEdit.text()
        print("hallo: " + new_kategorienname)
        selected_kategorie.kategorienname = new_kategorienname
    
    def clear_kontakt_dialog(self, kontakt_text_inputs):
    
        for line_edit_widget in kontakt_text_inputs.values():
            line_edit_widget.setText("")
        
            
    def kontakt_anlegen(self,
                        text_inputs,
                        adresse_inputs,
                        radio_buttons
                        ):
        
        kw_params = {}
        for paramname in text_inputs.keys():
            kw_params[paramname] = text_inputs[paramname].text()
        
        for radio_button in radio_buttons:
            if radio_button.isChecked():
                kw_params["gender"] = radio_button.gender
        
        kontakt = self.kontakte_repository.create(**kw_params)
        
        assert(kontakt is not None)
        
        kw_params = {}
        for paramname in adresse_inputs.keys():
            kw_params[paramname] = adresse_inputs[paramname].text()
        kw_params['kontakt'] = kontakt
        
        self.kontakte_repository.createAdresse(**kw_params)
        
        return kontakt
    
    def kontakt_init(self,
                     text_inputs,
                     adresse_inputs,
                     radio_buttons,
                     kontakt: Kontakt):
        
        for key in text_inputs.keys():
            text_inputs[key].setText(getattr(kontakt, key))
            
        for key in adresse_inputs.keys():
            try:
                adresse_inputs[key].setText(getattr(kontakt.adressen[0], key))
            except:
                adresse_inputs[key].setText("")
            
        for radio_button in radio_buttons:
            radio_button.setChecked(kontakt.gender == radio_button.gender)
        
    
    def kontakt_bearbeiten(self,
                           text_inputs,
                           adresse_inputs,
                           radio_buttons,
                           kontakt: Kontakt
                           ):

        for key in text_inputs.keys():
            setattr(kontakt, key, text_inputs[key].text())        
        
        if len(kontakt.adressen) == 0:
             self.kontakte_repository.createAdresse(kontakt)
            
        for key in adresse_inputs.keys():
            setattr(kontakt.adressen[0], key, adresse_inputs[key].text())
            
        for radio_button in radio_buttons:
            if radio_button.isChecked():
                kontakt.gender = radio_button.gender
                break

@singleton
class KontaktDialog(Ui_KontaktDialog, QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.radio_buttons = [self.female, self.male, self.divers, self.unknown]
        self.female.gender = GenderTypes.FEMALE
        self.male.gender = GenderTypes.MALE
        self.divers.gender = GenderTypes.DIVERS
        self.unknown.gender = GenderTypes.UNKNOWN

    
@singleton
class KategorienDialog(Ui_KategorieAnlegenDialog, QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        
@singleton        
class KategorieLoeschen(Ui_Kategorie_loeschen, QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.addButton(self.LoeschenButton, QDialogButtonBox.AcceptRole)
        self.buttonBox.accepted.connect(self.accept)        
        self.buttonBox.rejected.connect(self.reject)


@singleton        
class KategorieBearbeiten(Ui_Kategorie_bearbeiten, QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


@singleton
class MainGui(Ui_MainWindow, QMainWindow):
    
    @inject
    def __init__(self,
                 controller: Controller,
                 kategorien_dialog: KategorienDialog,
                 kategorie_loeschen: KategorieLoeschen,
                 kategorie_bearbeiten: KategorieBearbeiten,
                 kontakt_dialog: KontaktDialog
                 ) -> None:
        
        self.kategorien_dialog = kategorien_dialog
        self.kategorie_loeschen = kategorie_loeschen
        self.kategorie_bearbeiten = kategorie_bearbeiten
        self.kontakt_dialog = kontakt_dialog
        
        self.page = Page()
        
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.controller = controller
        self.setupUi(self)

        self.controller.fill_kategorie_dropdown(self.KategorienComboBox, add_kein_eintrag=True)
        self.searchButton.pressed.connect(self.cb_search)
        self.KategorienComboBox.setCurrentText(Controller.KEINE_KATEGORIE)
        self.controller.fill_tablewidget(self.page, self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(["Vorname", "Nachname"])
        self.NaechsteSeiteButton.pressed.connect(self.cb_next_page)
        self.NaechsteSeiteButton.setEnabled(False)
        self.VorherigeSeiteButton.pressed.connect(self.cp_previous_page)
        self.VorherigeSeiteButton.setEnabled(False)
        self.actionKategorie_anlegen.triggered.connect(self.cb_kategorien_dialog)
        self.actionKategorie_l_schen.triggered.connect(self.cb_kategorie_delete)
        self.actionKategorie_bearbeiten.triggered.connect(self.cb_kategorie_bearbeiten)
        self.actionKontakt_anlegen.triggered.connect(self.cb_kontakt_anlegen)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTriggers.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.itemDoubleClicked.connect(self.cb_kontakt_bearbeiten)

    def cb_search(self):
        
        self.page = self.controller.execute_search(Page(), self.searchFeld, self.KategorienComboBox)
        
        self.update_gui()
        
    def cb_next_page(self):
        
        self.page = self.controller.fetch_next_page(self.page)

        self.update_gui()
        
    def cp_previous_page(self):
        
        self.page = self.controller.fetch_previous_page(self.page)
        
        self.update_gui()
        
    def cb_kategorien_dialog(self):
        
        result = self.kategorien_dialog.exec()
        if result == QDialog.Accepted:
            self.controller.save_kategorie(self.kategorien_dialog.lineEdit, self.KategorienComboBox)
        else:
            print("Dialog wurde abgebrochen")
            
    def cb_kategorie_delete(self):
        
        self.controller.fill_kategorie_dropdown(self.kategorie_loeschen.KategorienComboBox)
        if self.kategorie_loeschen.exec() == QDialog.Accepted:
            self.controller.delete_kategorie(self.kategorie_loeschen.KategorienComboBox)
        self.KategorienComboBox.clear()
        self.controller.fill_kategorie_dropdown(self.KategorienComboBox)
    
    def cb_kategorie_bearbeiten(self):
        
        self.controller.fill_kategorie_dropdown(self.kategorie_bearbeiten.KategorienComboBox, add_kein_eintrag=False)
        result = self.kategorie_bearbeiten.exec()
        if result == QDialog.Accepted:
            self.controller.bearbeite_kategorie(self.kategorie_bearbeiten.KategorienComboBox,
                                                self.kategorie_bearbeiten.lineEdit)
            
        self.KategorienComboBox.clear()
        self.controller.fill_kategorie_dropdown(self.KategorienComboBox, add_kein_eintrag=True)
        
    def cb_kontakt_anlegen(self):
        
        self.controller.clear_kontakt_dialog(self.kontakt_text_inputs)
        self.kontakt_dialog.unknown.setChecked(True)
        
        result = self.kontakt_dialog.exec()
        
        if result != QDialog.Accepted:
            return
        
        self.controller.kontakt_anlegen(self.kontakt_text_inputs,
                                        self.kontakt_adresse_inputs,
                                        self.kontakt_dialog.radio_buttons)

        self.update_gui()
        
    def cb_kontakt_bearbeiten(self, table_item):
        
        self.controller.kontakt_init(self.kontakt_text_inputs,
                                     self.adresse_text_inputs,
                                     self.kontakt_dialog.radio_buttons,
                                     table_item.kontakt)
        
        result = self.kontakt_dialog.exec()
        
        if result != QDialog.Accepted:
            return
        
        self.controller.kontakt_bearbeiten(self.kontakt_text_inputs,
                                        self.adresse_text_inputs,
                                        self.kontakt_dialog.radio_buttons,
                                        table_item.kontakt)

        self.update_gui()
        
    def _get_kontakt_text_inputs(self):
        
        return {"nachname": self.kontakt_dialog.NachnameInput,
                "vornamen": self.kontakt_dialog.VornamenInput,
                "mailadresse": self.kontakt_dialog.MailadresseInput,
            }

    def _get_adresse_text_inputs(self):
        
        return {
                "strasse": self.kontakt_dialog.StrasseInput,
                "hausnummer": self.kontakt_dialog.HausnummerInput,
                "wohnort": self.kontakt_dialog.WohnortInput,
                "plz": self.kontakt_dialog.PLZInput,
                "land": self.kontakt_dialog.LandInput
            }
        
    def update_gui(self):
        
        self.NaechsteSeiteButton.setEnabled(not self.page.is_last_page())
        self.VorherigeSeiteButton.setEnabled(not self.page.is_first_page())
        self.controller.fill_tablewidget(self.page, self.tableWidget)
        
    kontakt_text_inputs = property(_get_kontakt_text_inputs)
    adresse_text_inputs = property(_get_adresse_text_inputs)

    
if __name__ == '__main__':
    
    injector = Injector([DatabaseModule])
    
    app = QApplication(sys.argv)
    
    gui = injector.get(MainGui)
    gui.show()
    
    app.exec()
