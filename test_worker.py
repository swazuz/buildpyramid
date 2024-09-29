import unittest
from models.worker import Worker

class TestWorker(unittest.TestCase):
    
    def test_create_worker(self):
        # Arrange & Act
        worker = Worker(name="Raa", role="builder")
        # Assert
        self.assertEqual(worker.name, "Raa")
        self.assertEqual(worker.role, "builder")


    def test_create_architect(self):
        # Arrange & Act
        worker = Worker(name="Amun", role="architect")
        # Assert
        self.assertEqual(worker.name, "Amun")
        self.assertEqual(worker.role, "architect")


    def test_invalid_role(self):
        # Arrange & Act
        worker = Worker.create(name="somename", role="INVALID")
        # Assert
        self.assertEqual(worker, None)
        

if __name__ == '__main__':
    unittest.main()
