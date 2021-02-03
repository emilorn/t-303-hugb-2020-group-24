import unittest
from src.app.Models.Candidate import Candidate
from src.app.Models.PoliticalParty import PoliticalParty
from src.app.Models.Policy import Policy


class TestCandidate(unittest.TestCase):
    def setUp(self) -> None:
        self.new_political_party = PoliticalParty(0, 'TestParty')
        self.new_policy_1 = Policy(0, "Testing1", "TestDescription1")
        self.new_policy_2 = Policy(0, "Testing2", "TestDescription2")
        self.policies = [self.new_policy_1, self.new_policy_2]
        self.new_candidate = Candidate(0, "Tester", self.new_political_party, self.policies)

    def test_id(self):
        self.assertEqual(self.new_candidate.id, 0)

    def test_name(self):
        self.assertEqual(self.new_candidate.name, "Tester")

    def test_political_party(self):
        self.assertEqual(self.new_candidate.political_party, self.new_political_party)

    def test_policies(self):
        self.assertEqual(self.new_candidate.policies, self.policies)

    def test_str_method(self):
        policy_str: str = ""
        for policy in self.new_candidate.policies:
            policy_str += str(policy) + "\n"
        test_str: str = "{:<15}\t{:>60}\n{:^115}\n{}".format(self.new_candidate.name,
                                                             str(self.new_candidate.political_party), "***Policies***",
                                                             policy_str)
        self.assertEqual(self.new_candidate.__str__(), test_str)


if __name__ == '__main__':
    unittest.main()
