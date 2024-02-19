'''
Created on 09.08.2023

@author: Jojo
'''

from sqlalchemy import create_engine
from JoJo.KontaktVerwaltung.Domain import Base, Kontakt, Kategorie,\
    Adresse, Spendeninformation, Bankdaten, Telefonnummer,\
    kontakte_to_kategorien
from sqlalchemy.orm.session import Session
from sqlalchemy.sql._selectable_constructors import select
from enum import Enum
from _operator import or_, and_
from injector import Module, inject, provider, singleton
import os
from sqlalchemy.engine.base import Engine


class KontakteException(Exception):
    
    pass

class IllegalIdException(KontakteException):
    
    def __init__(self, id):
        
        if id is None:
            super().__init__("None is not a valid identifier")
        else:
            super().__init__("%d is not a valid identifier" % id)

class RecordOrder(Enum):
    
    NACHNAME_AUFSTEIGEND = 1            
            
class Page(object):
    
    def __init__(self):
        
        self.page_idx:int = 0
        self.page_size = 10
        self.record_order:RecordOrder = RecordOrder.NACHNAME_AUFSTEIGEND
        self.kategory_filter:Kategorie = None
        self.search_string:str = None
        
        self.kontakt_list = []
        self.number_of_pages = None
        
    def is_last_page(self) -> bool:
        
        return self.page_idx + 1 == self.number_of_pages
        
    def is_first_page(self) -> bool:
        
        return self.page_idx == 0
        
class DatenbankService(object):
    '''
    classdocs
    '''
    
    def __init__(self, url="sqlite://"):
        '''
        Constructor
        '''
        self.url = url
        self.engine = None
    
    def setup(self):
        
        engine = self.create_engine() 
        
        Base.metadata.create_all(engine, checkfirst=False)
        
        return engine
    
    def create_engine(self):
        
        if self.engine is None:
            self.engine = create_engine(self.url, echo=True)
        
        return self.engine 

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
        
@singleton
class KontakteRepository(BaseRepository):
    
    @inject
    def __init__(self, session: Session):
        
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
    
    def get_page(self, page: Page) -> Page:

        where_clause = self._build_where_clause(page)
    
        page.number_of_pages = self._get_number_of_pages_for_page(page, where_clause)
        
        select_stmt = self._build_select(page)
        if where_clause is not None:
            select_stmt = select_stmt.where(where_clause)
        results = self.session.execute(select_stmt)
        
        page.kontakt_list = []
        for kontakt in results.scalars():
            page.kontakt_list.append(kontakt)
            
        return page
    
    def get_next_page(self, page: Page) -> Page:
        
        if page.page_idx + 1 >= page.number_of_pages:
            raise Exception("There is no next page.")
        
        page.page_idx += 1
        
        return self.get_page(page)     
    
    def get_previous_page(self, page: Page) -> Page:  
        
        if page.page_idx <= 0:
            raise Exception("There is no previous page") 
        
        page.page_idx -= 1
        
        return self.get_page(page)
    
    def _build_select(self, page: Page):
        
        stmt = select(Kontakt).\
               order_by(Kontakt.nachname).\
               limit(page.page_size).\
               offset(page.page_idx*page.page_size)
               
        if page.kategory_filter is not None:
            stmt = stmt.join(kontakte_to_kategorien).\
                    join(Kategorie)

        return stmt
    
    def _build_query(self, page: Page):
        
        query = self.session.query(Kontakt)
               
        if page.kategory_filter is not None:
            query = query.join(kontakte_to_kategorien).\
                join(Kategorie)

        return query

    def _build_where_clause(self, page: Page):
        
        print(page.search_string)
        if (page.search_string is None or page.search_string == "") and \
            (page.kategory_filter is None or page.kategory_filter == ""):
            return None
        
        search_clause = None
        if page.search_string is not None:
            search_clause = or_(or_(Kontakt.nachname.ilike('%%%s%%' % page.search_string),
                Kontakt.vornamen.ilike('%%%s%%' % page.search_string)),
                Kontakt.mailadresse.ilike('%%%s%%' % page.search_string))
            if page.kategory_filter is None:
                return search_clause
            
        kategorie_clause = None
        if page.kategory_filter is not None:
            kategorie_clause = Kategorie.kategorienname == page.kategory_filter
            if page.search_string is None:
                return kategorie_clause
            
        return and_(search_clause, kategorie_clause)

    def _get_number_of_pages_for_page(self, page: Page, where_clause) -> int:
        
        query = self._build_query(page)
        
        if where_clause is not None:
            query = query.where(where_clause) 
        
        count_result = query.count()
        number_of_pages = int(count_result / page.page_size)
        
        if count_result % page.page_size > 0:
            number_of_pages += 1
        
        return number_of_pages
    
    def delete(self, kontakt):
        
        super().delete(kontakt)

@singleton
class KategorieRepository(BaseRepository):
    
    @inject
    def __init__(self, session: Session):
        
        super().__init__(session, Kategorie)
        
    def get_by_kategorienname(self, kategorienname: str) -> Kategorie:
        
        stmt = select(Kategorie).where(Kategorie.kategorienname == kategorienname)
        results = self.session.execute(stmt)
        
        list_of_kategorien = []
        for kategorie in results.scalars():
            list_of_kategorien.append(kategorie)
        
        assert(len(list_of_kategorien) == 1)
            
        return list_of_kategorien[0]

    def find_all(self):
        
        stmt = select(Kategorie).order_by(Kategorie.kategorienname)
        results = self.session.execute(stmt)
        
        list_of_kategorien = []
        for kategorie in results.scalars():
            list_of_kategorien.append(kategorie)
            
        return list_of_kategorien     

class DatabaseModule(Module):
    
    @provider
    @singleton
    def get_db_service(self) -> DatenbankService:
        
        self.db_file = "C:\\Temp\\database.db"
      
        if "DB_FILE" in os.environ:
            self.db_file = os.environ["DB_FILE"]
        
        return DatenbankService("sqlite:///%s" % self.db_file)
    
    @inject
    @provider
    @singleton
    def get_session(self, engine: Engine) -> Session:
        
        return Session(engine)

    @inject
    @provider
    @singleton
    def get_engine(self, db_service: DatenbankService) -> Engine:
        
        return db_service.create_engine()