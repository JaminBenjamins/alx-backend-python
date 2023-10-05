#!/usr/bin/env python3
""" A method that safely gets a value from a dictionary """
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely getting values from a dictionary
    Args:
        dct(dict): Dictionary to get value from.
        key(str): key to get value from.
        default(any): Default value to return if key not found.
    Return:
        Value from dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
