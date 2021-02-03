from src.app.Service.Service import Service

class PollController:

    def __init__(self):
        self.service = Service()

    def get_all_polls(self):
        polls = self.service.get_all_polls()
        return polls

    def get_average_poll(self, electionID: str):
        return self.service.get_average_poll(electionID)

    def get_all_current_polls(self):
        return self.service.get_all_current_polls()

    def get_current_polls_by_region(self, regionID: str):
        return self.service.get_current_polls_by_region(regionID)

    def get_polls_by_region_and_date(self, regionID: str, date: str):
        return self.service.get_polls_by_region_and_date(regionID, date)

    def get_polls_by_date(self, date: str):
        return self.service.get_polls_by_date(date)

    def get_all_historical_polls(self, year: str):
        return self.service.get_all_historical_polls(year)

    def get_polls_by_region(self, region):
        return self.service.get_polls_by_region(region)

    def get_polls_by_election(self, election):
        return self.service.get_polls_by_election(election)

