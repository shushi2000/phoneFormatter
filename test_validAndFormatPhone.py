#!/usr/bin/env python
#!coding: utf-8

import unittest
from validAndFormatPhone import validAndFormatPhone

class TestValidAndFormatPhone(unittest.TestCase):
    def test_alphabetic(self):
        self.assertIsNone(
                validAndFormatPhone('abcdefg'))

    def test_mixed_alpha_numbers(self):
        self.assertIsNone(
                validAndFormatPhone('456-a09-0001')
                )

    def test_inccorect_length(self):
        self.assertIsNone(
                validAndFormatPhone('123-456-789'))

    def test_with_country_number_1(self):
        self.assertEqual(
                validAndFormatPhone('1-301-480-0123'),
                '(301)-480-0123'
                )
    
    def test_with_bracket(self):
        self.assertEqual(
                validAndFormatPhone('(456)-789-0001'),
                '(456)-789-0001'
                )

    def test_imcomplete_bracket(self):
        self.assertEqual(
                validAndFormatPhone('(456-789-0001'),
                '(456)-789-0001'
                )

    def test_only_one_hyphone(self):
        self.assertEqual(
                validAndFormatPhone('456-7890001'),
                '(456)-789-0001'
                )
        self.assertEqual(
                validAndFormatPhone('456789-0001'),
                '(456)-789-0001'
                )

    def test_hypone_wrong_place(self):
        self.assertIsNone(
                validAndFormatPhone('4567-89-0001')
                )
    
    def test_empty_string(self):
        self.assertIsNone(
                validAndFormatPhone('')
                )

    def test_input_None(self):
        self.assertIsNone(
                validAndFormatPhone(None)
                )

    def test_input_float(self):
        self.assertEqual(
                validAndFormatPhone(4561237890),
                '(456)-123-7890'
                )

    def test_input_floatNan(self):
        self.assertIsNone(
                validAndFormatPhone(float('nan'))
                )

if __name__ == "__main__":
    unittest.main()
