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

class A1_3(Base):
    __tablename__ = 'A1_3'
    
    CountryCode = Column(String, primary_key=True)
    BirdRed = Column(String)
    BirdAmd = Column(String)
    BirdGrn = Column(String)

class A1_3_1_ActionPlan(Base):
    __tablename__ = 'A1_3_1_ActionPlan'

    CountryCode = Column(String, primary_key=True)
    BirdComp = Column(String)
    MammalComp = Column(String)
    AmphibComp = Column(String)
    FishComp = Column(String)
    InvertComp = Column(String)
    PlantsComp = Column(String)
    BirdPlan = Column(String)
    MammalPlan = Column(String)
    AmphibPlan = Column(String)
    FishPlan = Column(String)
    InvertPlan = Column(String)
    PlantsPlan = Column(String)
    PlanDataSource = Column(String)

class A1_3_1_BirdIndicator(Base):
    __tablename__ = 'A1_3_1_BirdIndicator'

    CountryCode = Column(String, primary_key=True)
    IndicatorDev = Column(String)
    IndicatorDesc = Column(String)
    DataSource = Column(String)

class A1_3_1_BirdMonitoring(Base):
    __tablename__ = 'A1_3_1_BirdMonitoring'

    CountryCode = Column(String, primary_key=True)
    active = Column(String)

class A1_3_1_RedList(Base):
    __tablename__ = 'A1_3_1_RedList'

    CountryCode = Column(String, primary_key=True)
    Bird = Column(String)
    Mammal = Column(String)
    Amphib = Column(String)
    Fish = Column(String)
    Invert = Column(String)
    Plants = Column(String)
