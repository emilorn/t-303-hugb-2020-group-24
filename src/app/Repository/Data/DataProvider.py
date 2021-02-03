from src.app.Models.Poll import Poll
from src.app.Models.Vote import Vote
from src.app.Models.Region import Region
from src.app.Models.Candidate import Candidate
from src.app.Models.Policy import Policy
from src.app.Models.MultiRegionalPoll import MultiRegionalPoll
from src.app.Models.PoliticalParty import PoliticalParty
from src.app.Models.Election import Election
from datetime import datetime
import os

# WORKING_DIR is to ensure the file path to all the
# CSV documents is compatible between different systems
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# ---CONSTANTS TO MATCH COLUMNS IN CSV DOCUMENTS --- #
# ---POLL CSV COLUMNS--- #
POLL_ID = 0
POLL_CHOICES = 1
POLL_START_DATE = 2
POLL_END_DATE = 3
POLL_IS_OPEN = 4
POLL_REGION = 5
POLL_RESULTS = 6
POLL_ELECTION_ID = 7

# ---POLL CSV COLUMNS--- #
MULTI_REGIONAL_POLL_ID = 0
MULTI_REGIONAL_POLL_CHOICES = 1
MULTI_REGIONAL_POLL_START_DATE = 2
MULTI_REGIONAL_POLL_END_DATE = 3
MULTI_REGIONAL_POLL_IS_OPEN = 4
MULTI_REGIONAL_POLL_REGIONS = 5
MULTI_REGIONAL_POLL_POLL_IDS = 6
MULTI_REGIONAL_POLL_RESULTS = 7
MULTI_REGIONAL_POLL_ELECTION_ID = 8

# ---CANDIDATES CSV COLUMNS--- #
CANDIDATE_ID = 0
CANDIDATE_NAME = 1
CANDIDATE_POLITICAL_PARTY = 2
CANDIDATE_POLICIES_IDS = 3

# ---POLICIES CSV COLUMNS--- #
POLICY_ID = 0
POLICY_CATEGORY = 1
POLICY_DESCRIPTION = 2

# ---POLITICAL PARTIES CSV COLUMNS--- #
POLITICAL_PARTY_ID = 0
POLITICAL_PARTY_NAME = 1

# ---REGION CSV COLUMNS--- #
REGION_ID = 0
REGION_ELECTORAL_VOTES = 1
REGION_NAME = 2

# ---VOTES CSV COLUMNS--- #
VOTE_ID = 0
VOTE_POLL_ID = 1
VOTE_CANDIDATE_ID = 2

# ---ELECTION CSV COLUMNS--- #
ELECTION_ID = 0
ELECTION_NAME = 1
ELECTION_CANDIDATES = 2
ELECTION_VOTING_DATE = 3



class DataProvider:
    """
    This class emulates a Database by reading and writing from/to selected CSV Documents
    """
    # --- FILE PATHS --- #
    FOLDER = "bank"
    polls_filename = os.path.join(WORKING_DIR, FOLDER + '/polls.csv')
    candidates_filename = os.path.join(WORKING_DIR, FOLDER + '/candidates.csv')
    regions_filename = os.path.join(WORKING_DIR, FOLDER + '/regions.csv')
    votes_filename = os.path.join(WORKING_DIR, FOLDER + '/votes.csv')
    policies_filename = os.path.join(WORKING_DIR, FOLDER + '/policies.csv')
    political_party_filename = os.path.join(WORKING_DIR, FOLDER + '/political_party.csv')
    multi_regional_polls_filename = os.path.join(WORKING_DIR, FOLDER + '/multi_regional_polls.csv')
    election_filename = os.path.join(WORKING_DIR, FOLDER + '/elections.csv')



    def __init__(self):
        self.political_parties = self.pull_political_parties_data()
        self.regions = self.pull_regions_data()
        self.policies = self.pull_policies_data()
        self.candidates = self.pull_candidates_data()
        self.elections = self.pull_all_elections()
        self.polls = self.pull_polling_data()
        self.multi_regional_polls = self.pull_multi_regional_polls()

        self.add_resource_dict = {
            'polls': DataProvider.add_poll,
            'candidate': DataProvider.add_candidate,
            'region': DataProvider.add_region,
            'vote': DataProvider.add_vote,
            'policy': DataProvider.add_policy,
            'political party': DataProvider.add_political_party,
            'multi region poll': DataProvider.add_multi_region_poll,
            'election': DataProvider.add_election
        }

        # self.votes = self.pull_votes_data()
        # Line 68 is not needed at this stage since we are not interested in Votes only the results from polls

    def pull_policies_data(self) -> list:
        """
        This method will create policy models from data retrieved in ./bank/policies.csv
        and return a list of all those objects.
        :return: list<Policy>
        """
        policies_stream = open(self.policies_filename)

        policies = []
        header = True  # To exclude the first line of the CSV (the header)
        for line in policies_stream:
            if not header:
                policy_row = line.split(",")
                policy_id = int(policy_row[POLICY_ID])
                category = policy_row[POLICY_CATEGORY]
                description = policy_row[POLICY_DESCRIPTION].strip()
                policies.append(Policy(policy_id, category, description))
            else:
                header = False
        policies_stream.close()
        return policies

    def pull_political_parties_data(self) -> list:
        """
        This method will create PoliticalParty models from data retrieved in ./bank/political_party.csv
        and return a list of all those objects.
        :return: list<PoliticalParty>
        """
        political_party_stream = open(self.political_party_filename)

        political_parties = []
        header = True  # To exclude the first line of the CSV (the header)
        for line in political_party_stream:
            if not header:
                political_party_row = line.split(",")
                political_party_id = int(political_party_row[POLITICAL_PARTY_ID])
                name = political_party_row[POLITICAL_PARTY_NAME].strip()
                political_parties.append(PoliticalParty(political_party_id, name))
            else:
                header = False
        political_party_stream.close()
        return political_parties

    def pull_candidates_data(self) -> list:
        """
        This method will create Candidate models from data retrieved from ./bank/Candidate.csv
        and return a list of all those objects.
        :return: list<Candidate>
        """
        candidate_stream = open(self.candidates_filename)
        political_parties = self.political_parties
        policies = self.policies

        candidates = []
        header = True  # To exclude the first line of the CSV (the header)
        for line in candidate_stream:
            if not header:
                candidate_row = line.split(",")
                candidate_id = int(candidate_row[CANDIDATE_ID])
                name = candidate_row[CANDIDATE_NAME].strip()
                political_party_id = int(candidate_row[CANDIDATE_POLITICAL_PARTY])
                political_party = None
                for party in political_parties:
                    if party.id == political_party_id:
                        political_party = party
                        break
                policies_ids = candidate_row[CANDIDATE_POLICIES_IDS]
                candidate_policies = []
                for policy in policies:
                    if str(policy.id) in policies_ids:
                        candidate_policies.append(policy)
                candidates.append(Candidate(candidate_id, name, political_party, candidate_policies))
            else:
                header = False
        candidate_stream.close()
        return candidates

    def pull_regions_data(self) -> list:
        """
        This method will create Region models from data retrieved from ./bank/regions.csv
        and return a list of all those objects.
        :return: list<Region>
        """
        region_stream = open(self.regions_filename)

        regions = []
        header = True  # To exclude the first line of the CSV (the header)
        for line in region_stream:
            if not header:
                region_row = line.split(",")
                region_id = int(region_row[REGION_ID])
                electoral_votes = int(region_row[REGION_ELECTORAL_VOTES])
                name = region_row[REGION_NAME].strip()
                regions.append(Region(region_id, name, electoral_votes))
            else:
                header = False
        region_stream.close()
        return regions

    def pull_polling_data(self) -> list:
        """
        This method will create Poll models from data retrieved from ./bank/polls.csv
        and return a list of all those objects.
        :return: list<Poll>
        """
        polls = []
        poll_stream = open(self.polls_filename)

        candidates = self.candidates
        regions = self.regions
        elections = self.elections

        # --Polls-- #
        header = True  # To exclude the first line of the CSV (the header)
        for line in poll_stream:
            if not header:
                poll = line.split(",")

                poll_id = int(poll[POLL_ID])
                candidates_ids = poll[POLL_CHOICES].split(";")
                start_date = datetime.strptime(poll[POLL_START_DATE], '%Y-%m-%d %H:%M:%S')
                end_date = datetime.strptime(poll[POLL_END_DATE], '%Y-%m-%d %H:%M:%S')
                is_open = True if poll[POLL_IS_OPEN] == "True" else False
                region_id = int(poll[POLL_REGION])

                # --Candidates--#
                candidate_list = []
                for candidate in candidates:
                    if str(candidate.id) in candidates_ids:
                        candidate_list.append(candidate)

                # --Region--#
                region_object = None
                for region in regions:
                    if region.id == int(region_id):
                        region_object = region

                # --Results--#
                results = poll[POLL_RESULTS].strip().split(";")  # Splitting on ; to get all the results in the poll
                result_dict = {}
                candidate_object = None
                for result in results:
                    candidate_id, score = result.split(":")  # Splitting on : to separate the candidate from his score
                    for candidate in candidates:
                        if candidate.id == int(candidate_id):
                            candidate_object = candidate
                    # Filling the dictionary with the candidates name as key and his score as the value
                    result_dict[candidate_object] = int(score)

                # --Election--#
                election_id = poll[POLL_ELECTION_ID].strip()
                election_object = None
                for election in elections:
                    if election.id is int(election_id):
                        election_object = election

                new_poll = Poll(poll_id, candidate_list, start_date, end_date, is_open, region_object, result_dict,
                                election_object)
                polls.append(new_poll)
            else:
                header = False
        poll_stream.close()
        return polls

    def pull_votes_data(self) -> list:
        """
        This method will create Vote models from data retrieved from ./bank/polls.csv
        and return a list of all those objects.
        :return: list<Vote>
        """
        votes_stream = open(self.votes_filename)

        polls = self.pull_polling_data()
        candidates = self.pull_candidates_data()

        votes = []
        header = True  # To exclude the first line of the CSV (the header)
        for line in votes_stream:
            if not header:
                vote_row = line.split(",")
                vote_id = int(vote_row[VOTE_ID])
                poll_id = int(vote_row[VOTE_POLL_ID])
                candidate_id = int(vote_row[VOTE_CANDIDATE_ID])

                poll_object = None
                for poll in polls:
                    if poll.id == poll_id:
                        poll_object = poll

                candidate_object = None
                for candidate in candidates:
                    if candidate.id == candidate_id:
                        candidate_object = candidate

                votes.append(Vote(vote_id, poll_object, candidate_object))
            else:
                header = False
        votes_stream.close()
        return votes

    def pull_multi_regional_polls(self):
        multi_regional_polls = []
        multi_regional_polls_stream = open(self.multi_regional_polls_filename)

        candidates = self.candidates
        elections = self.elections

        # --Polls-- #
        header = True  # To exclude the first line of the CSV (the header)
        for line in multi_regional_polls_stream:
            if not header:
                multi_regional_poll = line.split(",")

                multi_regional_poll_id = int(multi_regional_poll[MULTI_REGIONAL_POLL_ID])
                candidates_ids = multi_regional_poll[MULTI_REGIONAL_POLL_CHOICES].split(";")
                start_date = datetime.strptime(multi_regional_poll[MULTI_REGIONAL_POLL_START_DATE], '%Y-%m-%d %H:%M:%S')
                end_date = datetime.strptime(multi_regional_poll[MULTI_REGIONAL_POLL_END_DATE], '%Y-%m-%d %H:%M:%S')
                is_open = True if multi_regional_poll[MULTI_REGIONAL_POLL_IS_OPEN] == "True" else False
                region_ids = multi_regional_poll[MULTI_REGIONAL_POLL_REGIONS].split(";")
                poll_ids = multi_regional_poll[MULTI_REGIONAL_POLL_POLL_IDS].split(";")

                # --Region--#
                regions = []
                for region in region_ids:
                    for region_object in self.regions:
                        if region_object.id == int(region):
                            regions.append(region_object)

                # --- polls ---- #
                polls = []
                for poll in poll_ids:
                    for poll_object in self.polls:
                        if poll_object.id == int(poll):
                            polls.append(poll_object)

                # --Candidates--#
                candidate_list = []
                for candidate in candidates:
                    if str(candidate.id) in candidates_ids:
                        candidate_list.append(candidate)

                # --Results--#
                results = multi_regional_poll[MULTI_REGIONAL_POLL_RESULTS].strip().split(
                    ";")  # Splitting on ; to get all the results in the poll
                result_dict = {}
                candidate_object = None
                for result in results:
                    candidate_id, score = result.split(":")  # Splitting on : to separate the candidate from his score
                    for candidate in candidates:
                        if candidate.id == int(candidate_id):
                            candidate_object = candidate
                    # Filling the dictionary with the candidates name as key and his score as the value
                    result_dict[candidate_object] = int(score)

                # --Election--#
                election_id = multi_regional_poll[MULTI_REGIONAL_POLL_ELECTION_ID].strip()
                election_object = None
                for election in elections:
                    if election.id is int(election_id):
                        election_object = election

                new_multi_regional_poll = MultiRegionalPoll(multi_regional_poll_id,
                                                            start_date,
                                                            end_date,
                                                            is_open,
                                                            candidate_list,
                                                            regions,
                                                            polls,
                                                            result_dict,
                                                            election_object)

                # id, start_date, end_date, is_open, choices, regions, pollIds, overallResults
                multi_regional_polls.append(new_multi_regional_poll)
            else:
                header = False
        multi_regional_polls_stream.close()
        return multi_regional_polls

    def pull_all_elections(self):
        election_stream = open(self.election_filename)

        candidates = self.candidates

        elections = []
        header = True
        for line in election_stream:
            if not header:
                election_data = line.split(",")

                election_id = int(election_data[ELECTION_ID])
                election_name = election_data[ELECTION_NAME]
                election_candidates_ids = election_data[ELECTION_CANDIDATES].split(";")
                election_voting_date = datetime.strptime(election_data[ELECTION_VOTING_DATE].strip(), '%Y-%m-%d '
                                                                                                      '%H:%M:%S')

                election_candidates = []
                # --Candidates--#
                candidate_list = []
                for candidate in candidates:
                    if str(candidate.id) in election_candidates_ids:
                        candidate_list.append(candidate)

                elections.append(Election(election_id, election_name, candidate_list, election_voting_date))
            else:
                header = False
        return elections

    def add_candidate(self, data):
        id = len(self.candidates)+1
        name = data["name"]
        political_party = data["politicalParty"]
        policy_id = self.add_policy(data)

        for party in self.political_parties:
            party_id = party.id if party.name == political_party else None

        if party_id is None:
            party_id = self.add_political_party(data)

        with open(self.candidates_filename, "a") as f:
            f.write(f"{id},{name},{party_id},{policy_id}\n")

        self.candidates = self.pull_candidates_data()
        return id

    def add_poll(self, data):
        raise NotImplementedError()

    def add_vote(self, data):
        raise NotImplementedError()

    def add_region(self, data):
        raise NotImplementedError()

    def add_multi_region_poll(self, data):
        raise NotImplementedError()

    def add_policy(self, data):
        id = len(self.policies)+1
        agenda = data["agenda"]
        category = "Undefined"

        with open(self.policies_filename, "a") as f:
            f.write(f"{id},{category},{agenda}\n")

        self.policies = self.pull_policies_data()
        return id

    def add_political_party(self, data):
        id = len(self.political_parties)+1
        name = data["politicalParty"]

        with open(self.political_party_filename, "a") as f:
            f.write(f"{id},{name}\n")

        self.political_parties = self.pull_political_parties_data()
        return id

    def add_election(self, data):
        raise NotImplementedError()

    def create_resouce(self, data, resource_type: str) -> object:
        if resource_type == "candidate":
             id = self.add_candidate(data)
        return id





if __name__ == '__main__':
    new_db = DataProvider()

    poll = new_db.polls[0]
    multi_reg = new_db.multi_regional_polls[0]
