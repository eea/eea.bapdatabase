from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String
from utilities import cp_1252_chars


Base = declarative_base()


class Header(Base):
    __tablename__ = '01Header'
    
    CountryCode = Column(String, primary_key=True)
    Country = Column(String)
    PrefilledName = Column(String)
    PrefilledVerifiedCOName = Column(String)
    PrefilledVerifiedCODate = Column(String)
    PrefilledVerifiedECName = Column(String)
    PrefilledVerifiedECDate = Column(String)
    DataEntryMSName = Column(String)
    DataEntryCOName = Column(String)
    VerifiedMSName = Column(String)
    VerifiedMSDate = Column(String)
    VerifiedCOName = Column(String)
    VerifiedCODate = Column(String)
    VerifiedECName = Column(String)
    VerifiedECDate = Column(String)


class Narrative(Base):
    __tablename__ = 'Narrative'

    Country = Column(String, ForeignKey('01Header.CountryCode'), primary_key=True)
    Objective = Column(String)
    Ident = Column(String)
    MOP = Column(String)
    Narative = Column(String)
    MSComments = Column(String)
    Clarifcations = Column(String)
    DataSource = Column(String)
    MSVerrified = Column(String)
    EC1Verrified = Column(String)
    EC2Verrified = Column(String)
    CO1Verrified = Column(String)
    CO2Verrified = Column(String)


class QuestionsText(Base):
    __tablename__ = 'QuestionsText'

    ID = Column(String, primary_key=True)
    Ident = Column(String, ForeignKey('Narrative.Ident'))
    MOP = Column(String)
    Action = Column(String)
    MSAction = Column(String)
    FullText = Column(String)
    MOPText = Column(String)


class Objective(Base):
    __tablename__ = 'objectives'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)