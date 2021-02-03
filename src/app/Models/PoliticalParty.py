from src.app.Models.JsonEncoder import JsonEncoder

class PoliticalParty:
    """
    Model Class to represent a PoliticalParty data in the system.
    PoliticalParty has a association relationship with Candidate Model Class
    """

    json_encoder = JsonEncoder()

    def __init__(self, political_party_id, name):
        self.id = political_party_id
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

    def to_json(self):
        return PoliticalParty.json_encoder.encode(self)

