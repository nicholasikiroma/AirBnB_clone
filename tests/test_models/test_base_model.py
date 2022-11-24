#!/usr/bin/python3
"""Module contains unittests for BaseModel"""

import unittest
import re
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit testing for BaseModel clase"""

    def test_base(self):
        """test base instances"""
        user = BaseModel()

        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user, BaseModel)

        check_match = re.fullmatch(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", user.id)
        self.assertTrue(check_match)

    def test_unique_id(self):
        """Test for unique user i.d"""
        user_1 = BaseModel()
        user_2 = BaseModel()

        self.assertNotEqual(user_1.id, user_2.id)

    def test_str(self):
        user = BaseModel()
        expected = f"[{'BaseModel'}] {user.id} {user.__dict__}"

        self.assertEqual(str(user), expected)


if __name__ == '__main__':
    unittest.main()
