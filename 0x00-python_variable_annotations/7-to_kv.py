#!/usr/bin/env python3
"""to kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    '''returns a tuple'''
    square: float = pow(v, 2)
    return (k, square)
