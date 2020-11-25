#!/usr/bin/env python3
""" Unittests and integration tests module.
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized, param


class TestAccessNestedMap(unittest.TestCase):
    """ Class for nested map access test.
    """
    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, expected, nested_map, path):
        """ Method that test access nested map
            and returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(KeyError, nested_map={}, path=("a",)),
        param(KeyError, nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, expected, nested_map, path):
        """ Method that test acces nested map exception.
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
