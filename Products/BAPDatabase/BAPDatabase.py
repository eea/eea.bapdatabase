import re
import os
from os.path import join, dirname, splitext

try:
    import json
except ImportError:
    import simplejson as json

from z3c.sqlalchemy.util import registeredWrappers, createSAWrapper
from sqlalchemy.orm.exc import NoResultFound

from App.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import view_management_screens, view
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.Naaya.NyFolder import NyFolder, addNyFolder

import models

pattern = re.compile(r'^(?P<heading>[a-zA-Z\s]+\:?(\s*\w[\s\d\.]+)?)(?P<text>.*)$', re.DOTALL)
target_pattern = re.compile(r'^[A-Z]\d+\_\d+$', re.DOTALL)


tables = {}
for f in os.listdir(join(dirname(__file__), 'zpt')):
    if f.endswith('.zpt'):
        fname = splitext(f)[0]
        tables.setdefault(fname,
                            PageTemplateFile('zpt/%s' % fname, globals()))

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

from Products.NaayaCore.LayoutTool.DiskFile import allow_path
allow_path('Products.BAPDatabase:www/css/')


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


    def humanize_text(self, text):
        m = pattern.match(text)
        if m is not None:
            return m.group('heading').strip(), m.group('text').strip()
        return ['', '']

    def get_targets(self, objective, country):
        result = {}
        for target in self._get_session().query(models.TargetActions.Target, models.QuestionsText.FullText) \
                                .join((models.Narrative, models.Narrative.Ident == models.TargetActions.Target)) \
                                .join((models.QuestionsText, models.QuestionsText.Ident == models.TargetActions.Target)) \
                                .filter(models.Narrative.Country == country) \
                                .filter(models.Narrative.Objective == objective).distinct().all():
            result[target[0]] = target[1]
        return iter(sorted(result.iteritems()))

    def get_objective_targets(self, objective):
        result = {}
        for target in self._get_session().query(models.TargetActions.Target, models.QuestionsText.FullText) \
                                .join((models.Narrative, models.Narrative.Ident == models.TargetActions.Target)) \
                                .join((models.QuestionsText, models.QuestionsText.Ident == models.TargetActions.Target)) \
                                .filter(models.Narrative.Objective == objective).distinct().all():
            result[target[0]] = target[1]
        return iter(sorted(result.iteritems()))

    def get_actions(self, objective, target, country):
        result = {}
        for action in self._get_session().query(models.QuestionsText) \
                        .join((models.Narrative, models.QuestionsText.Ident == models.Narrative.Ident)) \
                        .filter(models.Narrative.Country == country) \
                        .filter(models.Narrative.Objective == objective) \
                        .filter(models.QuestionsText.Ident.like('%s%%' % target)).all():
            if action.Ident != target:   #skip targets
                result[action.Ident] = action

        return [result[k] for k in sorted(result)]

    def get_target_actions(self, objective, target):
        result = {}
        for action in self._get_session().query(models.QuestionsText) \
                        .join((models.Narrative, models.QuestionsText.Ident == models.Narrative.Ident)) \
                        .filter(models.Narrative.Objective == objective) \
                        .filter(models.QuestionsText.Ident.like('%s%%' % target)).all():
            if action.Ident != target:   #skip targets
                result[action.Ident] = action

        return [result[k] for k in sorted(result)]

    def get_country_code(self, country):
        return self._get_session().query(models.Header.CountryCode) \
                                .filter(models.Header.Country == country).one()[0]

    def get_action_mop(self, id, country, mop=''):
        try:
            return self._get_session().query(models.Narrative) \
                                .filter(models.Narrative.Ident == id) \
                                .filter(models.Narrative.MOP == mop) \
                                .filter(models.Narrative.Country == country).one()
        except NoResultFound:
            return

    def get_action(self, id, mop=None):
        try:
            return self._get_session().query(models.QuestionsText) \
                                    .filter(models.QuestionsText.Ident == id) \
                                    .filter(models.QuestionsText.MOP == mop).one()
        except NoResultFound:
            return

    def get_objective(self, id):
        try:
            return self._get_session().query(models.Objective) \
                                    .filter(models.Objective.id == id).one()
        except NoResultFound:
            return

    def get_action_values(self, table_id, country):
        try:
            code = self.get_country_code(country)
            model = getattr(models, table_id)
            return self._get_session().query(model) \
                                .filter(model.CountryCode == code).one()
        except NoResultFound:
            return None

    def get_table(self, action_id, country):
        template = tables.get(action_id)
        try:
            if template is not None:
                return template.__of__(self)(country=country, action_id=action_id)
        except:
            return self.empty_table.__of__(self)()

    def get_comparision_countries(self, ref_country):
        return [ c for c in self.get_countries() if c!=ref_country ]

    def get_countries(self):
        countries = self._get_session().query(models.Header.Country) \
                                        .order_by(models.Header.Country).all()
        return [ country[0] for country in countries if country ]

    def get_objectives(self):
        return self._get_session().query(models.Objective).all()

    def build_compare_details(self, text, id, is_first=False):
        parsed_text = self.humanize_text(text)
        if is_first:
            href_class = "action-link first-element"
        else:
            href_class = "action-link"
        if isinstance(parsed_text, tuple):
            return '<a class="%(href_class)s" title="Click to see details" href="#">%(heading)s</a> %(text)s' % {
                 'href_class': href_class,
                 'id': id,
                 'heading': parsed_text[0],
                 'text': parsed_text[1]
             }

    def json_objectives(self):
        """ """
        records = []
        for objective in self.get_objectives():
            records.append({'optionValue': objective.name,
                            'optionDisplay': objective.name,
                            'optionTitle': objective.headline})
        return json.dumps(records)

    def json_get_targets(self, objective, country):
        """ """
        records = []
        if country == 'Community report':
            objective = int(objective.split('Objective')[1])
            for target in self.cl_get_targets(objective):
                records.append({
                    'optionValue': target.id,
                    'optionDisplay': target.name,
                    'optionTitle': target.name,
                })
        else:
            for target in self.get_objective_targets(objective):
                records.append({'optionValue': target[0],
                                'optionDisplay': target[0],
                                'optionTitle': target[1]})
        return json.dumps(records)

    def json_get_comparision_countries(self, ref_country):
        """ """
        records = []
        for country in self.get_comparision_countries(ref_country):
            records.append({'optionValue': country,
                            'optionDisplay': country,
                            'optionTitle': country})
        return json.dumps(records)

    ################################
    #   Community report functions #
    ################################

    def cl_get_table(self, action_id, country):
        try:
            if country == 'Community report':
                text = "\n\n".join([mop.progress
                    for mop in self.cl_get_mops(action_id) if mop.progress])
                return self.compare_community_details.__of__(self)(text=text)
            else:
                try:
                    if str(int(action_id)) == action_id: #Is numeric
                        action_id = self.cl_get_action(action_id).name
                except ValueError:
                    pass
                action_id = action_id.replace('.', '_')
                template = tables.get(action_id)
                if template is not None:
                    return template.__of__(self)(country=country,
                            action_id=action_id)
        except:
            pass
        return self.empty_table.__of__(self)()

    def cl_get_objectives(self):
        """ Same as get_objectives, but will probably change in the future"""
        return self.get_objectives()

    def cl_get_objective(self, objective_id):
        """ Get objective """
        return self._get_session().query(models.Objective).\
                filter(models.Objective.id == objective_id).one()

    def cl_get_targets(self, objective):
        if isinstance(objective, basestring) and 'Objective' in objective:
            objective = objective.split('Objective')[1]
        return self._get_session().query(models.Target).filter(
                models.Target.objective == objective).all()

    def cl_get_target(self, target_id):
        """ Get target """
        return self._get_session().query(models.Target).\
                filter(models.Target.id == target_id).one()

    def cl_get_actions(self, target):
        """ Get actions for a cl_target """
        return self._get_session().query(models.Action).filter(
                models.Action.target == target).all()

    def cl_get_actions_combined(self, req_objective, req_target, req_country):
        """ Combine both types of action """

        actions = []
        for action in self.cl_get_actions(req_target):
            actions.append({
                'id': action.id,
                'text': action.action,
                'name': action.name
            })

        for action in self.get_actions(req_objective, req_target, req_country):
            actions.append({
                'id': action.Ident,
                'text': action.FullText,
                'name': action.Ident
            })
        return actions

    def cl_get_action(self, action_id):
        """ Get target """
        return self._get_session().query(models.Action).\
                filter(models.Action.id == action_id).one()

    def cl_get_mops(self, action_id):
        """ get measurements of progress """
        return self._get_session().query(models.ActionProgress).\
                filter(models.ActionProgress.action == action_id).\
                order_by(models.ActionProgress.year).all()

    index_html = PageTemplateFile('zpt/index', globals())
    details = PageTemplateFile('zpt/details', globals())
    objective = PageTemplateFile('zpt/objective', globals())

    compare = PageTemplateFile('zpt/compare', globals())
    compare_details = PageTemplateFile('zpt/compare_details', globals())

    compare_multiple = PageTemplateFile('zpt/compare_multiple', globals())
    compare_side_by_side = PageTemplateFile('zpt/compare_side_by_side', globals())
    compare_community_details = PageTemplateFile('zpt/compare_community_details', globals())


    cl_compare_multiple = PageTemplateFile('zpt/cl_compare_multiple', globals())
    cl_compare_side_by_side = PageTemplateFile('zpt/cl_compare_side_by_side', globals())
    empty_table = PageTemplateFile('zpt/empty_table', globals())

    community_report = PageTemplateFile('zpt/community_report', globals())
    community_objective = PageTemplateFile('zpt/community_objective', globals())
    community_target = PageTemplateFile('zpt/community_target', globals())
    community_action = PageTemplateFile('zpt/community_action', globals())

InitializeClass(BAPDatabase)