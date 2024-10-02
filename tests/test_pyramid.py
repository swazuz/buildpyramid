import pytest
from src.pyramid import Pyramid


def test_calculate_blocks():
    # Arrange
    pyramid = Pyramid()
    height = 3  # Example height

    # Act
    result = pyramid.calculate_blocks(height)

    # Assert
    assert result == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_calculate_blocks_invalid_height():
    # Arrange
    pyramid = Pyramid()
    height = 0  # Invalid height

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        pyramid.calculate_blocks(height)
    assert str(excinfo.value) == "Height must be at least 1."
