#!/usr/bin/env python3
"""Module for pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuble[int, int]:
    """
        index_range: function that receive page and
            page_size and return tuple
        Argument:
            page(int): the page received e.g. page =3
            page_size(int): the number of item to be added to the page
        Return:
            Tuple: (int, int)
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
