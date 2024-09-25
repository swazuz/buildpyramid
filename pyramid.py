class Pyramid:
    def calculate_blocks(self, height):
        if height < 1:
            raise ValueError("Height must be at least 1.")
        return sum(i**2 for i in range(1, height+1))
