#!/usr/bin/env python3
"""task 4 solution"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """class to test client.GithubOrgClient class"""

    @parameterized.expand(
        [("google", {"login": "google"}), ("abc", {"login": "google"})]
    )
    def test_org(self, org, expected):
        """get_json once with the expected argument"""

        with patch("client.GithubOrgClient.org") as mock_org:
            mock_org(org).return_value = expected
            mock_org.assert_called_once_with(org)
            self.assertEqual(expected, {"login": "google"})

    def test_public_repos_url(self):
        """test GithubOrgClient._public_repos_url"""

        with patch(
                "client.GithubOrgClient.org", new_callable=PropertyMock
            ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
