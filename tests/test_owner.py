import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    def test_owner_info(self):
        owner = Owner("Alice", "0123", "Hà Nội")
        self.assertEqual(owner.name, "Alice")
        self.assertIn("Phone: 0123", owner.get_info())
