from src.app.Repository.PollRepository import PollRepository
from src.app.Repository.CandidateRepository import CandidateRepository
from src.app.Repository.RegionRepository import RegionRepository
from src.app.Repository.PolicyRepository import PolicyRepository
from src.app.Repository.Data.DataProvider import DataProvider


class Repository:

    def __init__(self):
        self.__db = DataProvider()
        self.__poll_repo = PollRepository(self.__db)
        self.__region_repo = RegionRepository(self.__db)
        self.__candidate_repo = CandidateRepository(self.__db)
        self.__policy_repo = PolicyRepository(self.__db)

    # ------- POLLS ---------- #

    def get_all_polls(self):
        return self.__poll_repo.get_all_polls()

    def get_all_multi_regional_polls(self):
        return self.__poll_repo.get_all_multi_regional_polls()

    def get_all_elections(self):
        return self.__poll_repo.get_all_elections()

    def get_all_current_polls(self):
        return self.__poll_repo.get_all_current_polls()

    def get_current_polls_by_region(self, region):
        return self.__poll_repo.get_current_polls_by_region(region)

    def get_polls_by_region_and_date(self, region, date):
        return self.__poll_repo.get_polls_by_region_and_date(region, date)

    def get_polls_by_date(self, date: str):
        return self.__poll_repo.get_polls_by_date(date)

    def get_historical_polls(self, year: str):
        return self.__poll_repo.get_historical_polls(year)

    def get_election_by_id(self, election_id: str):
        return self.__poll_repo.get_election_by_id(election_id)


    # -------- CANDIDATES --------- #

    def get_all_candidates(self):
        return self.__candidate_repo.get_all_candidates()

    def get_candidate_by_id(self, candidate_id: str):
        return self.__candidate_repo.get_candidate_by_id(candidate_id)

    def get_candidates_by_party(self, party: str):
        return self.__candidate_repo.get_candidates_by_party(party)

    def get_all_regions(self):
        return self.__region_repo.get_all_regions()

    def get_region_by_id(self, region_id: str):
        return self.__region_repo.get_region_by_id(region_id)

    def get_polls_by_region(self, region):
        return self.__poll_repo.get_polls_by_region(region)

    def get_polls_by_election(self, election_id):
        return self.__poll_repo.get_polls_by_election(election_id)

    def get_regions_by_election(self, polls: list):
        return self.__region_repo.get_regions_by_election(polls)

    def create_candidate(self, data):
        return self.__candidate_repo.create_candidate(data)


if __name__ == '__main__':
    repo = Repository()
    election = repo.get_election_by_id("1")
    print()



