import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phase(self):
        translater= PigLatin("hellow world")
        self.assertEqual("hellow world",translater.get_phrase())


