import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())
    import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    
     def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

     def test_addressDew(self):
        "Location testing"
        #Uses both Custom Dewberry regex is DewLocEnt and built in location recognizer 

        #two positive test cases. 
        #NCAT address.
        res = analyze_text('1601 E Market St, Greensboro, NC 27411')
        self.assertIn('LOCATION', str(res))
        self.assertIn('DewLocEnt', str(res))

        #UNCG address. 
        res = analyze_text('1400 Spring Garden St, Greensboro, NC 27412')
        self.assertIn('LOCATION', str(res))
        self.assertIn('DewLocEnt', str(res))


        #In-built locator has a clear error and failure in how it's setup.
        #Brazil in the 1900s is NOT a real location, and should logically not be flagged as such.
        res = analyze_text('Brazil in the 1900s')
        #this assertIn statment SHOULD fail
        self.assertIn('LOCATION', str(res))
        #default fails, mine works. 
        self.assertNotIn('DewLoCEnt', str(res))
        