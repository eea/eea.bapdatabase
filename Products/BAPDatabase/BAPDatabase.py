from z3c.sqlalchemy.util import registeredWrappers, createSAWrapper

from App.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import view_management_screens, view
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.NaayaCore.FormsTool.NaayaTemplate import NaayaPageTemplateFile
from Products.Naaya.NyFolder import NyFolder, addNyFolder

import views

def create_object_callback(parent, id, contributor):
    ob = BAPDatabase(id, contributor)
    parent._setObject(id, ob)
    ob = parent._getOb(id)
    return ob

manage_add_html = PageTemplateFile('zpt/admin/manage_add_html', globals())
def manage_add(self, id, REQUEST=None):
    """ Create new BAPDatabase object from ZMI.
    """
    id = addNyFolder(self, id, callback=create_object_callback)
    ob = self._getOb(id)
    if REQUEST:
        ob.db_host = REQUEST.get('db_host', None)
        ob.db_port = REQUEST.get('db_port', None)
        ob.db_username = REQUEST.get('db_username', None)
        ob.db_password = REQUEST.get('db_password', None)
        ob.db_name = REQUEST.get('db_name', None)
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
    db_debug = True

    def _get_schema(self):
        from Products.NaayaCore.constants import ID_SCHEMATOOL
        return self.getSite()._getOb(ID_SCHEMATOOL).getSchemaForMetatype('Naaya Folder')

    def __init__(self, id, contributor):
        """
        Constructor that builds new BAPDatabase object.
        Parameters:
        """
        super(BAPDatabase, self).__init__(id, contributor)

    security.declarePrivate('get_db_session')
    def get_db_session(self):
        """
        Retrive managed database connection
        Return:
            SQLAlchemy database session
        """
        wrapper = None
        if self.db_name in registeredWrappers.keys():
            wrapper = registeredWrappers[self.db_name]
        else:
            wrapper = createSAWrapper('mysql://%s:%s@%s:%d/%s' \
                                      % (self.db_username, self.db_password, self.db_host, int(self.db_port), self.db_name),
                                      name=self.db_name,
                                      engine_options = {'echo' : self.db_debug, 'encoding' : 'utf-8'})
        return wrapper.session


    def _delete_wrapper(self):
        """
        Delete the Z3C.SQLAlchemy registered wrapper (created by get_db_session)
        """
        if self.db_name in registeredWrappers.keys():
            del registeredWrappers[self.db_name]
            self._p_changed = 1

    security.declareProtected(view, 'getCountryActions')
    def getCountryActions(self, objective):
        """ get country actions """
        session = self.get_db_session()
        country = self.aq_parent.title_or_id()
        return views.list_actionsnarrative(session, country, objective)
   
    _index = NaayaPageTemplateFile('zpt/index', globals(), 'products.bapdatabase.index')
    security.declareProtected(view, 'index_html')
    def index_html(self, REQUEST):
        """ Main product page
        """
        session = self.get_db_session()
        return self._index(REQUEST, 
                        objectives = views.list_objectives(session))

InitializeClass(BAPDatabase)