#!/usr/bin/env python3
"""to kv"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''returns a tuple'''
    square: float = pow(v, 2)
    return (k, square)
