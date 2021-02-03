class CandidateRepository:

    def __init__(self, data_provider):
        self.__db = data_provider

    def get_all_candidates(self) -> list:
        return self.__db.candidates

    def get_candidate_by_id(self, candidate_id: str):
        return next((candidate for candidate in self.__db.candidates if int(candidate_id) == candidate.id), None)

    def get_candidates_by_party(self, party: str) -> list:
        return [candidate for candidate in self.__db.candidates if candidate.political_party.id == int(party)]

    def create_candidate(self, data):
        id = self.__db.create_resouce(data, "candidate")
        return next((candidate for candidate in self.__db.candidates if candidate.id == id))
