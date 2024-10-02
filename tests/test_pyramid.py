# test_pyramid.py
import pytest
from src.pyramid import Pyramid

def test_pyramid_creation_triangular(pyramid_triangular):
    assert pyramid_triangular.rows == 5
    assert pyramid_triangular.type == 'triangular'
    assert pyramid_triangular.blocks_per_row == [1, 3, 6, 10, 15]

def test_pyramid_creation_square(pyramid_square):
    assert pyramid_square.rows == 4
    assert pyramid_square.type == 'square'
    assert pyramid_square.blocks_per_row == [1, 4, 9, 16]

def test_total_blocks_triangular(pyramid_triangular):
    assert pyramid_triangular.total_blocks() == 35

def test_total_blocks_square(pyramid_square):
    assert pyramid_square.total_blocks() == 30

def test_blocks_in_row_triangular(pyramid_triangular):
    assert pyramid_triangular.blocks_in_row(3) == 6

def test_blocks_in_row_square(pyramid_square):
    assert pyramid_square.blocks_in_row(2) == 4

def test_invalid_row_number(pyramid_triangular):
    with pytest.raises(ValueError):
        pyramid_triangular.blocks_in_row(6)

# Test case for invalid type during creation
def test_invalid_pyramid_type():
    with pytest.raises(ValueError, match="Invalid pyramid type"):
        Pyramid(5, 'hexagonal')

# Test cases for invalid row numbers during creation
def test_invalid_row_number_below_lower_bound():
    with pytest.raises(ValueError, match="Number of rows must be at least 1"):
        Pyramid(0, 'triangular')

import pytest

def test_large_number_of_rows():
    with pytest.raises(ValueError, match="Number of rows must not exceed 1000"):
        Pyramid(1001, 'triangular')
