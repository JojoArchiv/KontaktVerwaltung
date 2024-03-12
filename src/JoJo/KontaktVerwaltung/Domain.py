'''
Created on 31.07.2023

@author: Jojo
'''
from sqlalchemy.orm.base import Mapped
from sqlalchemy.orm._orm_constructors import mapped_column, relationship
from typing import List
from typing import Optional
from sqlalchemy.sql.sqltypes import BOOLEAN, Integer
from sqlalchemy.sql.schema import ForeignKey, Column, Table, UniqueConstraint
from sqlalchemy.orm.decl_api import DeclarativeBase
import enum

class Base(DeclarativeBase):
    pass

kontakte_to_kategorien = Table(
    "kontakte_to_kategorien",
    Base.metadata,
    Column("kategorien_id", Integer, ForeignKey("kategorien.id"), primary_key=True),
    Column("kontakte_id", Integer, ForeignKey("kontakte.id"), primary_key=True)
    )

class GenderTypes(enum.Enum):
    
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2
    DIVERS = 3

class TelefonNummernTyp(enum.Enum):
    
    FESTNETZ_PRIVAT = 1
    FESTNETZ_BUERO = 2
    HANDY_PRIVAT = 3
    HANDY_BUERO = 4    
    
class Kategorie(Base):
    
    __tablename__ = "kategorien"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kategorienname: Mapped[str]
    __table_args__ = (UniqueConstraint("kategorienname", name="kateogrienname_unique"),)
    
    def __repr__(self) -> str:
        return f"Kategorie(id={self.id!r}, kategorienname={self.kategorienname!r})"
    
    def __init__(self):
        
        self.id:int = None 
        self.kategorienname:str = None 
        
    def __str__(self):
        
        return self.kategorienname
        
class Adresse(Base): 
    
    __tablename__ = "adressen"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    strasse: Mapped[Optional[str]]
    hausnummer: Mapped[Optional[int]]
    plz: Mapped[Optional[str]]
    wohnort: Mapped[Optional[str]]
    land: Mapped[Optional[str]]
    
    kontakt_id: Mapped[int] = mapped_column(ForeignKey("kontakte.id"))
    
    def __repr__(self) -> str:
        return f"Adresse(id={self.id!r}, strasse={self.strasse!r}, hausnummer={self.hausnummer!r}, plz={self.plz!r}, wohnort={self.wohnort!r}, land={self.land!r})"
       
    def __init__(self, kontakt):  
         
        self.id:int = None 
        self.strasse:str = None
        self.hausnummer:int = None
        self.plz:str = None
        self.wohnort:str = None
        self.land:str = None
        self.kontakt_id = kontakt.id
        kontakt.adressen.append(self)

class Spendeninformation(Base):
    
    __tablename__ = "spendeninformationen"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    spendenhoehe: Mapped[int]
    spendenjahr: Mapped[int]
    spendenbescheinigung: Mapped[Optional[bool]] = mapped_column(BOOLEAN)
    
    kontakt_id: Mapped[int] = mapped_column(ForeignKey("kontakte.id"))
    
    kontakt: Mapped["Kontakt"] = relationship(back_populates="spendeninformationen")
    
    def __repr__(self) -> str:
        return f"Spendeninformation(id={self.id!r}, spendenhoehe={self.spendenhoehe!r}, " + \
            "spendenjahr={self.spendenjahr!r}, spendenbescheinigung={self.spendenbescheinigung!r})"
            
    def __init__(self, kontakt):
        
        self.id:int = None
        self.spendenhoehe:int = None
        self.spendenjahr:int = None
        self.spendenbescheinigung:bool = False
        self.kontakt:Kontakt = None 
        self.kontakt_id = kontakt.id
        kontakt.spendeninformationen.append(self)

class Bankdaten(Base):
    
    __tablename__ = "bankdaten"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    iban: Mapped[str]
    bic: Mapped[Optional[str]]
    kreditinstitut: Mapped[Optional[str]]
    
    kontakt_id: Mapped[int] = mapped_column(ForeignKey("kontakte.id"))
    
    def __repr__(self) -> str:
        return f"Bankdaten(id={self.id!r}, iban={self.iban!r}, bic={self.bic!r}, kreditinstitut={self.kreditinstitut!r})"
    
    def __init__(self, kontakt):
        
        self.id:int = None 
        self.iban:str = None 
        self.bic:str = None 
        self.kreditinstitut:str = None 
        self.kontakt_id = kontakt.id 
        kontakt.bankdaten.append(self)
        
class Telefonnummer(Base):
    
    __tablename__ = "telefonnummern"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    telefonnummer: Mapped[str]
    
    telefon_nummern_typ = Mapped[TelefonNummernTyp]
    
    praeferiert: Mapped[bool]
    
    kontakt_id: Mapped[int] = mapped_column(ForeignKey("kontakte.id"))
    
    def __repr__(self) -> str:
        return f"Telefonnummer(id={self.id!r}, telefonnummer={self.telefonnummer!r}, telefon_nummern_typ={self.telefon_nummern_typ!r}, praeferiert={self.praeferiert!r})"
    
    def __init__(self, kontakt):
        
        self.id:int = None 
        self.telefonnummer:str = None 
        self.telefon_nummern_typ:TelefonNummernTyp = None 
        self.praeferiert:bool = False 
        self.kontakt_id = kontakt.id
        kontakt.telefonnummern.append(self)
    
class Kontakt(Base):
    
    __tablename__ = "kontakte"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nachname: Mapped[Optional[str]]
    vornamen: Mapped[Optional[str]]
    mailadresse: Mapped[Optional[str]]
    
    gender: Mapped[GenderTypes]
    
    adressen: Mapped[List[Adresse]] = relationship(
    cascade="all, delete-orphan"
    )
    
    spendeninformationen: Mapped[List[Spendeninformation]] = relationship(
        back_populates="kontakt", cascade="all, delete-orphan"
    )
    
    bankdaten: Mapped[List[Bankdaten]] = relationship(
    cascade="all, delete-orphan"
    )
    
    kategorien: Mapped[List[Kategorie]] = relationship(
        secondary=kontakte_to_kategorien
    )
    
    telefonnummern: Mapped[List[Telefonnummer]] = relationship(
    cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"Kontakt(id={self.id!r}, nachname={self.nachname!r}, vornamen={self.vornamen!r}, mailadresse={self.mailadresse!r})"
    
    def __init__(self):
        
        self.id:int = None
        self.nachname:str = None
        self.vornamen:str = None
        self.mailadresse:str = None
        self.gender:str = None
        self.adressen = []
        self.spendeninformationen = []
        self.bankdaten = []
        self.kategorien = []
            
        