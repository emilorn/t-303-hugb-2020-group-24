from src.app.Models.JsonEncoder import JsonEncoder
from src.app.Models.dataTransferObjects.CandidateDetailsDTO import CandidateDetailsDTO
from src.app.Models.dataTransferObjects.RegionDTO import RegionDTO
from src.app.Models.dataTransferObjects.ElectionsDTO import ElectionDTO

class PollDTO:

    json_encoder = JsonEncoder()

    class __RegionPoll:
        def __init__(self, data, region):
            self.data = data
            self.region = RegionDTO(region)

    class __PollData:

        def __init__(self, candidate, votes):
            self.candidate = CandidateDetailsDTO(candidate)
            self.votes = votes


    def __init__(self, poll):
        self.pollID = str(poll.id)
        self.dataArray = []
        self.year = poll.start_date.year
        self.organization = ""
        self.election = ElectionDTO(poll.election)
        self.pollDate = ""
        self.url = ""

        if(type(poll).__name__ == "MultiRegionalPoll"):
            self.__convert_multi_regional_poll_to_pollDTO(poll)

        elif(type(poll).__name__ == "Poll"):
            self.__convert_poll_to_pollDTO(poll)


    def __convert_poll_to_pollDTO(self, poll):
        data = [PollDTO.__PollData(candidate, votes) for candidate, votes in poll.results.items()]
        self.dataArray = [PollDTO.__RegionPoll(data, poll.region)]


    def __convert_multi_regional_poll_to_pollDTO(self, multi_regional_poll):
        region_polls = []
        for poll in multi_regional_poll.includedPolls:
            data = [PollDTO.__PollData(candidate, votes) for candidate, votes in poll.results.items()]
            region_polls.append(PollDTO.__RegionPoll(data, poll.region))
        self.dataArray = region_polls

    def to_json(self):
        return PollDTO.json_encoder.encode(self)








