from src.app.Service.Service import Service


class ElectionController:

    def __init__(self):
        self.service = Service()

    def get_election_by_id(self, election_id):
        return self.service.get_election_by_id(election_id)
