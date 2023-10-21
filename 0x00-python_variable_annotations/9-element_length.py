#!/usr/bin/env python3
"""returns len of list"""


def element_length(lst: list) -> int:
    """returns list length"""
    return [(i, len(i)) for i in lst]
