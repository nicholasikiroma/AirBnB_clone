#!/usr/bin/python3
"""Module contains unittests for BaseModel"""

import unittest
import re
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit testing for BaseModel clase"""
    
    def test_base(self):
        """test base instances"""
        dummy = BaseModel()

        self.assertIsInstance(dummy.id, str)
        self.assertIsInstance(dummy, BaseModel())

        check_match = re.fullmatch(r"\w{7}-\w{4}-\w{4}-\w{12}")
        self.assertTrue(chech_match)


if __name__ == '__main__':
    unittest.main()
