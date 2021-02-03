from datetime import datetime
from datetime import timedelta

class PollRepository:

    def __init__(self, data_provider):
        self.__db = data_provider
        print()

    def get_all_polls(self):
        return self.__db.polls

    def get_all_multi_regional_polls(self):
        return self.__db.multi_regional_polls

    def get_all_elections(self):
        return self.__db.elections

    def get_election_by_id(self, election_id: str):
        return next((election for election in self.__db.elections if int(election_id) == election.id), None)

    def get_polls_by_date(self, date: str):
        # Make a datetime object out of the date string given
        date_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        poll_list = []

        for poll in self.__db.polls:
            # get all polls who are taking place during the given date
            if poll.start_date < date_object < poll.end_date:
                poll_list.append(poll)
        return poll_list

    def get_polls_by_region_and_date(self, region_id: str, date: str):
        # Make a datetime object out of the date string given
        date_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        poll_list = []

        for poll in self.__db.polls:
            # get all polls who are taking place during the given date, and are in the given region
            if poll.start_date < date_object < poll.end_date and int(region_id) == poll.region.id:
                poll_list.append(poll)
        return poll_list

    def get_current_polls_by_region(self, region_id: str):
        return [poll for poll in self.__db.polls if poll.region.id == int(region_id) and poll.is_open]  # Returns all open polls for selected region

    def get_all_current_polls(self):
        return [poll for poll in self.__db.polls if poll.is_open is True]  # Returns all open polls

    def get_historical_polls(self, year):
        poll_list = []
        year_begin = datetime.strptime(str(year), '%Y')
        year_end = datetime.strptime(str(int(year)+1), '%Y') - timedelta(milliseconds=1)
        for poll in self.__db.polls:
            if poll.end_date >= year_begin and poll.start_date <= year_end:
                poll_list.append(poll)

        return poll_list

    def get_polls_by_region(self, region):
        return [poll for poll in self.__db.polls if poll.region.id == int(region)]

    def get_polls_by_election(self, election_id):
        pollList = []
        for poll in self.__db.polls:
            if poll.election:
                if poll.election.id == int(election_id):
                    pollList.append(poll)
        return pollList






