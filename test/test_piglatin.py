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
        translater = PigLatin("any")
        self.assertEqual("anynay", translater.translate())

    def test_word_end_with_vovel_a(self):
        translater = PigLatin("apple")
        self.assertEqual("appleyay", translater.translate())

    def test_word_end_with_volel_e(self):
        translater = PigLatin("ask")
        self.assertEqual("askay", translater.translate())

    #US-4
    def test_translate_word_end_with_one_consonant(self):
        translater = PigLatin("hello")
        self.assertEqual("ellohay", translater.translate())

    #US - 5
    #def test_translate_word_end_with_one_consonant(self):
    #    translater = PigLatin("hello")
    #    self.assertEqual("ellohay", translater.translate())