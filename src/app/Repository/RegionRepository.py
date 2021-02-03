from src.app.Repository.Data.DataProvider import DataProvider

class RegionRepository:

    def __init__(self, data_provider):
        self.__db = data_provider

    def get_all_regions(self) -> list:
        return self.__db.regions

    def get_region_by_id(self, region_id: str):
        return next((region for region in self.__db.regions if int(region_id) == region.id), None)

    def get_regions_by_election(self, polls: list):
        region_arr = []
        for poll in polls:
            if poll.region not in region_arr:
                region_arr.append(poll.region)
        return region_arr

        #return [region for region in self.__db.regions if region.name == polls.region]
        #return [region for region in self.__db.regions if region.id == int(region_id)]