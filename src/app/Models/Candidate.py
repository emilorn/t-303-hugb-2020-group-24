from src.app.Models.JsonEncoder import JsonEncoder


class Candidate:
    """
    Model Class to represent a candidate data in the system.
    Candidate has association relationship with PoliticalParty Model Class
    Candidate has association relationship with Policy Model Class
    """

    json_encoder = JsonEncoder()

    def __init__(self, candidate_id, name, political_party, policies):
        self.id = candidate_id
        self.name = name
        self.political_party = political_party
        self.policies = policies

    def __str__(self):
        policy_str: str = ""
        for policy in self.policies:
            policy_str += str(policy) + "\n"
        return "{:<15}\t{:>60}\n{:^115}\n{}".format(self.name, str(self.political_party), "***Policies***", policy_str)

    def to_json(self):
        return Candidate.json_encoder.encode(self)
