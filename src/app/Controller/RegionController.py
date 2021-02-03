from src.app.Service.Service import Service

class RegionController:

    def __init__(self):
        self.service = Service()

    def get_all_regions(self):
        return self.service.get_all_regions()

    def get_region_by_id(self, region_id: str):
        return self.service.get_region_by_id(region_id)

    def get_regions_by_election(self, election_id: str):
        return self.service.get_regions_by_election(election_id)
