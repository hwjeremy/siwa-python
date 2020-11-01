"""
Apple ID Python
Key Cache Module
author: hugh@blinkybeach.com
"""
from siwa.library.key_protocol import PublicKey
from typing import Optional, Dict, List


class KeyCache:

    def __init__(self) -> None:
        self._stored_keys: Dict[str, PublicKey] = {}
        return

    def store(self, key: PublicKey) -> None:
        self._stored_keys[key.identifier] = key
        return

    def store_many(self, keys: List[PublicKey]) -> None:
        for k in keys:
            self.store(k)
        return

    def retrieve(self, identifier: str) -> Optional[PublicKey]:
        if identifier in self._stored_keys.keys():
            return self._stored_keys[identifier]
        return None
