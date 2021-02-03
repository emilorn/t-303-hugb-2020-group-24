from src.app.Service.Service import Service
class CandidateController:
    def __init__(self):
        self.service = Service()

    def get_all_candidates(self):
        return self.service.get_all_candidates()

    def get_candidate_by_id(self, candidate_id: str):
        return self.service.get_candidate_by_id(candidate_id)

    def get_candidates_by_party(self, party: str):
        return self.service.get_candidates_by_party(party)

    def create_candidate(self, data):
        return self.service.create_candidate(data)
