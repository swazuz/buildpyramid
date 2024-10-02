# tests/conftest.py
import pytest
from src.pyramid import Pyramid

@pytest.fixture
def pyramid_triangular():
    return Pyramid(5, 'triangular')

@pytest.fixture
def pyramid_square():
    return Pyramid(4, 'square')
