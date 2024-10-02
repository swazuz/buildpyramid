class Pyramid:
    MAX_ROWS = 1000  # Set a reasonable limit for the number of rows

    def __init__(self, rows: int, type: str='square'):
        if rows < 1:
            raise ValueError("Number of rows must be at least 1")
        if rows > self.MAX_ROWS:
            raise ValueError(f"Number of rows must not exceed {self.MAX_ROWS}")
        self.rows = rows
        self.type = type
        self.blocks_per_row = self.calculate_blocks_per_row()

    def calculate_blocks_per_row(self):
        blocks_per_row = []
        if self.type == 'triangular':
            for n in range(1, self.rows + 1):
                blocks_per_row.append((n * (n + 1)) // 2)
        elif self.type == 'square':
            for n in range(1, self.rows + 1):
                blocks_per_row.append(n ** 2)
        else:
            raise ValueError("Invalid pyramid type")
        return blocks_per_row

    def total_blocks(self):
        return sum(self.blocks_per_row)

    def blocks_in_row(self, row):
        if 1 <= row <= self.rows:
            return self.blocks_per_row[row - 1]
        else:
            raise ValueError("Row number out of range")
