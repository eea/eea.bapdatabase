from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String

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

    Country = Column(String, primary_key=True)
    Objective = Column(String, primary_key=True)
    Ident = Column(String, primary_key=True)
    MOP = Column(String, primary_key=True)
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
    Ident = Column(String)
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


class A1_1_1_Natura2000Compleat(Base):
  __tablename__ = 'A1_1_1_Natura2000Compleat'

  CountryCode = Column(String, primary_key=True)
  HabitatSites = Column(String)
  HabitatArea = Column(String)
  HabitatTerraArea = Column(String)
  HabitatMarineSites = Column(String)
  HabitatMarineArea = Column(String)
  BirdSites = Column(String)
  BirdArea = Column(String)
  BirdTerraArea = Column(String)
  BirdMarineSites = Column(String)
  BirdMarineArea = Column(String)
  

class A1_1_1_Natura2000Plan(Base):
    __tablename__ = 'A1_1_1_Natura2000Plan'

    CountryCode = Column(String, primary_key=True)
    Compleat = Column(String)
    Preperation = Column(String)
    None_ = Column('None', String)

      
class A1_1_3(Base):
    __tablename__ = 'A1_1_3'

    CountryCode = Column(String, primary_key=True)
    Y2004 = Column(String)
    Y2005 = Column(String)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

        
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


class A2_1_1(Base):
    __tablename__ = 'A2_1_1'

    CountryCode = Column(String, primary_key=True)
    EAFRDTotal = Column(String)
    EAFRDAxis2 = Column(String)
    EAFRDAxis2Percent = Column(String)
    PublicTotal = Column(String)
    PublicAxis2 = Column(String)
    PublicAxis2Percent = Column(String)
    AgriEAFRD = Column(String)
    AgriEAFRDPercent = Column(String)
    AgriPublic = Column(String)
    AgriPublicPercent = Column(String)
    NaturaAgriEAFRD = Column(String)
    NaturaAgriEAFRDPercent = Column(String)
    NaturaAgriPublic = Column(String)
    NaturaAgriPublicPercent = Column(String)
    NaturaForestEAFRD = Column(String)
    NaturaForestEAFRDPercent = Column(String)
    NaturaForestPublic = Column(String)
    NaturaForestPublicPercent = Column(String)
    ForestEAFRD = Column(String)
    ForestEAFRDPercent = Column(String)
    ForestPublic = Column(String)
    ForestPublicPercent = Column(String)

class A10_1_9(Base):
    __tablename__ = 'A10_1_9'
    CountryCode = Column(String, primary_key=True)
    MoU = Column(String)
    Associate = Column(String)
    NonMember = Column(String)
    GBIFDetails = Column(String)
    GBIFLink = Column(String)
    Gov = Column(String)
    Public = Column(String)
    NotMember = Column(String)
    ENBIDetails = Column(String)

class B1_1_1(Base):
    __tablename__ = 'B1_1_1'
    CountryCode = Column(String, primary_key=True)
    NatProg = Column(String)
    NatProgDetails = Column(String)
    NatProgData = Column(String)
    Mange2004 = Column(String)
    Restore2004 = Column(String)
    Other2004 = Column(String)
    Mange2005 = Column(String)
    Restore2005 = Column(String)
    Other2005 = Column(String)
    Mange2006 = Column(String)
    Restore2006 = Column(String)
    Other2006 = Column(String)
    Mange2007 = Column(String)
    Restore2007 = Column(String)
    Other2007 = Column(String)
    Mange2008 = Column(String)
    Restore2008 = Column(String)
    Other2008 = Column(String)

class B1_1_4(Base):
    __tablename__ = 'B1_1_4'
    CountryCode = Column(String, primary_key=True)
    Cat51_2006 = Column(String)
    Cat51_2007 = Column(String)
    Cat51_2008 = Column(String)
    Cat51_2009 = Column(String)
    Cat55_2006 = Column(String)
    Cat55_2007 = Column(String)
    Cat55_2008 = Column(String)
    Cat55_2009 = Column(String)
    Cat56_2006 = Column(String)
    Cat56_2007 = Column(String)
    Cat56_2008 = Column(String)
    Cat56_2009 = Column(String)

class B1_1_8(Base):
    __tablename__ = 'B1_1_8'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

class B2_4(Base):
    __tablename__ = 'B2_4'
    CountryCode = Column(String, primary_key=True)
    New = Column(String)
    Existing = Column(String)
    Develope = Column(String)
    NoNew = Column(String)
    Details = Column(String)

class B3_1_2(Base):
    __tablename__ = 'B3_1_2'
    CountryCode = Column(String, primary_key=True)
    Local = Column(String)
    Regional = Column(String)
    National = Column(String)

class B3_1_5(Base):
    __tablename__ = 'B3_1_5'
    CountryCode = Column(String, primary_key=True)
    Local = Column(String)
    Regional = Column(String)
    National = Column(String)

class B3_1_6(Base):
    __tablename__ = 'B3_1_6'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

class B3_1_7(Base):
    __tablename__ = 'B3_1_7'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

class B3_1_8(Base):
    __tablename__ = 'B3_1_8'
    CountryCode = Column(String, primary_key=True)
    EU = Column(String)
    NonEU = Column(String)

class B4_1_1(Base):
    __tablename__ = 'B4_1_1'
    CountryCode = Column(String, primary_key=True)
    Yes = Column(String)
    No = Column(String)
    Dev = Column(String)
    NotYet = Column(String)
    Partially = Column(String)
    Fully = Column(String)

class B4_1_2(Base):
    __tablename__ = 'B4_1_2'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Declaration = Column(String)

class C1_2(Base):
    __tablename__ = 'C1_2'
    CountryCode = Column(String, primary_key=True)
    SEBI = Column(String)

class C1_2_1(Base):
    __tablename__ = 'C1_2_1'
    CountryCode = Column(String, primary_key=True)
    Abundance = Column(String)
    RedList = Column(String)
    Species = Column(String)
    Ecosystem = Column(String)
    Habitat = Column(String)
    Livestock = Column(String)
    Areas = Column(String)
    BirdSites = Column(String)
    Nitrogen = Column(String)
    Aliens = Column(String)
    BirdClimate = Column(String)
    MarineTrophic = Column(String)
    FragArea = Column(String)
    FragRicer = Column(String)
    NutrientCostal = Column(String)
    FWQuality = Column(String)
    ForestGrow = Column(String)
    ForestDead = Column(String)
    AgriNitro = Column(String)
    AgriAreas = Column(String)
    Fisheries = Column(String)
    Aquaculture = Column(String)
    Footprint = Column(String)
    Patent = Column(String)
    Finance = Column(String)
    Public = Column(String)
    Additional = Column(String)

class C1_3(Base):
    __tablename__ = 'C1_3'
    CountryCode = Column(String, primary_key=True)
    Costal = Column(String)
    Dunes = Column(String)
    FWHabitats = Column(String)
    Heath = Column(String)
    Scrub = Column(String)
    Grass = Column(String)
    Bogs = Column(String)
    Rocky = Column(String)
    Forest = Column(String)
    HabitatOther = Column(String)
    Birds = Column(String)
    Mammals = Column(String)
    Amphibians = Column(String)
    Fish = Column(String)
    Inverts = Column(String)
    Plants = Column(String)
    SpeciesOther = Column(String)
    CostalDetail = Column(String)
    DunesDetail = Column(String)
    FWHabitatsDetail = Column(String)
    HeathDetail = Column(String)
    ScrubDetail = Column(String)
    GrassDetail = Column(String)
    BogsDetail = Column(String)
    RockyDetail = Column(String)
    ForestDetail = Column(String)
    HabitatOtherDetail = Column(String)
    BirdsDetail = Column(String)
    MammalsDetail = Column(String)
    AmphibiansDetail = Column(String)
    FishDetail = Column(String)
    InvertsDetail = Column(String)
    PlantsDetail = Column(String)
    SpeciesOtherDetail = Column(String)
