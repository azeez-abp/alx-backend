"""Module for pagination"""
from typing import tuple

def index_range(page: int, page_size: int)->tuple:
    """
        index_range: function that receive page and
            page_size and return tuple
        Argument:
            page: int: the page received e.g. page =3
            page_size: the number of item to be added to the page
    """
    return page, page + page_size
