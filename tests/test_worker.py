import pytest
from src.worker import Worker

def test_create_worker():
    # Arrange & Act
    worker = Worker(name="Raa", role="builder")
    # Assert
    assert worker.name == "Raa"
    assert worker.role == "builder"

def test_create_architect():
    # Arrange & Act
    worker = Worker(name="Amun", role="architect")
    # Assert
    assert worker.name == "Amun"
    assert worker.role == "architect"

def test_invalid_role():
    # Arrange & Act
    worker = Worker.create(name="somename", role="INVALID")
    # Assert
    assert worker is None
