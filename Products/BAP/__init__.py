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

import transaction
import zLOG

import BAP

__doc__ = """This Zope product represents the BAP Application. See specifications for more details on this component"""
__version__ = '0.1'


def initialize(context):
    """ 
        Product initialization method
        @param context: Zope server context 
    """
    app = context._ProductContext__app

    try:
        context.registerClass(
            BAP.BAP,
            constructors = (
                BAP.manage_add_html,
                BAP.manage_add_BAP),
        )
    except:
        import sys, traceback, string
        type, val, tb = sys.exc_info()
        zLOG.LOG(__name__, zLOG.ERROR, 'An error occurred during product initialization. The BAP product will not be available', error = (type, val, tb), reraise=True)
        sys.stderr.write(string.join(traceback.format_exception(type, val, tb), ''))
        del type, val, tb
