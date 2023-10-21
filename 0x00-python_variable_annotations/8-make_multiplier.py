#!/usr/bin/env python3
"""returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def func(num: float) -> float:
        """a function inside a function"""
        return num * multiplier
    return func
