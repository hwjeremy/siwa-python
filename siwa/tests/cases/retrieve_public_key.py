"""
Signin With Apple
Retrieve Public Keys Test
author: hugh@blinkybeach.com
"""
from siwa import ApplePublicKey
from siwa.tests.test import Test
from siwa.tests.test_result import Success, TestResult


class RetrievePublicKeys(Test):

    NAME = 'Retrieve Apple\'s public keys'

    def execute(self) -> TestResult:

        all_keys = ApplePublicKey.retrieve_all()
        assert isinstance(all_keys, list)
        assert len(all_keys) > 1
        assert False not in [isinstance(k, ApplePublicKey) for k in all_keys]

        key_id = all_keys[0].identifier

        specific_key = ApplePublicKey.retrieve_by_id(key_id)
        assert isinstance(specific_key, ApplePublicKey)
        assert specific_key.identifier == key_id

        return Success()
