#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a start and end indexes of a list"""
    # Compute the start index of the list
    start_index = (page - 1) * page_size

    # Compute the end index of the list
    end_index = start_index + page_size

    return (start_index, end_index)
