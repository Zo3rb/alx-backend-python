#!/usr/bin/env python3
'''11. More involved type annotations'''

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary based on a key, with an optional default value.

    Args:
      dct (Mapping): The dictionary-like object to retrieve values from.
      key (Any): The key to look for in the dictionary.
      default (Optional[T], optional): The optional default value. Defaults to None.
    Returns:
        Union[Any, T]: The value from the dictionary if the key is found, or the default value.
    """
    if key in dct:
      return dct[key]
    else:
      return default

