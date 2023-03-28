#! /usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from src.fancy_addition import fancy_addition


class FancyAdditionTestCase(unittest.TestCase):
    def test_fancy_addition(self):
        self.assertEqual(0, fancy_addition(0, 0))
        self.assertEqual(3, fancy_addition(3, 0))
        self.assertEqual(5, fancy_addition(2, 3))
        self.assertEqual(3635, fancy_addition(1343, 2292))

        self.assertNotEqual(0, fancy_addition(3, 0))
        self.assertNotEqual(4, fancy_addition(0, 0))
        self.assertNotEqual(5, fancy_addition(4, 2))
        self.assertNotEqual(5234, fancy_addition(1687, 3546))


if __name__ == "__main__":
    unittest.main()
