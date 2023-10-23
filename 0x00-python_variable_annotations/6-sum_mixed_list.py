#!/usr/bin/env python3
"""mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sums a mixed list"""
    result = 0.0
    for num in mxd_list:
        result += num
    return result
