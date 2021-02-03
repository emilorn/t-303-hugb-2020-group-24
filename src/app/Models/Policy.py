from src.app.Models.JsonEncoder import JsonEncoder

class Policy:
    """
    Model Class to represent a policy data in the system.
    Policy has a association relationship with Candidate Model Class
    """
    json_encoder = JsonEncoder()

    def __init__(self, policy_id, category, description):
        self.id = policy_id
        self.category = category
        self.description = description

    def __str__(self):
        return "{:<15}:\t{:>100}".format(self.category, self.description)


    def to_json(self):
        return Policy.json_encoder.encode(self)


