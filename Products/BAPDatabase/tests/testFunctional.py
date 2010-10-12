from unittest import TestSuite, makeSuite
from BeautifulSoup import BeautifulSoup
from Products.Naaya.tests.NaayaFunctionalTestCase import NaayaFunctionalTestCase

class BAPFunctionalTestCase(NaayaFunctionalTestCase):
    """ TestCase for BAP object """
    def afterSetUp(self):
        from Products.Naaya.NyFolder import addNyFolder
        from Products.BAPDatabase.BAPDatabase import manage_add
        addNyFolder(self.portal, 'countries', contributor='admin', submitted=1)
        #add a country
        addNyFolder(self.portal.countries, id='austria', title='Austria', contributor='admin', submitted=1)
        manage_add(self.portal, 
                    id = 'bap', 
                    db_host = 'localhost', 
                    db_port = '3306',
                    db_username = 'admin',
                    db_password = 'admin',
                    db_name='bap')
        import transaction; transaction.commit()

    def beforeTearDown(self):
        self.portal.manage_delObjects(['bap'])
        import transaction; transaction.commit()

    def test_connection(self):
        objectives = self.portal.bap.get_objectives()
        self.assertEqual(len(objectives), 15)

    def test_objectives(self):
        self.browser.go('http://localhost/portal/countries/austria/bap')
        html = self.browser.get_html()
        self.failUnless("Objective1: To safeguard the EU's most important habitats and species" in html)
        
        
        