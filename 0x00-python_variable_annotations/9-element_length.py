#!/usr/bin/env python3
"""
    A function to annotate the parameters 
    and return appropriate types
"""
from typing import  Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                    ) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with length of each element"""
    return [(i, len(i)) for i in lst]
