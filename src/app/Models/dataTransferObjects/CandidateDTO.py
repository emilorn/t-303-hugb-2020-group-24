from src.app.Models.JsonEncoder import JsonEncoder




class CandidateDTO:
    '''
    candidateID: string
    name: string
    politicalParty: string (optional)
    '''
    json_encoder = JsonEncoder()

    def __init__(self, candidate):

        self.candidateID = str(candidate.id)
        self.name = candidate.name
        # self.politicalParty = candidate.political_party.name


    def to_json(self):
        return CandidateDTO.json_encoder.encode(self)











