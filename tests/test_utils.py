import unittest
from src.utils.logger import get_logger


class TestUtils(unittest.TestCase):
    def test_get_logger(self):
        """Test that get_logger creates a logger with the correct name."""
        logger = get_logger("test_logger")
        self.assertEqual(logger.name, "test_logger")


if __name__ == "__main__":
    unittest.main()
