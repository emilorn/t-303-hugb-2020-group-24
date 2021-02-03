from src.app.Models.JsonEncoder import JsonEncoder

class RegionDTO:

    json_encoder = JsonEncoder()

    def __init__(self, region):
        self.regionID = str(region.id)
        self.name = region.name

    def to_json(self):
        return RegionDTO.json_encoder.encode(self)