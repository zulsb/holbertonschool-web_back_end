#!/usr/bin/env python3
""" Unittests and integration tests module.
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized, param
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for test Github org client.
    """

    @parameterized.expand([
        param(org="google", test_payload={"payload": True}),
        param(org="abc", test_payload={"payload": False})
    ])
    def test_org(self, org, test_payload):
        """ Test """

    def test_public_repos_url(self):
        """ Test """
