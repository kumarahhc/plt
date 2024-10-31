import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    #US-1
    def test_input_phase(self):
        translater= PigLatin("hellow world")
        self.assertEqual("hellow world",translater.get_phrase())

    #US-2
    def test_empty_prase(self):
        translater= PigLatin("")
        self.assertEqual("nil",translater.translate())

    # US-3
    def test_word_end_with_y(self):
        translater = PigLatin("why")
        self.assertEqual("whynqy", translater.translate())

    def test_word_end_with_vovel_a(self):
        translater = PigLatin("salsa")
        self.assertEqual("salsayay", translater.translate())
    def test_word_end_with_volel_e(self):
        translater = PigLatin("salse")
        self.assertEqual("salseyay", translater.translate())
    def test_word_end_with_volel_i(self):
        translater = PigLatin("salsi")
        self.assertEqual("salsiyay", translater.translate())
    def test_word_end_with_volel_o(self):
        translater = PigLatin("salso")
        self.assertEqual("salsoyay", translater.translate())
    def test_word_end_with_volel_u(self):
        translater = PigLatin("salsu")
        self.assertEqual("salsuyay", translater.translate())