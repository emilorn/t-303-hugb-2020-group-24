from unittest import TestCase
import datetime

from src.app.Repository.Repository import Repository
from src.app.Service.Service import Service


class TestService(TestCase):

    def setUp(self) -> None:
        self.repository = Repository()
        self.service = Service()
        self.maxDiff = None

    def test_get_all_polls(self):
        repository_polls = self.repository.get_all_polls()
        service_polls = self.service.get_all_polls()
        self.assertEqual(len(repository_polls), len(service_polls))

    def test_get_all_current_polls(self):
        repository_polls = self.repository.get_all_current_polls()
        service_polls = self.service.get_all_current_polls()
        self.assertEqual(len(repository_polls), len(service_polls))

    def test_get_current_polls_by_region(self):
        regions = self.repository.get_all_regions()
        some_region = regions[1].id
        repository_polls = self.repository.get_current_polls_by_region(some_region)
        service_polls = self.service.get_current_polls_by_region(some_region)
        self.assertEqual(len(repository_polls), len(service_polls))

    def test_get_polls_by_region_and_date(self):
        regions = self.repository.get_all_regions()
        some_region = regions[1].id
        date = datetime.datetime(2016, 8, 12)
        some_date = date.strftime("%Y-%m-%d %H:%M:%S")
        repository_polls = self.repository.get_polls_by_region_and_date(some_region, some_date)
        service_polls = self.service.get_polls_by_region_and_date(some_region, some_date)
        self.assertEqual(len(repository_polls), len(service_polls))

    def test_get_polls_by_date(self):
        date = datetime.datetime(2016, 8, 12)
        some_date = date.strftime("%Y-%m-%d %H:%M:%S")
        repository_polls = self.repository.get_polls_by_date(some_date)
        service_polls = self.service.get_polls_by_date(some_date)
        self.assertEqual(len(repository_polls), len(service_polls))

    def test_get_all_candidates(self):
        repository_candidates = self.repository.get_all_candidates()
        service_candidates = self.service.get_all_candidates()
        self.assertEqual(len(repository_candidates), len(service_candidates))

