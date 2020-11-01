"""
Apple ID Python
Key Protocol Module
author: hugh@blinkybeach.com
"""
from rsa import PublicKey as RSA_PublicKey


class PublicKey:
    """Abstract protocol defining behaviour of implemented public keys"""
    identifier: str = NotImplemented
    rsa_public_key: RSA_PublicKey = NotImplemented
