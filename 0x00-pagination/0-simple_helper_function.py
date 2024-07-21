#!/usr/bin/python3

"""Module for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuble[int, int]:
    """
        index_range: function that receive page and
            page_size and return tuple
        Argument:
            page: int: the page received e.g. page =3
            page_size: the number of item to be added to the page
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
