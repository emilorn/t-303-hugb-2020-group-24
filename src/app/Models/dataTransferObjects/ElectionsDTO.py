from src.app.Models.JsonEncoder import JsonEncoder
from src.app.Models.dataTransferObjects.CandidateDTO import CandidateDTO


class ElectionDTO:
    json_encoder = JsonEncoder()

    def __init__(self, election):
        self.electionID = str(election.id)
        self.name = election.name
        self.candidates = []
        for candidate in election.candidates:
            self.candidates.append(CandidateDTO(candidate))
        self.votingDate = str(election.voting_date)

    def to_json(self):
        return ElectionDTO.json_encoder.encode(self)
