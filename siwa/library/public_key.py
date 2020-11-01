"""
Apple ID Python
Public Key Module
author: hugh@blinkybeach.com
"""
from typing import TypeVar, Type
from urllib.request import Request, urlopen
from typing import List, Dict, Optional
from rsa import PublicKey as RSA_PublicKey
from siwa.library.data import Data
import json
from siwa.library.key_protocol import PublicKey
from siwa.library.key_cache import KeyCache

T = TypeVar('T', bound='ApplePublicKey')


class ApplePublicKey(PublicKey):

    _RETRIEVAL_URL = 'https://appleid.apple.com/auth/keys'

    def __init__(
        self,
        algorithm: str,
        identifier: str,
        family: str,
        use: str,
        modulus: str,     # n value
        exponent: str     # e value
    ) -> None:

        self._family = family
        self._identifier = identifier
        self._use = use
        self._algorithm = algorithm
        self._modulus = modulus
        self._exponent = exponent

        return

    identifier = property(lambda s: s._identifier)
    rsa_public_key = property(lambda s: RSA_PublicKey(
        n=int.from_bytes(Data.decode_b64(s._modulus), 'big'),
        e=int.from_bytes(Data.decode_b64(s._exponent), 'big')
    ))

    @classmethod
    def decode(cls: Type[T], data: Dict[str, str]) -> T:
        return cls(
            algorithm=data['alg'],
            identifier=data['kid'],
            family=data['kty'],
            use=data['use'],
            modulus=data['n'],
            exponent=data['e']
        )

    @classmethod
    def decode_many(
        cls: Type[T],
        data: List[Dict[str, str]]
    ) -> List[PublicKey]:
        return [cls.decode(d) for d in data]

    @classmethod
    def retrieve_all(
        cls: Type[T],
        cache: Optional[KeyCache] = None
    ) -> List[PublicKey]:

        request = Request(
            url=cls._RETRIEVAL_URL,
            method='GET'
        )

        response = urlopen(request).read()
        data = json.loads(response)
        keys = cls.decode_many(data['keys'])
        if cache is not None:
            cache.store_many(keys)
        return keys

    @classmethod
    def retrieve_by_id(
        cls: Type[T],
        identifier: str,
        cache: Optional[KeyCache] = None
    ) -> Optional[PublicKey]:

        if cache is not None:
            cached = cache.retrieve(identifier)
            if cached is not None:
                return cached

        all_keys = cls.retrieve_all()
        for key in all_keys:
            if key.identifier == identifier:
                return key
        return None
