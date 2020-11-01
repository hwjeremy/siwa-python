"""
Signin With Apple
Parse Identity Token Test
author: hugh@blinkybeach.com
"""
from siwa import IdentityToken
from siwa.tests.test import Test
from siwa.tests.test_result import Success, TestResult


class ParseIdentityToken(Test):

    NAME = 'Parse an identity token'

    def execute(self) -> TestResult:

        IdentityToken.parse(self.example_token)

        return Success()
