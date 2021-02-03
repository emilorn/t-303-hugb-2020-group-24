import unittest

from src.app.Models.Election import Election
from src.app.Models.Poll import Poll
from src.app.Models.Region import Region
from src.app.Models.Candidate import Candidate
from src.app.Models.Policy import Policy
from src.app.Models.PoliticalParty import PoliticalParty
from datetime import datetime


class TestPoll(unittest.TestCase):

    def __new_candidate(self, number: int) -> Candidate:
        new_political_party = PoliticalParty(0, 'TestParty')
        new_policy_1 = Policy(0, f"Testing{number}", f"TestDescription{number}")
        new_policy_2 = Policy(0, f"Testing{number+1}", f"TestDescription{number+1}")
        policies = [new_policy_1, new_policy_2]
        new_candidate = Candidate(0, "Tester", new_political_party, policies)
        return new_candidate

    def setUp(self) -> None:
        self.choices = [self.__new_candidate(1), self.__new_candidate(2)]
        self.result_dict = {self.choices[0].name: 100, self.choices[1].name: 200}
        self.start_date = datetime.strptime("2019-10-07 00:00:00", '%Y-%m-%d %H:%M:%S')
        self.end_date = datetime.strptime("2019-10-07 00:00:00", '%Y-%m-%d %H:%M:%S')

        self.new_region = Region(0, "TestRegion", 100)

        self.test_election = Election(0, "test_election", self.choices, self.end_date)
        self.test_poll = Poll(0, self.choices, self.start_date, self.end_date, True, self.new_region, self.result_dict,
                              self.test_election)

    def test_id(self):
        self.assertEqual(self.test_poll.id, 0)

    def test_choices(self):
        self.assertEqual(self.test_poll.choices, self.choices)

    def test_start_date(self):
        self.assertEqual(self.test_poll.start_date, self.start_date)

    def test_end_date(self):
        self.assertEqual(self.test_poll.end_date, self.end_date)

    def test_is_open(self):
        self.assertEqual(self.test_poll.is_open, True)

    def test_region(self):
        self.assertEqual(self.test_poll.region, self.new_region)

    def test_result_dict(self):
        self.assertEqual(self.test_poll.results, self.result_dict)


if __name__ == '__main__':
    unittest.main()
