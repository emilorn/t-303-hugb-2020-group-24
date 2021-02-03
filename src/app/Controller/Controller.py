import unittest
from src.app.Controller.CandidateController import CandidateController
from src.app.Controller.PollController import PollController
from src.app.Controller.RegionController import RegionController
from src.app.Controller.ElectionController import ElectionController


class Controller(object):

    def __init__(self):
        self.poll_controller = PollController()
        self.candidate_controller = CandidateController()
        self.region_controller = RegionController()
        self.election_controller = ElectionController()

    def input_parser(self, function_input):
        raise NotImplemented()

    # ---- POLL METHODS START ----
    def get_all_polls(self):
        return self.poll_controller.get_all_polls()

    def get_average_poll(self, electionID: str):
        return self.poll_controller.get_average_poll(electionID)

    def get_all_current_polls(self):
        return self.poll_controller.get_all_current_polls()

    def get_current_polls_by_region(self, regionID: str):
        return self.poll_controller.get_current_polls_by_region(regionID)

    def get_polls_by_region_and_date(self, regionID: str, date: str):
        return self.poll_controller.get_polls_by_region_and_date(regionID, date)

    def get_polls_by_date(self, date: str):
        return self.poll_controller.get_polls_by_date(date)

    def get_all_historical_polls(self, year: str):
        return self.poll_controller.get_all_historical_polls(year)

    def get_polls_by_region(self, region):
        return self.poll_controller.get_polls_by_region(region)

    def get_polls_by_election(self, election):
        return self.poll_controller.get_polls_by_election(election)
    # ---- POLL METHODS END ----

    # ---- REGION METHODS START ----

    def get_all_regions(self):
        return self.region_controller.get_all_regions()

    def get_region_by_id(self, region_id: str):
        return self.region_controller.get_region_by_id(region_id)

    def get_regions_by_election(self, election_id: str):
        return self.region_controller.get_regions_by_election(election_id)
    # ---- REGION METHODS END ----

    # ---- CANDIDATE METHODS START ----
    def get_all_candidates(self):
        return self.candidate_controller.get_all_candidates()

    def get_candidate_by_id(self, candidate_id: str):
        return self.candidate_controller.get_candidate_by_id(candidate_id)

    def get_candidates_by_party(self, party: str):
        return self.candidate_controller.get_candidates_by_party(party)

    def create_candidate(self, data):
        return self.candidate_controller.create_candidate(data)
    # ---- CANDIDATE METHODS END ----
    # ---- ELECTION METHODS START ----
    def get_election_by_id(self, election_id):
        return self.election_controller.get_election_by_id(election_id)
    # ---- ELECTION METHODS END ----



if __name__ == '__main__':
    new_cont = Controller()
    new_cont.get_all_polls()
