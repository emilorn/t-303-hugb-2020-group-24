from unittest import TestCase
from src.app.Controller.Controller import Controller
from src.app.Service.Service import Service


class TestController(TestCase):

    def setUp(self) -> None:
        self.controller = Controller()
        self.service = Service()
        self.region = "43"
        self.date = "2017-5-5 0:0:0"

    def test_get_all_polls(self):
        self.all_polls_controller = self.controller.get_all_polls()
        self.all_polls_service = self.service.get_all_polls()
        self.assertEqual(len(self.all_polls_controller), len(self.all_polls_service))

    def test_get_current_polls_by_region(self):
        current_polls_by_region_controller = self.controller.get_current_polls_by_region(self.region)
        current_polls_by_region_service = self.service.get_current_polls_by_region(self.region)
        self.assertEqual(len(current_polls_by_region_controller), len(current_polls_by_region_service))

    def test_get_polls_by_region_and_date(self):
        polls_by_region_date_controller = self.controller.get_polls_by_region_and_date(self.region, self.date)
        polls_by_region_date_service = self.service.get_polls_by_region_and_date(self.region, self.date)
        self.assertEqual(len(polls_by_region_date_controller), len(polls_by_region_date_service))

    def test_get_polls_by_date(self):
        polls_by_date_controller = self.controller.get_polls_by_date(self.date)
        polls_by_date_service = self.service.get_polls_by_date(self.date)
        self.assertEqual(len(polls_by_date_controller), len(polls_by_date_service))

    def test_get_all_current_polls(self):
        current_polls_controller = self.controller.get_all_current_polls()
        current_polls_service = self.service.get_all_current_polls()
        self.assertEqual(len(current_polls_controller), len(current_polls_service))

    def test_get_all_candidates(self):
        candidates_controller = self.controller.get_all_candidates()
        candidates_service = self.service.get_all_candidates()
        self.assertEqual(len(candidates_controller), len(candidates_service))
