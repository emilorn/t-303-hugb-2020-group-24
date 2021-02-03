import unittest
from src.app.Models.PoliticalParty import PoliticalParty


class TestPoliticalParty(unittest.TestCase):
    def setUp(self) -> None:
        self.new_political_party = PoliticalParty(0, "TestParty")

    def test_id(self):
        self.assertEqual(self.new_political_party.id, 0)

    def test_name(self):
        self.assertEqual(self.new_political_party.name, "TestParty")


if __name__ == '__main__':
    unittest.main()
