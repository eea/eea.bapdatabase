import models

def list_objectives(session):
    return session.query(models.Objective).all()

def list_actionsnarrative(session, country, objective):
    return session.query(models.Narrative.Country, 
                        models.QuestionsText.ID, 
                        models.Narrative.Objective,
                        models.Narrative.Ident, 
                        models.QuestionsText.FullText,
                        models.QuestionsText.MOPText, 
                        models.Narrative.Narative)\
        .join((models.QuestionsText, models.QuestionsText.Ident == models.Narrative.Ident)) \
        .filter(models.QuestionsText.FullText != None) \
        .filter(models.Narrative.Country == country) \
        .filter(models.Narrative.Objective == objective).all()
