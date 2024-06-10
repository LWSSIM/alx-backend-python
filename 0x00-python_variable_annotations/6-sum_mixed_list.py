#!/usr/bin/env python3
""" mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum a miced list of ints and floats """
    return sum(mxd_lst)
