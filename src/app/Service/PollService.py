from src.app.Models.MultiRegionalPoll import MultiRegionalPoll
from src.app.Models.Poll import Poll
from src.app.Repository.Repository import Repository
from src.app.Models.dataTransferObjects.PollDTO import PollDTO
from src.app.Models.dataTransferObjects.ElectionsDTO import ElectionDTO


class PollService:
    def __init__(self):
        self.repository = Repository()

    def get_all_polls(self):
        return [PollDTO(poll) for poll in self.repository.get_all_polls()] #+ self.repository.get_all_multi_regional_polls()]

    def get_average_poll(self, electionID: str):
        polls = self.repository.get_polls_by_election(electionID)
        election = self.repository.get_election_by_id(electionID)
        if len(polls) < 1: raise Exception("election has no polls, cannot calculate average")

        first = polls[0].start_date
        last = polls[0].end_date
        regions = [polls[0].region]

        choices = polls[0].choices
        avg_result = {}
        for choice in choices:
            avg_result[choice] = 0

        for poll in polls:
            for key, value in poll.results.items():
                avg_result[key] = avg_result[key] + value

            if poll.start_date < first:
                first = poll.start_date
            if poll.end_date > last:
                last = poll.end_date
            if poll.region not in regions:
                regions.append(poll.region)

        for key in avg_result:
            avg_result[key] = avg_result[key] / len(polls)

        avg_poll = MultiRegionalPoll(None, first, last, False, choices, regions, polls, avg_result, election)
        # avg_poll = Poll(None, choices, first, last, False, None, avg_result, election)

        return PollDTO(avg_poll)

    def get_all_elections(self):
        return [ElectionDTO(election) for election in self.repository.get_all_elections()]

    def get_all_current_polls(self):
        return [PollDTO(poll) for poll in self.repository.get_all_current_polls()]

    def get_current_polls_by_region(self, regionID):
        return [PollDTO(poll) for poll in self.repository.get_current_polls_by_region(regionID)]

    def get_polls_by_region_and_date(self, regionID: str, date: str):
        return [PollDTO(poll) for poll in self.repository.get_polls_by_region_and_date(regionID, date)]

    def get_polls_by_date(self, date: str):
        return [PollDTO(poll) for poll in self.repository.get_polls_by_date(date)]

    def get_all_historical_polls(self, year: str):
        return [PollDTO(poll) for poll in self.repository.get_historical_polls(year)]

    def get_polls_by_region(self, region):
        return [PollDTO(poll) for poll in self.repository.get_polls_by_region(region)]

    def get_election_by_id(self, election_id):
        return ElectionDTO(self.repository.get_election_by_id(election_id))

    def get_polls_by_election(self, election_id):
        return [PollDTO(poll) for poll in self.repository.get_polls_by_election(election_id)]


if __name__ == '__main__':

    thing = PollService()
    polls = thing.get_all_polls()
    print(polls[-1].to_json())