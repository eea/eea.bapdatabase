# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s):
# Cristian Romanescu, Eau De Web
from OFS.Folder import Folder
from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import InitializeClass
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from z3c.sqlalchemy.util import registeredWrappers, createSAWrapper

from Products.BAP.sql import query
from Products.BAP.paginate import DiggPaginator
from Products.BAP.utils import paginate_items

manage_add_html = PageTemplateFile('zpt/admin/manage_add_html', globals())
def manage_add_BAP(parent, id, REQUEST=None):
    """ Create new BAP object from ZMI.
    """
    parent._setObject(id, BAP(id, 'BAP application - %s' % id, 'en'))
    ob = parent._getOb(id)
    if REQUEST:
        ob.db_host = REQUEST.get('db_host', None)
        ob.db_port = REQUEST.get('db_port', None)
        ob.db_username = REQUEST.get('db_username', None)
        ob.db_password = REQUEST.get('db_password', None)
        ob.db_name = REQUEST.get('db_name', None)
        return parent.manage_main(parent, REQUEST, update_menu=1)
    
    return ob


class BAP(Folder):
    """
        BAP object, folder-type that contains items described within specs.
        This is the root of the application.
    """
    meta_type = 'BAP Application'
    security = ClassSecurityInfo()

    db_host = None
    db_port = None
    db_username = None
    db_password = None
    db_name = None
    db_debug = True


    def __init__(self, id, title, lang):
        """
        Constructor that builds new BAP object.
        Parameters:
        """
        super(BAP, self).__init__(id)

    security.declarePrivate('loadDefaultData')
    def loadDefaultData(self, *args, **kwargs):
        """ Load the initial data into a new created object
        """
        pass


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

    ##### VIEWS #####


    _index_html = PageTemplateFile('zpt/index_html', globals())
    def index_html(self, REQUEST):
        """ Main product page
        """
        return self._index_html(REQUEST)


    _country_html = PageTemplateFile('zpt/views/country_html', globals())
    def country(self, REQUEST):
        """ List of countries
        """
        session = self.get_db_session()
        items = query.list_country(session)
        items = paginate_items(items, 20, REQUEST)
        return self._country_html(REQUEST, page=items)

    _actionsnarrative_html = PageTemplateFile('zpt/views/actionsnarrative_html', globals())
    def actionsnarrative(self, REQUEST):
        """ Query - actionsnarrative
        """
        session = self.get_db_session()
        items = query.list_actionsnarrative(session)
        items = paginate_items(items, 20, REQUEST)
        return self._actionsnarrative_html(REQUEST, page=items)

    ##### END VIEWS #####

    template_tpl = PageTemplateFile('zpt/template_tpl', globals())
    paginator = PageTemplateFile('zpt/paginator_inc', globals())
    navigator = PageTemplateFile('zpt/navigator_inc', globals())

InitializeClass(BAP)