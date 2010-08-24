'''
Created on Aug 23, 2010

@author: cristiroma
'''
from sqlalchemy.schema import Table, MetaData, Column, ForeignKey
from sqlalchemy.types import String
from sqlalchemy.orm import mapper

metadata = MetaData()

t_01header = Table('01header', metadata,
        Column('Country', String),
        Column('CountryCode', String, primary_key=True), 
        Column('PrefilledName', String),
        Column('PrefilledVerifiedCOName', String),
        Column('PrefilledVerifiedCODate', String),
        Column('PrefilledVerifiedECName', String),
        Column('PrefilledVerifiedECDate', String),
        Column('DataEntryMSName', String),
        Column('DataEntryCOName', String),
        Column('VerifiedMSName', String),
        Column('VerifiedMSDate', String),
        Column('VerifiedCOName', String),
        Column('VerifiedCODate', String),
        Column('VerifiedECName', String),
        Column('VerifiedECDate', String),
)

class T01Header(object):
    """ Mapping for table
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

mapper(T01Header, t_01header)



t_narrative = Table('narrative', metadata,
        Column('Country', String, ForeignKey(T01Header.CountryCode), primary_key=True), 
        Column('Objective', String),
        Column('Ident', String),
        Column('MOP', String),
        Column('Narative', String),
        Column('MSComments', String),
        Column('Clarifcations', String),
        Column('DataSource', String),
        Column('MSVerrified', String),
        Column('EC1Verrified', String),
        Column('EC2Verrified', String),
        Column('CO1Verrified', String),
        Column('CO2Verrified', String),
)

class TNarrative(object):
    """ Mapping for table
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

mapper(TNarrative, t_narrative)



t_questionstext = Table('questionstext', metadata,
        Column('ID', String, primary_key=True), 
        Column('Ident', String, ForeignKey(TNarrative.Ident)),
        Column('MOP', String),
        Column('Action', String),
        Column('MSAction', String),
        Column('FullText', String),
        Column('MOPText', String),
)

class TQuestionsText(object):
    """ Mapping for table
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

mapper(TQuestionsText, t_questionstext)

