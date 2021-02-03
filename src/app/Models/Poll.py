from src.app.Models.JsonEncoder import JsonEncoder

class Poll:
    """
    Model Class to represent a PolL data in the system.
    Poll has association relationship with Candidate Model Class
    Poll has association relationship with Region Model Class
    """

    json_encoder = JsonEncoder()

    def __init__(self, poll_id, choices, start_date, end_date, is_open, region, results, election):
        self.end_date = end_date
        self.start_date = start_date
        self.results = results
        self.region = region
        self.is_open = is_open
        self.choices = choices
        self.id = poll_id
        self.election = election

    def __str__(self):
        result: str = "{:^30}{:^30}\n".format("Candidate", "No. Votes")
        for key, value in self.results.items():
            result += "{:<30}:{:^30}\n".format(key.name, value)
        poll: str = "Location  : {}\n" \
                    "Start date: {}\n" \
                    "End date  : {}\n" \
                    "Results: \n" \
                    "{}".format(self.region.name, self.start_date, self.end_date, result)
        return poll

    def to_json(self):
        temp_poll = Poll(self.id, self.choices, str(self.start_date), str(self.end_date), self.is_open, self.region, self.results)
        return Poll.json_encoder.encode(temp_poll)
