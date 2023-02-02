#!/usr/bin/env python3
"""
    Duck typing Typevar
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
        Args:
            dct: Mapping
            key: Any data type
            default: Default value

        Return:
            Any or T format
    """
    if key in dct:
        return dct[key]
    else:
        return default
