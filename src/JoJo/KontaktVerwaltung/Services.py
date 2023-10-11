'''
Created on 09.08.2023

@author: Jojo
'''

from sqlalchemy import create_engine
from JoJo.KontaktVerwaltung.Domain import Base, Kontakt, GenderTypes, Kategorie,\
    Adresse, Spendeninformation, Bankdaten, Telefonnummer,\
    kontakte_to_kategorien
from sqlalchemy.orm.session import Session
from sqlalchemy.sql._selectable_constructors import select
from sqlalchemy.sql._dml_constructors import delete

class KontakteException(Exception):
    
    pass

class IllegalIdException(KontakteException):
    
    def __init__(self, id):
        
        if id is None:
            super().__init__("None is not a valid identifier")
        else:
            super().__init__("%d is not a valid identifier" % id)

class DatenbankService(object):
    '''
    classdocs
    '''
    
    def __init__(self, url="sqlite://"):
        '''
        Constructor
        '''
        self.url = url
    
    def setup(self):
        
        engine = self.create_engine() 
        
        Base.metadata.create_all(engine, checkfirst=False)
        
        return engine
    
    def create_engine(self):

        return create_engine(self.url, echo=True) 

class BaseRepository(object):
    
    def __init__(self, session, repository_class):
        
        self.session:Session = session

        self.repository_class = repository_class

    def create(self, **kwargs):

        return self._create(self.repository_class, **kwargs)
    
    def _create(self, class_definition, *parent_objects, **kwargs):

        class_instance = class_definition(*parent_objects)
                
        for key, value in kwargs.items():
            setattr(class_instance, key, value)

        self.session.add(class_instance)
        self.session.commit()
        
        return class_instance
        
    def get(self, id:int):
        
        stmt = select(self.repository_class).where(self.repository_class.id == id)
        results = self.session.execute(stmt)

        for class_instance in results.scalars():
            return class_instance
        
        raise IllegalIdException(id)
    
    def delete(self, class_instance):

        self.session.delete(class_instance)
        
class KontakteRepository(BaseRepository):
    
    def __init__(self, session):
        
        super().__init__(session, Kontakt)
        
    def createAdresse(self, kontakt, **kwargs):
        
        adresse = self._create(Adresse, kontakt, **kwargs)
        return adresse
    
    def createSpendeninformation(self, kontakt, **kwargs):
        
        spendeninformation = self._create(Spendeninformation, kontakt, **kwargs)
        return spendeninformation
    
    def createBankdaten(self, kontakt, **kwargs):
        
        bankdaten = self._create(Bankdaten, kontakt, **kwargs)
        return bankdaten
    
    def createTelefonnummer(self, kontakt, **kwargs):
        
        telefonnummer = self._create(Telefonnummer, kontakt, **kwargs)
        return telefonnummer
    
    def addKategorie(self, kontakt, kategorie):
        
        stmt = select(Kontakt).join(Kontakt.kategorien)
        self.session.execute(stmt)
        kontakt.kategorien.append(kategorie)
        self.session.flush([kontakt, kategorie])
        self.session.expire(kategorie)
        self.session.expire(kontakt)
        
    def find_by_nachname(self, nachname):

        stmt = select(Kontakt).where(Kontakt.nachname == nachname)
        results = self.session.execute(stmt)
        
        list_of_kontakte = []
        for kontakt in results.scalars():
            list_of_kontakte.append(kontakt)
            
        return list_of_kontakte
            
    def find_by_spendeninformation(self, spendenjahr):
        
        stmt = select(Kontakt).join(Spendeninformation).where(Spendeninformation.spendenjahr == spendenjahr)   
        results = self.session.execute(stmt)
        
        list_of_kontakte = []
        for kontakt in results.scalars():
            list_of_kontakte.append(kontakt)
            
        return list_of_kontakte     
    
    def find_by_kategorie(self, kategorienname):
        
        stmt = select(Kontakt).join(kontakte_to_kategorien).join(Kategorie).where(Kategorie.kategorienname == kategorienname)
        results = self.session.execute(stmt)
        
        list_of_kontakte = []
        for kontakt in results.scalars():
            list_of_kontakte.append(kontakt)
        
        return list_of_kontakte
    
    def delete(self, kontakt):
        
        super().delete(kontakt)
    
class KategorieRepository(BaseRepository):
    
    def __init__(self, session):
        
        super().__init__(session, Kategorie)
