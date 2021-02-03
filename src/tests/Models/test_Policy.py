import unittest
from src.app.Models.Policy import Policy


class TestPolicy(unittest.TestCase):
    def setUp(self) -> None:
        self.new_policy = Policy(0, "TestCategory", "TestDescription")

    def test_id(self):
        self.assertEqual(self.new_policy.id, 0)

    def test_category(self):
        self.assertEqual(self.new_policy.category, "TestCategory")

    def test_description(self):
        self.assertEqual(self.new_policy.description, "TestDescription")


if __name__ == '__main__':
    unittest.main()
