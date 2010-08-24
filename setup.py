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

from setuptools import setup, find_packages

w_long_description = """\
BAP Application
"""

VERSION='0.1'

setup(name='edw_bap',
      author='Eau de Web',
      author_email='office@eaudeweb.ro',
      description='BAP Application',
      version=VERSION,
      download_url='http://naaya.eaudeweb.ro/eggshop/watsan.portal-'+VERSION+'.zip',
      url='http://watsan.edw.ro/',
      long_description=w_long_description,
      zip_safe=False,
      packages=find_packages(exclude='tests'),
      include_package_data=True,
      package_data={'':['*.*']},
      license='Python',
      platforms=['all',],
      install_requires=[],
)
