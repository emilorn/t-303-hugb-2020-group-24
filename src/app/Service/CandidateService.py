from src.app.Repository.Repository import Repository
from src.app.Models.dataTransferObjects.CandidateDetailsDTO import CandidateDetailsDTO
from src.app.Models.dataTransferObjects.CandidateDTO import CandidateDTO


class CandidateService:
    def __init__(self):
        self.repository = Repository()

    def get_all_candidates(self):
        return [CandidateDTO(candidate) for candidate in self.repository.get_all_candidates()]

    def get_candidate_by_id(self, candidate_id: str):
        return CandidateDetailsDTO(self.repository.get_candidate_by_id(candidate_id))

    def get_candidates_by_party(self, party: str):
        return [CandidateDTO(candidate) for candidate in self.repository.get_candidates_by_party(party)]

    def create_candidate(self, data):
        return CandidateDetailsDTO(self.repository.create_candidate(data))
