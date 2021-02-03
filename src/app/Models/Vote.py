from src.app.Models.JsonEncoder import JsonEncoder

class Vote:
    """
    Model Class to represent a Vote data in the system.
    Vote has association relationship with Candidate Model Class
    Vote has association relationship with Poll Model Class
    """

    json_encoder = JsonEncoder()

    def __init__(self, id, poll, candidate):
        self.id = id
        self.poll = poll
        self.candidate = candidate

    def to_json(self):
        return Vote.json_encoder.encode(self)
