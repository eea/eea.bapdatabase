'''
Created on Aug 23, 2010

@author: cristiroma
'''
from Products.BAP.sql import mappings

def list_country(session):
    """ Retrieve the list of countries from table 01header
    """
    return session.query(mappings.T01Header).order_by('Country').all()


def list_actionsnarrative(session):
    """ SELECT A.Country, B.ID, A.Objective, A.Ident, B.FullText, B.MOPText, A.Narative
        FROM narrative A
        LEFT JOIN questionstext B ON A.Ident = B.Ident
        WHERE B.FullText Is Not Null
        ORDER BY A.Country, B.ID;
    """
    return session.query(mappings.TNarrative.Country, mappings.TQuestionsText.ID, mappings.TNarrative.Objective, 
                  mappings.TNarrative.Ident, mappings.TQuestionsText.FullText,
                  mappings.TQuestionsText.MOPText, mappings.TNarrative.Narative).join((mappings.TQuestionsText, mappings.TQuestionsText.Ident == mappings.TNarrative.Ident)) \
        .filter(mappings.TQuestionsText.FullText != None) \
        .order_by(mappings.TNarrative.Country, mappings.TQuestionsText.ID)