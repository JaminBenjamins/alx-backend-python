#!/usr/bin/env python3
""" A function that converts a variable to key-value pair """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Converts a variable to KV pair"""
    return k, v**2
