"""
Signin With Apple
Header Module
author: hugh@blinkybeach.com
"""
from typing import TypeVar, Type, Dict, Optional
from siwa.library.public_key import ApplePublicKey
from siwa.library.key_protocol import PublicKey
from siwa.library.key_cache import KeyCache

T = TypeVar('T', bound='Header')


class Header:

    def __init__(
        self,
        identifier: str,
        algorithm: str
    ) -> None:

        self._identifier = identifier
        self._algorithm = algorithm

        return

    def retrieve_public_key(
        self,
        key_cache: Optional[KeyCache] = None
    ) -> PublicKey:
        key = ApplePublicKey.retrieve_by_id(
            identifier=self._identifier,
            cache=key_cache
        )
        if key is None:
            raise RuntimeError('Apple PublicKey not found ' + self._identifier)
        return key

    @classmethod
    def decode(cls: Type[T], data: Dict) -> T:
        return cls(
            identifier=data['kid'],
            algorithm=data['alg']
        )
