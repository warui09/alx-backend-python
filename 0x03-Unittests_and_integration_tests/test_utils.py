#!/usr/bin/env python3
"""task 0 solution"""

from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
import unittest
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """class to test the utils.access_nested_map function"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """test utils.access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """test if utils.access_nested_map function raises exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class to test utils.get_json function"""

    @patch("requests.get")
    def test_get_json(self, mock_get):
        """test utils.get_json with two params"""

        test_data = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_data:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_with(test_url)

            self.assertEqual(result, test_payload)
