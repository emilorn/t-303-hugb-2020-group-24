import asyncio
import websockets
import json
from src.app.Controller.Controller import Controller

from src.app.Models.JsonEncoder import JsonEncoder


class ComponentInterface:
    def __init__(self):
        self.controller = Controller()

    # ---- POLL METHODS START ----
    def getAllPolls(self, data):
        return self.controller.get_all_polls()

    def getAveragePoll(self, data):
        election = data["electionID"]
        return self.controller.get_average_poll(election)

    def getPollPerRegion(self, data):
        region = data["regionID"]
        polls_per_region = self.controller.get_polls_by_region(region)
        return polls_per_region

    def getPollPerElection(self, data):
        election = data["electionID"]
        return_value = self.controller.get_polls_by_election(election)
        return return_value

    def getHistoricalPolls(self, data):
        date = data["year"]
        polls_historical = self.controller.get_all_historical_polls(date)
        return self.controller.get_all_historical_polls(date)

    def get_all_current_polls(self, data):
        poll_arr = []
        polls_current = self.controller.get_all_current_polls()
        for poll in polls_current:
            poll_json = poll.to_json()
            poll_arr.append(poll_json)
        return poll_arr

    def get_polls_by_region_and_date(self, data):
        region = data["region"]
        date = data["date"]
        polls_json = []
        polls = self.controller.get_polls_by_region_and_date(region, date)
        for poll in polls:
            poll_json = poll.to_json()
            polls_json.append(poll_json)
        return polls_json
    # ---- POLL METHODS END ----

    # ---- REGION METHODS START ----
    def getRegionDetails(self, data):
        region_id = data["regionID"]
        region = self.controller.get_region_by_id(region_id)
        return region

    def getRegions(self, data):
        all_regions = self.controller.get_all_regions()
        return all_regions
        #return self.controller.get_all_regions()

    def getAllRegions(self, data):
        election_id = data["electionID"]
        regions = self.controller.get_regions_by_election(election_id)
        return regions

    # ---- REGION METHODS END ----

    # ---- CANDIDATE METHODS START ----
    def createCandidate(self, data):
        return self.controller.create_candidate(data)

    def getCandidates(self, data):
        return self.controller.get_all_candidates()

    def getCandidateDetails(self, data):
        candidate_id = data["candidateID"]
        candidate = self.controller.get_candidate_by_id(candidate_id)
        return candidate

    def getPartyCandidates(self, data):
        party = data["party"]
        candidate_arr = []
        party_candidates = self.controller.get_candidates_by_party(party)
        for candidate in party_candidates:
            candidate_json = candidate.to_json()
            candidate_arr.append(candidate_json)
        return candidate_arr
    # ---- CANDIDATE METHODS END ----
    # ---- ELECTION METHODS START ----
    def getElectionDetails(self, data):
        election = data["electionID"]
        return self.controller.get_election_by_id(election)
    # ---- ELECTION METHODS END ----



class ComponentPort:
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method"""
        if ComponentPort.__instance is None:
            __instance = ComponentPort()

        return __instance

    def __init__(self):
        self.interface = ComponentInterface()

    async def __msg_handler(self, websocket, path):
        msg = await websocket.recv()
        body = json.loads(msg)

        try:
            if "data" in body:
                print("Trying to call {}, with data {}".format(body["op"], body["data"]), end="")
                op_return = getattr(self.interface, body["op"])(body["data"])
            else:
                print("Trying to call {}".format(body["op"]), end="")
                op_return = getattr(self.interface, body["op"])()

            return_value = json.dumps({"msg": op_return}, cls=JsonEncoder)
            print(" -> Success!")
        except Exception as e:
            print(" -> Error!")
            return_value = json.dumps({"msg": "Oops! An error has occurred", "error": str(e)})

        await websocket.send(return_value)

    def start(self):

        start_server = websockets.serve(self.__msg_handler, "localhost", 8080)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    compPort = ComponentPort.get_instance()
    compPort.start()
