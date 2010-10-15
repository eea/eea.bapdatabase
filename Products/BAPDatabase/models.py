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

class A1_2_3(Base):
    __tablename__ = 'A1_2_3'
    
    CountryCode = Column(String, primary_key=True)
    ToolInPlace = Column(String)
    ToolInDev = Column(String)

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

class A2_1_3_ForestCert(Base):
    __tablename__ = 'A2_1_3_ForestCert'
    CountryCode = Column(String, primary_key=True)
    FSCArea = Column(String)
    FSCPercent = Column(String)
    PECFArea = Column(String)
    PECFPercent = Column(String)
    OtherCert = Column(String)
    OtherCertArea = Column(String)
    OtherCertPercent = Column(String)

class A2_1_3_HNV(Base):
    __tablename__ = 'A2_1_3_HNV'
    CountryCode = Column(String, primary_key=True)
    Area = Column(String)
    Share = Column(String)
    NoMapped = Column(String)
    Mapped = Column(String)

class A2_1_4(Base):
    __tablename__ = 'A2_1_4'
    CountryCode = Column(String, primary_key=True)
    Livestock = Column(String)
    Pasture = Column(String)
    Landscape = Column(String)
    Habitat = Column(String)
    GAEC = Column(String)
    GAECDetails = Column(String)

class A2_1_6(Base):
    __tablename__ = 'A2_1_6'
    CountryCode = Column(String, primary_key=True)
    Training = Column(String)
    TrainingAmount = Column(String)
    TrainingPercent = Column(String)

class A6_1_1(Base):
    __tablename__ = 'A6_1_1'
    CountryCode = Column(String, primary_key=True)
    NationalReport4 = Column(String)
    NBSAP = Column(String)
    NBSAPData = Column(String)
    CBDYear = Column(String)
    CBDAmount = Column(String)
    CMSYear = Column(String)
    CMSAmount = Column(String)
    AEWAYear = Column(String)
    AEWAAmount = Column(String)
    RamsarYear = Column(String)
    RamsarAmount = Column(String)
    WHCYear = Column(String)
    WHCAmount = Column(String)
    ConventionData = Column(String)

class A7_1(Base):
    __tablename__ = 'A7_1'
    CountryCode = Column(String, primary_key=True)
    Aid2006 = Column(String)
    Aid2007 = Column(String)
    Aid2008 = Column(String)
    Percent2006 = Column(String)
    Percent2007 = Column(String)
    Percent2008 = Column(String)


class A7_1_3(Base):
    __tablename__ = 'A7_1_3'
    CountryCode = Column(String, primary_key=True)
    BiAid2006 = Column(String)
    BiAid2007 = Column(String)
    BiAid2008 = Column(String)
    BiPercent2006 = Column(String)
    BiPercent2007 = Column(String)
    BiPercent2008 = Column(String)


class A7_1_4(Base):
    __tablename__ = 'A7_1_4'
    CountryCode = Column(String, primary_key=True)
    Total3rd = Column(String)
    Total4th = Column(String)
    Total5th = Column(String)
    Percent3rd = Column(String)
    Percent4th = Column(String)
    Percent5th = Column(String)

class A7_2_2(Base):
    __tablename__ = 'A7_2_2'
    CountryCode = Column(String, primary_key=True)
    MandatorySEA_EIA = Column(String)

class A8_1(Base):
    __tablename__ = 'A8_1'
    CountryCode = Column(String, primary_key=True)
    A8_1_3Imp = Column(String)
    A8_1_3Partial = Column(String)
    A8_1_3Not = Column(String)
    A8_1_4Imp = Column(String)
    A8_1_4Partial = Column(String)
    A8_1_4Not = Column(String)
    A8_1_8Imp = Column(String)
    A8_1_8Partial = Column(String)
    A8_1_8Not = Column(String)

class A8_1_3_BenefitShare(Base):
    __tablename__ = 'A8_1_3_BenefitShare'
    CountryCode = Column(String, primary_key=True)
    Legal = Column(String)
    Aware = Column(String)

class A8_1_3_CBD(Base):
    __tablename__ = 'A8_1_3_CBD'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

class A8_1_3_GeneticResource(Base):
    __tablename__ = 'A8_1_3_GeneticResource'
    CountryCode = Column(String, primary_key=True)
    Legal = Column(String)
    Aware = Column(String)

class A8_1_4(Base):
    __tablename__ = 'A8_1_4'
    CountryCode = Column(String, primary_key=True)
    Y2006 = Column(String)
    Y2007 = Column(String)
    Y2008 = Column(String)
    Y2009 = Column(String)

class A8_1_8(Base):
    __tablename__ = 'A8_1_8'
    CountryCode = Column(String, primary_key=True)
    ImportApps = Column(String)
    ImportAppsDenied = Column(String)
    ImportPercent = Column(String)
    ExportApps = Column(String)
    ExportAppsDenied = Column(String)
    ExportPercent = Column(String)
    ReExportApps = Column(String)
    ReExportAppsDenied = Column(String)
    ReExportPercent = Column(String)
    SeizeP1Year = Column(String)
    SeizeP1Num = Column(String)
    SeizeP2Year = Column(String)
    SeizeP2Num = Column(String)
    NetChange = Column(String)
    Capacity = Column(String)
    Finance = Column(String)
    CITESDataLink = Column(String)
    Contributions = Column(String)
    Amount = Column(String)
    CITES_COPDataLink = Column(String)

class A9_1_1(Base):
    __tablename__ = 'A9_1_1'
    CountryCode = Column(String, primary_key=True)
    GHG2006 = Column(String)
    GHG2007 = Column(String)
    GHG2008 = Column(String)
    Change2006 = Column(String)
    Change2007 = Column(String)
    Change2008 = Column(String)

class A9_3_2(Base):
    __tablename__ = 'A9_3_2'
    CountryCode = Column(String, primary_key=True)
    PlanNo = Column(String)
    PlanDev = Column(String)
    PlanImp = Column(String)
    PlanDontKnow = Column(String)
    NREAPNo = Column(String)
    NREAPDev = Column(String)
    NREAPImp = Column(String)
    NREAPDontKnow = Column(String)
    Round = Column(String)
    NatCert = Column(String)
    OtherDesc = Column(String)
    OtherNat = Column(String)
    Require = Column(String)
    RequireDetail = Column(String)

class A9_4_1(Base):
    __tablename__ = 'A9_4_1'
    CountryCode = Column(String, primary_key=True)
    StratNo = Column(String)
    StratDev = Column(String)
    StratImp = Column(String)
    StratDontKnow = Column(String)
    PlanNo = Column(String)
    PlanDev = Column(String)
    PlanImp = Column(String)
    PlanDontKnow = Column(String)
    OtherDesc = Column(String)
    OtherNo = Column(String)
    OtherDev = Column(String)
    OtherImp = Column(String)
    OtherDontKnow = Column(String)
    AdaptStratYN = Column(String)
    AdaptStratDetail = Column(String)
    AdaptPlanYN = Column(String)
    AdaptPlanDetail = Column(String)
    BioStratYN = Column(String)
    BioStratDetail = Column(String)
    BioPlanYN = Column(String)
    BioPlanDetail = Column(String)
    ProjectsYN = Column(String)
    ProjectsDetail = Column(String)

class A9_4_3(Base):
    __tablename__ = 'A9_4_3'
    CountryCode = Column(String, primary_key=True)
    StudiesYN = Column(String)
    StudiesDetail = Column(String)
    HabitatYN = Column(String)
    HabitatDetail = Column(String)
    SpeciesYN = Column(String)
    SpeciesDetail = Column(String)

class A10_1(Base):
    __tablename__ = 'A10_1'
    CountryCode = Column(String, primary_key=True)
    Programme = Column(String)
    ProgrammeDetail = Column(String)
    Research = Column(String)
    ResearchDetail = Column(String)

class A10_1_2(Base):
    __tablename__ = 'A10_1_2'
    CountryCode = Column(String, primary_key=True)
    NatFollow = Column(String)
    WideFollow = Column(String)
    FollowDetails = Column(String)
    Local = Column(String)
    SubNat = Column(String)
    Nat = Column(String)
    Stakeholder = Column(String)
    Valuation = Column(String)
    CaseStudies = Column(String)
    Access = Column(String)
    Standards = Column(String)
    MAInPlans = Column(String)
    ValuationUsed = Column(String)

class A10_1_8(Base):
    __tablename__ = 'A10_1_8'
    CountryCode = Column(String, primary_key=True)
    Platform = Column(String)
    PlatfromUpdated = Column(String)
    PlatfromDevPlans = Column(String)
    PlatfromLink = Column(String)

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
