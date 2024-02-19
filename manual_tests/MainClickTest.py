'''
Created on 29.11.2023

@author: Jojo
'''
import unittest
from JoJo.KontaktVerwaltung.Services import DatabaseModule, DatenbankService,\
    KategorieRepository, KontakteRepository
from JoJo.KontaktVerwaltung.Main import Controller, MainGui
from sqlalchemy.orm.session import Session
import os
from unittest.mock import Mock
from injector import Injector
from PySide6.QtWidgets import QApplication
import sys
from sqlalchemy.engine.base import Engine
from JoJo.KontaktVerwaltung.Domain import GenderTypes

class Test(unittest.TestCase):


    def tearDown(self):
        
        del self.app
        
        session = self.injector.get(Session)
        engine = self.injector.get(Engine)
        session.commit()
        session.close()
        engine.dispose()
        

    def testKategorienDropDown(self):

        self.db_file = "C:\\Temp\\guitest.db"
        try:
            os.remove(self.db_file)
        except FileNotFoundError:
            pass
        
        os.environ["DB_FILE"] = self.db_file
        
        self.injector = Injector([DatabaseModule])
        
        dbservice = self.injector.get(DatenbankService)
    
        dbservice.setup()
        
        self.kategorien_service = self.injector.get(KategorieRepository)
        self.kontakte_service = self.injector.get(KontakteRepository)
        
        kategorien = [self.kategorien_service.create(kategorienname="Spender_in"),
                      self.kategorien_service.create(kategorienname="Fördermitglied"),
                      self.kategorien_service.create(kategorienname="Studierende"),
                      self.kategorien_service.create(kategorienname="Mitarbeitende"),
                      self.kategorien_service.create(kategorienname="Referent_innen")]
    
        for i in range (0, 30):
            k1 = self.kontakte_service.create(vornamen="Lisa%d" % i, nachname="Schulze%d" % i, gender=GenderTypes.FEMALE)
            self.kontakte_service.addKategorie(k1, kategorien[i % 5])
            k2 = self.kontakte_service.create(vornamen="Lutz%d" % i, nachname="Müller%d" % i, gender=GenderTypes.UNKNOWN) 
            self.kontakte_service.addKategorie(k2, kategorien[i % 5])
                
        self.app = QApplication()
            
        gui = self.injector.get(MainGui)
        gui.show()
    
        self.app.exec()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()