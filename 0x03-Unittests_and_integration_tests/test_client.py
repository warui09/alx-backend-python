#!/usr/bin/env python3
"""task 4 solution"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """class to test client.GithubOrgClient class"""

    @parameterized.expand(
        [("google", {"login": "google"}), ("abc", {"login": "google"})]
    )
    def test_org(self, org, expected):
        """get_json once with the expected argument"""

        with patch("client.GithubOrgClient.org") as mock_get:
            mock_get(org).return_value = expected
            mock_get.assert_called_once_with(org)
            self.assertEqual(expected, {"login": "google"})
