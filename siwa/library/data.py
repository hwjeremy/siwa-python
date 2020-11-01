"""
Sign In with Apple
Data Module
author: hugh@blinkybeach.com
"""
import base64
from typing import Union


class Data:

    @staticmethod
    def decode_b64(data: bytes) -> bytes:
        padded = Data.pad(data)
        return base64.urlsafe_b64decode(padded)

    @staticmethod
    def pad(data: Union[bytes, str]) -> bytes:
        if isinstance(data, str):
            data = data.encode('ascii')

        padding = len(data) % 4

        if padding > 0:
            data += b'=' * (4 - padding)

        return data
