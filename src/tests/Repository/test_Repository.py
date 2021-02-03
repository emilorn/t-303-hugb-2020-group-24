from unittest import TestCase
import os
from src.app.Repository.Repository import Repository
from datetime import datetime


POLLS_FILENAME = os.path.abspath("src/app/Repository/Data/Bank/polls.csv")
CANDIDATES_FILENAME = os.path.abspath("src/app/Repository/Data/Bank/candidates.csv")


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.test_repo = Repository()
        self.test_date = datetime.strptime("2017-5-5 0:0:0", '%Y-%m-%d %H:%M:%S')

    def test_get_all_polls(self):
        number_of_polls = -1  # -1 to exclude header
        with open(POLLS_FILENAME) as file:
            for _ in file:
                number_of_polls += 1
        # Test checks if we can get the equal amount of polls as there are lines in the CSV file
        self.assertEqual(len(self.test_repo.get_all_polls()), number_of_polls)

    def test_get_all_current_polls(self):
        number_of_open_polls = 0
        with open(POLLS_FILENAME) as file:
            for line in file:
                line_list = line.split(",")
                if line_list[4] == "True":
                    number_of_open_polls += 1
        # Test checks if we can get all the open polls correctly from the CSV file
        self.assertEqual(len(self.test_repo.get_all_current_polls()), number_of_open_polls)

    def test_get_current_polls_by_region(self):
        region_name = "43"
        number_of_polls_by_region = 0
        with open(POLLS_FILENAME) as file:
            for line in file:
                line_list = line.split(",")
                if line_list[5] == "43" and line_list[4] == "True":  # 43 is the ID of Utah in the Region.csv file
                    number_of_polls_by_region += 1

        # Test checks if we can get all the open polls for Utah correctly from the CSV file
        self.assertEqual(len(self.test_repo.get_current_polls_by_region(region_name)), number_of_polls_by_region)

    def test_get_polls_by_region_and_date(self):
        number_of_polls_by_region_and_date = 0
        region_name = "12"
        header = True
        with open(POLLS_FILENAME) as file:
            for line in file:
                if not header:
                    line_list = line.split(",")
                    start_date = datetime.strptime(line_list[2], '%Y-%m-%d %H:%M:%S')
                    end_date = datetime.strptime(line_list[3], '%Y-%m-%d %H:%M:%S')

                    # 12 is the ID for Illinois in Regions.csv
                    if start_date < self.test_date < end_date and line_list[5] == "12":
                        number_of_polls_by_region_and_date += 1
                else:
                    header = False
        self.assertEqual(len(self.test_repo.get_polls_by_region_and_date(region_name, "2017-5-5 0:0:0")),
                         number_of_polls_by_region_and_date)

    def test_get_polls_by_date(self):
        number_of_polls_by_date = 0
        header = True
        with open(POLLS_FILENAME) as file:
            for line in file:
                if not header:
                    line_list = line.split(",")
                    start_date = datetime.strptime(line_list[2], '%Y-%m-%d %H:%M:%S')
                    end_date = datetime.strptime(line_list[3], '%Y-%m-%d %H:%M:%S')
                    if start_date < self.test_date < end_date:  # 12 is the ID for Illinois in Regions.csv
                        number_of_polls_by_date += 1
                else:
                    header = False
        self.assertEqual(len(self.test_repo.get_polls_by_date("2017-5-5 0:0:0")),
                         number_of_polls_by_date)

    def test_get_all_candidates(self):
        number_of_candidates = -1  # -1 to exclude header
        with open(CANDIDATES_FILENAME) as file:
            for _ in file:
                number_of_candidates += 1
        # Test checks if we can get the equal amount of polls as there are lines in the CSV file
        self.assertEqual(len(self.test_repo.get_all_candidates()), number_of_candidates)


