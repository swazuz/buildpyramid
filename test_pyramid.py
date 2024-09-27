import unittest
from pyramid import Pyramid


class TestPyramid(unittest.TestCase):
    def test_calculate_blocks(self):
        # Arrange
        pyramid = Pyramid()
        height = 3  # Example height

        # Act
        result = pyramid.calculate_blocks(height)

        # Assert
        self.assertEqual(result, 14)  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14



    def test_calculate_blocks_invalid_height(self):
        # Arrange
        pyramid = Pyramid()
        height = 0  # Invalid height

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            pyramid.calculate_blocks(height)
        self.assertEqual(str(context.exception), "Height must be at least 1.")


        

if __name__ == '__main__':
    unittest.main()
