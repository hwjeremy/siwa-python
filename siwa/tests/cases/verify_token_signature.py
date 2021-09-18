"""
Signin With Apple
Verify Token Signature Test
author: hugh@blinkybeach.com
"""
from siwa import IdentityToken, KeyCache
from siwa.tests.test import Test
from siwa.tests.test_result import Success, TestResult


class VerifyTokenSignature(Test):

    NAME = 'Verify an IdentityToken\'s signature'

    def execute(self) -> TestResult:

        cache = KeyCache()

        token = IdentityToken.parse(self.example_token)
        valid = token.is_validly_signed(
            audience=self.test_audience,
            key_cache=cache,
            ignore_expiry=True
        )
        assert valid is True

        # Mess up the signature slightly
        bad_raw_token = self.example_token[:-3] + 'j' + self.example_token[-3:]

        bad_token = IdentityToken.parse(bad_raw_token)
        valid = bad_token.is_validly_signed(
            audience=self.test_audience,
            key_cache=cache,
            ignore_expiry=True
        )
        assert valid is False

        return Success()
