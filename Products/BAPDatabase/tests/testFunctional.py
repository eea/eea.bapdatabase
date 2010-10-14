from unittest import TestSuite, makeSuite
from BeautifulSoup import BeautifulSoup
from Products.Naaya.tests.NaayaFunctionalTestCase import NaayaFunctionalTestCase

class BAPFunctionalTestCase(NaayaFunctionalTestCase):
    """ TestCase for BAP object """
    def afterSetUp(self):
        from Products.Naaya.NyFolder import addNyFolder
        from Products.BAPDatabase.BAPDatabase import manage_add_bap
        addNyFolder(self.portal, 'countries', contributor='admin', submitted=1)
        #add a country
        addNyFolder(self.portal.countries, id='austria', title='Austria', contributor='admin', submitted=1)
        manage_add_bap(self.portal, 
                    id = 'bap', 
                    db_host = 'pivo.edw.ro', 
                    db_port = '3306',
                    db_username = 'bap',
                    db_password = 'bap',
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
        self.failUnless("Objective1:" in html)
    
    def test_headlines(self):
        self.browser.go('http://localhost/portal/countries/austria/bap')
        html = self.browser.get_html()
        self.failUnless("Headline Target" in html)
    
    def test_actions(self):
        self.browser.go('http://localhost/portal/countries/austria/bap')
        html = self.browser.get_html()
        self.failUnless("Target" in html)    

    def test_A1_1_3(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=A1_1_3')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Indicate the number of complaints/infringements (legal cases)')

        record = self.portal.bap.get_action_values('A1_1_3', country='Austria')
        self.assertTrue(hasattr(record, 'Y2004'))

    def test_A1_3_1(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=A1_3_1')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Indicate the number of action plans per species group')

        record = self.portal.bap.get_action_values('A1_3_1_ActionPlan', country='Austria')
        self.assertTrue(hasattr(record, 'BirdComp'))

    def test_A2_1_1(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=A2_1_1')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'EAFRD')

        record = self.portal.bap.get_action_values('A2_1_1', country='Austria')
        self.assertTrue(hasattr(record, 'EAFRDTotal'))

    def test_A10_1_9(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_A10_1_9')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Please indicate level of participation in the Global Biodiversity Information Facility (GBIF). Please select only ONE of the following:')
        record = self.portal.bap.get_action_values('test_A10_1_9', country='Austria')
        self.assertTrue(hasattr(record, 'MoU'))

    def test_B1_1_1(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B1_1_1')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Does a national programme identifying long-term goals and the allocation of funding (both COM and MS co-funding) for the related biodiversity activities exist? If present indicate Y, if absent indicate N')
        record = self.portal.bap.get_action_values('test_B1_1_1', country='Austria')
        self.assertTrue(hasattr(record, 'NatProg'))

    def test_B1_1_4(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B1_1_4')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, "Indicate cohesion and structural funds for projects directly or indirectly providing biodiversity benefits in all MS' operational programmes (in EUR)")
        record = self.portal.bap.get_action_values('test_B1_1_4', country='Austria')
        self.assertTrue(hasattr(record, 'Cat51_2006'))

    def test_B1_1_8(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B1_1_8')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Please indicate amount of national funding allocated for European and national biodiversity research activities and programmes for the years indicated.')
        record = self.portal.bap.get_action_values('test_B1_1_8', country='Austria')
        self.assertTrue(hasattr(record, 'Y2006'))

    def test_B2_4(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B2_4')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Has a new national environmental policy or strategy been created, or an existing policy or strategy updated, in light of the Communication 'Halting the loss of biodiversity by 2010 and beyond'? Please indicate Y or N in each case.')
        record = self.portal.bap.get_action_values('test_B2_4', country='Austria')
        self.assertTrue(hasattr(record, 'New'))

    def test_B3_1_2(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B3_1_2')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'How many farming and biodiversity, forestry and biodiversity partnerships have been facilitated by MS at the local, regional and national levels? Please indicate number of partnerships in the following table:')
        record = self.portal.bap.get_action_values('test_B3_1_2', country='Austria')
        self.assertTrue(hasattr(record, 'Local'))

    def test_B3_1_5(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B3_1_5')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Does MS have a forum or similar platform/framework set up for biodiversity and planning partnership at local, regional, national levels? Please indicate Y/N against each box')
        record = self.portal.bap.get_action_values('test_B3_1_5', country='Austria')
        self.assertTrue(hasattr(record, 'Local'))

    def test_B3_1_6(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B3_1_6')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'How many forums or similar platforms/frameworks have been set up by MS to encourage business biodiversity partnerships? Please indicate number of forums/partnerships in the following table:')
        record = self.portal.bap.get_action_values('test_B3_1_6', country='Austria')
        self.assertTrue(hasattr(record, 'Y2006'))

    def test_B3_1_7(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B3_1_7')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'How many forums or similar platform/framework set up to encourage partnerships between financing sector and biodiversity? Please indicate number of forums or similar platforms/frameworks in the following table:')
        record = self.portal.bap.get_action_values('test_B3_1_7', country='Austria')
        self.assertTrue(hasattr(record, 'Y2006'))

    def test_B3_1_8(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=test_B3_1_8')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Have the CBD Akwe-Kwon Guidelines been applied to projects financed by public funds? Please indicate Y/N against each box:')
        record = self.portal.bap.get_action_values('test_B3_1_8', country='EU')
        self.assertTrue(hasattr(record, 'Yes'))

    def test_B4_1_1(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=B4_1_1')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Has a communications campaign in support of the EU Biodiversity Action Plan (BAP) been developed at the national level?Please tick only one of the following')
        record = self.portal.bap.get_action_values('B4_1_1', country='Austria')
        self.assertTrue(hasattr(record, 'Yes'))

    def test_B4_1_2(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=B4_1_2')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'What is the amount of funding by the MS for the supporting the 2010 countdown initiative?Please indicate amounts (in EUR):')
        record = self.portal.bap.get_action_values('B4_1_2', country='Austria')
        self.assertTrue(hasattr(record, 'Y2006'))

    def test_C1_2(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=C1_2')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Indicate the extent to which the full suite of SEBI and national indicators is developed and applied:')
        record = self.portal.bap.get_action_values('C1_2', country='Austria')
        self.assertTrue(hasattr(record, 'SEBI'))

    def test_C1_2_1(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=C1_2_1')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Indicate national/sub-national biodiversity indicators')
        record = self.portal.bap.get_action_values('C1_2_1', country='Austria')
        self.assertTrue(hasattr(record, 'Abundance'))

    def test_C1_3(self):
        self.browser.go('http://localhost/portal/countries/austria/bap/details?id=C1_3')
        html = self.browser.get_html()
        soup = BeautifulSoup(html)
        datatable = soup.find('table', attrs={'class':'datatable'})
        self.assertEqual(datatable.tr.th.text, 'Indicate national/sub-national biodiversity monitoring schemes for habitats')
        record = self.portal.bap.get_action_values('C1_3', country='Austria')
        self.assertTrue(hasattr(record, 'Costal'))
