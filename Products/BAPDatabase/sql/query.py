import mappings

#def list_country(session):
#    """ Retrieve the list of countries from table 01header
#    """
#    return session.query(mappings.T01Header).order_by('Country').all()
#
#

def list_objectives(session, country):
    """ SELECT DISTINCT Objective
        FROM narrative
        WHERE Country = $country
    """
    return session.query(mappings.TNarrative.Objective) \
                .filter(mappings.TNarrative.Country == country) \
                .distinct().all()

def list_actionsnarrative(session, country, objective):
    """ SELECT B.FullText, B.MOPText, A.Narative
        FROM narrative A
        LEFT JOIN questionstext B ON A.Ident = B.Ident
        WHERE B.FullText Is Not Null
        AND A.Country = $country
        AND A.Objective = $objective
    """
    return session.query(mappings.TNarrative.Country, mappings.TQuestionsText.ID, mappings.TNarrative.Objective,
                  mappings.TNarrative.Ident, mappings.TQuestionsText.FullText,
                  mappings.TQuestionsText.MOPText, mappings.TNarrative.Narative)\
        .join((mappings.TQuestionsText, mappings.TQuestionsText.Ident == mappings.TNarrative.Ident)) \
        .filter(mappings.TQuestionsText.FullText != None) \
        .filter(mappings.TNarrative.Country == country) \
        .filter(mappings.TNarrative.Objective == objective).all()
