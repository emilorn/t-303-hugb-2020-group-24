from src.app.Models.JsonEncoder import JsonEncoder




class CandidateDetailsDTO:

    '''
    candidateID: string
    name: string
    birthDate: string (optional)

    politicalParty: string (optional)

    bio: string (optional)

    region: [Region] (optional)

    agenda: string (optional)

    electionsWon: [string]  (optional)
    '''
    json_encoder = JsonEncoder()

    def __init__(self, candidate):
        self.candidateID = str(candidate.id)
        self.name = candidate.name
        self.birthDate = ""
        # self.politicalParty = candidate.political_party.name
        self.bio = ""
        # self.region = [""]
        self.agenda = ""
        # self.electionsWon = ""



    def to_json(self):
        return CandidateDetailsDTO.json_encoder.encode(self)
