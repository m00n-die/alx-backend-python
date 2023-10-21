#!/usr/bin/env python3
"""returns len of list"""
from typing import Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list length"""
    return [(i, len(i)) for i in lst]
