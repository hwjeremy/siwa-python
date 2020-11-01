"""
Signin With Apple
Token Module
author: hugh@blinkybeach.com
"""
from enum import Enum


class RealPerson(Enum):
    UNSUPPORTED = 0
    UNKNOWN = 1
    LIKELY_REAL = 2
