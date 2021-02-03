from src.app.Models.JsonEncoder import JsonEncoder

class Region:
    """
    Model Class to represent a Region data in the system.
    Region has association relationship with Poll Model Class
    """

    json_encoder = JsonEncoder()

    def __init__(self, id, name, electoral_votes=None):
        self.id = id
        self.electoral_votes = electoral_votes
        self.name = name

    def __str__(self):
        return "{}\n" \
               "Electoral Votes: {}".format(self.name, self.electoral_votes)

    def to_json(self):
        return Region.json_encoder.encode(self)