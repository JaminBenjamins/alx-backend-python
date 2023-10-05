#!/usr/bin/env python3
"""A function augmenting code with correct duck-typed annotations"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list or None if list is empty"""
    if list:
        return lst[0]
    else:
        return None
