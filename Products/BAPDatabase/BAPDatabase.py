import re
from copy import deepcopy
from z3c.sqlalchemy.util import registeredWrappers, createSAWrapper
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import view_management_screens, view
from App.class_init import InitializeClass
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.NaayaCore.FormsTool.NaayaTemplate import NaayaPageTemplateFile
from Products.Naaya.NyFolder import NyFolder, addNyFolder
from sql import query

cp_1252_chars = {
    # from http://www.microsoft.com/typography/unicode/1252.htm
    u"\x80": u"\u20AC", # EURO SIGN
    u"\x82": u"\u201A", # SINGLE LOW-9 QUOTATION MARK
    u"\x83": u"\u0192", # LATIN SMALL LETTER F WITH HOOK
    u"\x84": u"\u201E", # DOUBLE LOW-9 QUOTATION MARK
    u"\x85": u"\u2026", # HORIZONTAL ELLIPSIS
    u"\x86": u"\u2020", # DAGGER
    u"\x87": u"\u2021", # DOUBLE DAGGER
    u"\x88": u"\u02C6", # MODIFIER LETTER CIRCUMFLEX ACCENT
    u"\x89": u"\u2030", # PER MILLE SIGN
    u"\x8A": u"\u0160", # LATIN CAPITAL LETTER S WITH CARON
    u"\x8B": u"\u2039", # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    u"\x8C": u"\u0152", # LATIN CAPITAL LIGATURE OE
    u"\x8E": u"\u017D", # LATIN CAPITAL LETTER Z WITH CARON
    u"\x91": u"\u2018", # LEFT SINGLE QUOTATION MARK
    u"\x92": u"\u2019", # RIGHT SINGLE QUOTATION MARK
    u"\x93": u"\u201C", # LEFT DOUBLE QUOTATION MARK
    u"\x94": u"\u201D", # RIGHT DOUBLE QUOTATION MARK
    u"\x95": u"\u2022", # BULLET
    u"\x96": u"\u2013", # EN DASH
    u"\x97": u"\u2014", # EM DASH
    u"\x98": u"\u02DC", # SMALL TILDE
    u"\x99": u"\u2122", # TRADE MARK SIGN
    u"\x9A": u"\u0161", # LATIN SMALL LETTER S WITH CARON
    u"\x9B": u"\u203A", # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    u"\x9C": u"\u0153", # LATIN SMALL LIGATURE OE
    u"\x9E": u"\u017E", # LATIN SMALL LETTER Z WITH CARON
    u"\x9F": u"\u0178", # LATIN CAPITAL LETTER Y WITH DIAERESIS
}

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
        return query.list_actionsnarrative(session, country, objective)

    security.declareProtected(view, 'fix_1252_codes')
    def fix_1252_codes(self, text):
        """
        Replace non-standard Microsoft character codes from the Windows-1252 character set in a unicode string with proper unicode codes.
        Code originally from: http://effbot.org/zone/unicode-gremlins.htm
        """
        if re.search(u"[\x80-\x9f]", text):
            def fixup(m):
                s = m.group(0)
                return cp_1252_chars.get(s, s)
            if isinstance(text, type("")):
                text = unicode(text, "iso-8859-1")
            text = re.sub(u"[\x80-\x9f]", fixup, text)
        return text

    ##### VIEWS #####

    _index = NaayaPageTemplateFile('zpt/index', globals(), 'products.bapdatabase.index')
    security.declareProtected(view, 'index_html')
    def index_html(self, REQUEST):
        """ Main product page
        """
        session = self.get_db_session()
        country = self.aq_parent.title_or_id()
        objectives = query.list_objectives(session, country)
        return self._index(REQUEST, objectives = objectives)

InitializeClass(BAPDatabase)