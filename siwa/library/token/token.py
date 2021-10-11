"""
Signin With Apple
Token Module
author: hugh@blinkybeach.com
"""
import jwt
from jwt.exceptions import PyJWTError
from typing import TypeVar, Type, Any, Dict, Union, Optional
from siwa.library.data import Data
import json
from siwa.library.key_cache import KeyCache
from siwa.library.token.header import Header
from siwa.library.token.payload import Payload

T = TypeVar('T', bound='IdentityToken')


class IdentityToken:

    def __init__(
        self,
        header: Header,
        payload: Payload,
        raw_signed_body: bytes,
        signature: bytes,
        raw_token: bytes
    ) -> None:

        self._header = header
        self._payload = payload
        self._raw_signed_body = raw_signed_body
        self._signature = signature
        self._raw_token = raw_token

        return

    payload = property(lambda s: s._payload)

    def is_validly_signed(
        self,
        audience: str,
        key_cache: Optional[KeyCache] = None,
        ignore_expiry: bool = False
    ) -> bool:

        if not isinstance(audience, str):
            raise TypeError('audience must be of type `str`')

        apple_public_key = self._header.retrieve_public_key(key_cache)
        rsa_key = apple_public_key.rsa_public_key
        pks = rsa_key.save_pkcs1()

        try:
            result = jwt.decode(
                jwt=self._raw_token,
                key=pks,
                algorithms=['RS256'],
                audience=audience,
                options={
                    'verify_exp': not ignore_expiry
                }
            )
        except PyJWTError as error:
            return False

        return result is not None

    @classmethod
    def decode(cls: Type[T], data: Dict[str, Any]) -> T:
        raise NotImplementedError

    @classmethod
    def parse(cls: Type[T], data: Union[bytes, str]) -> T:

        if isinstance(data, str):
            data = data.encode('utf-8')

        raw_header, raw_payload, raw_signature = data.rsplit(b'.')

        header = Header.decode(json.loads(Data.decode_b64(raw_header)))
        payload = Payload.decode(json.loads(Data.decode_b64(raw_payload)))
        signature = Data.decode_b64(raw_signature)

        return cls(
            header=header,
            payload=payload,
            raw_signed_body=b'.'.join((raw_header, raw_payload)),
            signature=signature,
            raw_token=data
        )
