
import unittest

from oop.account import Validator, Details

class MyTests(unittest.TestCase):

    def setUp(self):
        self.obj = Details()

    def test_add_data(self):
        
        comp =self.obj.keep("Mulondo", "Ali", "0772693031", \
            "..myalimul@gmail.com", "12345678")
        self.assertEqual(comp, True)
    
    def test_empty_data(self):
        comp = self.obj.keep("", "Ali", "0772693031", \
            "..myalimul@gmail.com", "12345678")
        self.assertEqual(comp, False)

    def test_fake_email(self):
        comp = self.obj.keep("", "Ali", "0772693031", \
            "..myalimulgmail.com", "12345678")
        self.assertEqual(comp, False)

    def test_rite_email(self):
        comp = self.obj.keep("Mulondo", "Ali", "0772693031", \
            "..myalimul@gmail.com", "12345678")
        self.assertEqual(comp, True)    