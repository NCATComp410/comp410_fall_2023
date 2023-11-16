import unittest
from pii_scan import show_aggie_pride, analyze_text


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_marital_status_detect(self):
        """Testing for Marital Status"""
        # Positive Test Cases - 1
        self.assertEqual("3", "3")
        results = analyze_text('We are married!')
        print(results)
        self.assertIn('MARITALSTATS', str(results))

        # # Positive Test Cases - 2
        results = analyze_text('divorced')
        print(results)
        self.assertIn('MARITALSTATS', str(results))

        # # Negative Test Case
        results = analyze_text('M@rried!')
        print(results)
        self.assertNotIn('MARITALSTATS', str(results))

    def test_addressDew(self):
        """Location testing"""
        # Uses both Custom Dewberry regex is DewLocEnt and built in location recognizer

        # two positive test cases.
        # NCAT address.
        res = analyze_text('1601 E Market St, Greensboro, NC 27411')
        self.assertIn('LOCATION', str(res))
        self.assertIn('DewLocEnt', str(res))

        # UNCG address.
        res = analyze_text('1400 Spring Garden St, Greensboro, NC 27412')
        self.assertIn('LOCATION', str(res))
        self.assertIn('DewLocEnt', str(res))

        # In-built locator has a clear error and failure in how it's setup.
        # Brazil in the 1900s is NOT a real location, and should logically not be flagged as such.
        res = analyze_text('Brazil in the 1900s')
        # this assertIn statment SHOULD fail
        self.assertIn('LOCATION', str(res))
        # default fails, mine works.
        self.assertNotIn('DewLoCEnt', str(res))

    def test_Interests(self):
        """Test to make sure the Aggie Pride function works"""

        results = analyze_text('I like Bibleman, but I do not like Chris Chan')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('I love Bitches.')
        self.assertIn('INTEREST', str(results))

        results = analyze_text('I don\'t like Mondays')
        self.assertNotIn('INTEREST', str(results))

    def test_mac_detect(self):
        """Testing for MAC Address"""
        # Positive Test Cases - 1
        results = analyze_text(
            'The device with the MAC address 52:34:56:78:9a:bc successfully connected to the network.')
        print(results)
        self.assertIn('MAC_ADDRESS', str(results))

        # Positive Test Cases - 2
        results = analyze_text(
            'The device with the MAC address 52-34-56-78-9A-BC successfully connected to the network.')
        print(results)
        self.assertIn('MAC_ADDRESS', str(results))

        # Negative Test Case
        results = analyze_text(
            'The device with the MAC address 52:341:56:78:9q:BC successfully connected to the network.')
        print(results)
        self.assertNotIn('MAC_ADDRESS', str(results))
        
    def test_ncdriversLicense(self):
        # Positive Test Case 1
        res = analyze_text('111111111111')
        self.assertIn('NCDL', str(res))

        # Negative test Case because of the dots
        res = analyze_text('1234.5678.9012')
        self.assertNotIn('NCDL', str(res))

        # Negative Test Case because it is 13 digits
        res = analyze_text('1234567890123')
        self.assertNotIn('NCDL', str(res))

#NEEDED IN requirements.txt
# face_recognition 
# Pillow


#NEEDED IN pii_scan.py 
# from PIL import Image 
# import face_recognition

# image = face_recognition.load_image_file("test.jpg")  
# image2 = face_recognition.load_image_file("noface.jpg") 
# image3 = face_recognition.load_image_file("otherdude.jpg")  

# def analyze_image(image) 
#   face_location = face_recognition.face_locations(images) 
#   return face_locations 


#NEEDED IN test_team_hackitects.py 
#from pii_scan import show_aggie_pride, analyze_text, analyze_image, image, image2, image3
#   
# #Test Cases are built to handle false positives natively, if an image does not conatian a face, array containing faces doesn't populate and a value is not returned
# 
#   def test_image_dectection(self):
#        """Testing if image is detected"""
#
#        # Positive Test Case 1

#        results = analyze_image(image)
#        print(results)
#        self.assertTrue(results) 
#        #image detected, so assert that the array is not empty (isEmpty? = False)
#
#        # Positive Test Case 2 
#
#        results2 = analyze_image(image3)
#        print(results2)
#        self.assertTrue(results2)
#        #image detected, so assert that the array is not empty (isEmpty? = False)
#
#        # Negative Test Case 
#
#        results3 = analyze_image(image2)
#        print(results3)
#        self.assertFalse(results3) 
#        #no image detected, so assert that the array is empty (isEmpty? = True)
