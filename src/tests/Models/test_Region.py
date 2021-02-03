import unittest
from src.app.Models.Region import Region


class TestRegion(unittest.TestCase):
    def setUp(self) -> None:
        self.new_region = Region(0, "TestRegion", 100)

    def test_id(self):
        self.assertEqual(self.new_region.id, 0)

    def test_name(self):
        self.assertEqual(self.new_region.name, "TestRegion")

    def test_electoral_votes(self):
        self.assertEqual(self.new_region.electoral_votes, 100)


if __name__ == '__main__':
    unittest.main()
