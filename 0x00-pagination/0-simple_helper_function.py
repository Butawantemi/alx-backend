#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start idx and an end idx
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx
