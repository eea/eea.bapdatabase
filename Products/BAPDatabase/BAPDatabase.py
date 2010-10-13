import re
from z3c.sqlalchemy.util import registeredWrappers, createSAWrapper
from sqlalchemy.orm.exc import NoResultFound

from App.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import view_management_screens, view
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.NaayaCore.FormsTool.NaayaTemplate import NaayaPageTemplateFile
from Products.Naaya.NyFolder import NyFolder, addNyFolder

import models
import utilities

pattern = re.compile(r'^(?P<heading>[a-zA-Z\s]+\:?(\s*\w[\s\d\.]+)?)(?P<text>.*)$', re.DOTALL)

country_codes = {'Austria': 'AT'}

tables = {
            'A1_3': NaayaPageTemplateFile('zpt/A1_3', globals(), 'products.bapdatabase.tables.A1_3'),
            'A1_3_1': NaayaPageTemplateFile('zpt/A1_3_1', globals(), 'products.bapdatabase.tables.A1_3_1'),
            'A2_1_1': NaayaPageTemplateFile('zpt/A2_1_1', globals(), 'products.bapdatabase.tables.A2_1_1')
        }


def create_object_callback(parent, id, contributor):
    ob = BAPDatabase(id, contributor)
    parent._setObject(id, ob)
    ob = parent._getOb(id)
    return ob

manage_add_html = PageTemplateFile('zpt/manage_add', globals())
def manage_add_bap(self, id, REQUEST=None, **kwargs):
    """ Create new BAPDatabase object from ZMI.
    """
    id = addNyFolder(self, id, callback=create_object_callback)
    ob = self._getOb(id)
    if REQUEST is not None:
        params = dict(REQUEST.form)
    else:
        params = kwargs
    ob.db_host = params.pop('db_host', None)
    ob.db_port = params.pop('db_port', None)
    ob.db_username = params.pop('db_username', None)
    ob.db_password = params.pop('db_password', None)
    ob.db_name = params.pop('db_name', None)
    if REQUEST is not None:
        return self.manage_main(self, REQUEST, update_menu=1)
    return ob


class BAPDatabase(NyFolder):
    """
        BAPDatabase object, folder-type that contains items described within specs.
        This is the root of the application.
    """
    meta_type = 'BAPDatabase'
    security = ClassSecurityInfo()

    db_host = None
    db_port = None
    db_username = None
    db_password = None
    db_name = None
    db_debug = False

    def _get_schema(self):
        from Products.NaayaCore.constants import ID_SCHEMATOOL
        return self.getSite()._getOb(ID_SCHEMATOOL).getSchemaForMetatype('Naaya Folder')

    def __init__(self, id, contributor):
        """
            Constructor that builds new BAPDatabase object.
        """
        super(BAPDatabase, self).__init__(id, contributor)

    def _get_session(self):
        """ Create a Z3C.SQLAlchemy registered wrapper """
        if self.db_name in registeredWrappers.keys():
            wrapper = registeredWrappers[self.db_name]
        else:
            wrapper = createSAWrapper('mysql://%s:%s@%s:%d/%s?charset=utf8&use_unicode=0' \
                                      % (self.db_username, self.db_password, self.db_host, int(self.db_port), self.db_name),
                                      name=self.db_name,
                                      engine_options = {'echo' : self.db_debug})
        return wrapper.session

    def _delete_wrapper(self):
        """
            Delete the Z3C.SQLAlchemy registered wrapper
        """
        if self.db_name in registeredWrappers.keys():
            del registeredWrappers[self.db_name]
            self._p_changed = 1

    #database queries
    def get_headline(self, objective):
        result = self._get_session().query(models.QuestionsText.FullText).\
                                    filter(models.QuestionsText.Ident == objective).all()
        if result:
            return result[0][0]    #take the first headline
        return ''

    def humanize_text(self, text, id):
        m = pattern.match(text)
        if m is not None:
            return '<a href="%(url)s">%(heading)s</a> %(text)s' % {
                'url': '%s/details?id=%s' % (self.REQUEST.ACTUAL_URL, id),
                'heading': m.group('heading').strip(),
                'text': m.group('text').strip(),
            }
        return text

    def get_objectives(self):
        return self._get_session().query(models.Objective).all()

    def get_action_mop(self, id, country):
        try:
            return self._get_session().query(models.Narrative) \
                                .filter(models.Narrative.Ident == id) \
                                .filter(models.Narrative.Country == country).one()
        except NoResultFound:
            return

    def get_action(self, id):
        action = self._get_session().query(models.QuestionsText) \
                                .filter(models.QuestionsText.Ident == id).all()
        if action:
            return action[0]    #texts are simlar
        return ''

    def get_targets(self, objective, country):
        result = {}
        for target in self._get_session().query(models.QuestionsText) \
                        .join((models.Narrative, models.QuestionsText.Ident == models.Narrative.Ident)) \
                        .filter(models.Narrative.Country == country) \
                        .filter(models.Narrative.Objective == objective).all():
            if target.Ident != objective:   #skip headlines
                result[target.Ident] = target
            
        return [result[k] for k in sorted(result)]

    def get_action_values(self, action, country):
        code = country_codes.get(country)
        model = getattr(models, action)
        try:
            return self._get_session().query(model) \
                                    .filter(model.CountryCode == code).one()
        except NoResultFound:
            return

    def get_table(self, action, mop, country):
        template = tables.get(action.Ident)
        return template.__of__(self)(mop=mop, country=country, action=action)

    index_html = NaayaPageTemplateFile('zpt/index', globals(), 'products.bapdatabase.index')
    details = NaayaPageTemplateFile('zpt/details', globals(), 'products.bapdatabase.details')

InitializeClass(BAPDatabase)