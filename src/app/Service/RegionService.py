from src.app.Repository.Repository import Repository
from src.app.Models.dataTransferObjects.RegionDTO import RegionDTO


class RegionService:
    def __init__(self):
        self.repository = Repository()

    def get_all_regions(self):
        #all_regions = self.repository.get_all_regions()
        return [RegionDTO(region) for region in self.repository.get_all_regions()]

    def get_region_by_id(self, region_id: str):
        return RegionDTO(self.repository.get_region_by_id(region_id))

    def get_regions_by_election(self, election_id):
        all_election_polls = self.repository.get_polls_by_election(election_id)
        return [RegionDTO(region) for region in self.repository.get_regions_by_election(all_election_polls)]






