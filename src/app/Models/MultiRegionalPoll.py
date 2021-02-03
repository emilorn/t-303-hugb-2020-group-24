from src.app.Models.JsonEncoder import JsonEncoder



class MultiRegionalPoll:
    json_encoder = JsonEncoder()

    def __init__(self, id, start_date, end_date, is_open, choices, regions, pollsList, overallResults, election):
        self.id = id
        self.choices = choices
        self.start_date = start_date
        self.end_date = end_date
        self.is_open = is_open
        self.regions = regions
        self.includedPolls = pollsList
        self.overallResults = overallResults
        self.election = election

    def to_json(self):
        return MultiRegionalPoll.json_encoder.encode(self)