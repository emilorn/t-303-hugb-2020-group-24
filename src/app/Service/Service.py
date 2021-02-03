from src.app.Service.PollService import PollService
from src.app.Service.CandidateService import CandidateService
from src.app.Service.RegionService import RegionService


class Service:
    def __init__(self):
        self.pollService = PollService()
        self.politicianService = CandidateService()
        self.regionService = RegionService()

    def get_all_polls(self):
        return self.pollService.get_all_polls()

    def get_average_poll(self, electionID: str):
        return self.pollService.get_average_poll(electionID)

    def get_all_current_polls(self):
        return self.pollService.get_all_current_polls()

    def get_all_elections(self):
        return self.pollService.get_all_elections()

    def get_election_by_id(self, election_id: str):
        return self.pollService.get_election_by_id(election_id)

    def get_current_polls_by_region(self, region):
        return self.pollService.get_current_polls_by_region(region)

    def get_polls_by_region_and_date(self, region, date):
        return self.pollService.get_polls_by_region_and_date(region, date)

    def get_polls_by_date(self, date):
        return self.pollService.get_polls_by_date(date)

    def get_all_historical_polls(self, year: str):
        return self.pollService.get_all_historical_polls(year)

    def get_all_candidates(self):
        return self.politicianService.get_all_candidates()

    def get_candidate_by_id(self, candidate_id: str):
        return self.politicianService.get_candidate_by_id(candidate_id)

    def get_candidates_by_party(self, party: str):
        return self.politicianService.get_candidates_by_party(party)

    def get_all_regions(self):
        return self.regionService.get_all_regions()

    def get_region_by_id(self, region_id: str):
        return self.regionService.get_region_by_id(region_id)

    def get_polls_by_region(self, region):
        return self.pollService.get_polls_by_region(region)

    def get_regions_by_election(self, election_id):
        return self.regionService.get_regions_by_election(election_id)

    def get_polls_by_election(self, election_id):
        return self.pollService.get_polls_by_election(election_id)

    def create_candidate(self, data):
        return self.politicianService.create_candidate(data)


if __name__ == '__main__':
    elections = Service().get_all_elections()
    polls = Service().get_all_polls()
    print()
