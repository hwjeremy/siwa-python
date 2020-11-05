"""
Signin With Apple
Header Module
author: hugh@blinkybeach.com
"""
from typing import TypeVar, Type, Dict, Optional
from siwa.library.token.real_person import RealPerson

T = TypeVar('T', bound='Payload')


class Payload:

    def __init__(
        self,
        issuer: str,
        subject: str,
        audience: str,
        issued_at: int,
        expiration_time: int,
        nonce: Optional[str],
        nonce_supported: bool,
        email: str,
        email_verified: bool,
        is_private_email: Optional[bool],
        real_person: Optional[RealPerson]

    ) -> None:

        self._issuer = issuer
        self._subject = subject
        self._audience = audience
        self._issued_at = issued_at
        self._expiration_time = expiration_time
        self._nonce = nonce
        self._nonce_supported = nonce_supported
        self._email = email
        self._email_verified = email_verified
        self._is_private_email = is_private_email
        self._real_person = real_person

        return

    unique_apple_user_id = property(lambda s: s._subject)
    expires_utc_seconds_since_epoch = property(lambda s: s._expiration_time)
    issued_utc_seconds_since_epoch = property(lambda s: s._issued_at)
    email = property(lambda s: s._email)
    email_is_private = property(lambda s: s._is_private_email)
    real_person = property(lambda s: s._real_person)
    audience = property(lambda s: s._audience)

    @classmethod
    def decode(cls: Type[T], data: Dict) -> T:
        return cls(
            issuer=data['iss'],
            subject=data['sub'],
            audience=data['aud'],
            issued_at=data['iat'],
            expiration_time=data['exp'],
            nonce=data['nonce'] if 'nonce' in data else None,
            nonce_supported=data['nonce_supported'],
            email=data['email'],
            email_verified=data['email_verified'],
            is_private_email=data['is_private_email'] if 'is_private_email' in
            data else None,
            real_person=RealPerson(data['real_user_status']) if
            'real_user_status' in data else None
        )
