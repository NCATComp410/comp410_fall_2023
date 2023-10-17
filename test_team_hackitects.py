import unittest
from pii_scan import show_aggie_pride, analyze_text, analyze_image, image, image2, image3


class TestTeamHackitects(unittest.TestCase):
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    # evals false if 'results' is not defined (empty array)
    # if evals true, then array is not empty (face has been detected) 

    
    def test_image_dectection(self):
        """Testing if image is detected"""
        
        # Positive Test Case 1
        
        results = analyze_image(image)
        print(results)
        self.assertTrue(results) 
        #image detected, so assert that the array is not empty (isEmpty? = False)

        # Positive Test Case 2 
        
        results2 = analyze_image(image3)
        print(results2)
        self.assertTrue(results2)
        #image detected, so assert that the array is not empty (isEmpty? = False)
        
        # Negative Test Case 
        
        results3 = analyze_image(image2)
        print(results3)
        self.assertFalse(results3) 
        #no image detected, so assert that the array is empty (isEmpty? = True)
        
