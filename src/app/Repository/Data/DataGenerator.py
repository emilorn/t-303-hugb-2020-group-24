import random
import datetime

CANDIDATES = [0, 1]

ELECTORAL_VOTES = {
    'Alabama': 9,
    'Alaska': 3,
    'Arizona': 11,
    'Arkansas': 6,
    'California': 55,
    'Colorado': 9,
    'Connecticut': 7,
    'Delaware': 3,
    'Florida': 29,
    'Georgia': 16,
    'Hawaii': 4,
    'Idaho': 4,
    'Illinois': 4,
    'Indiana': 11,
    'Iowa': 6,
    'Kansas': 6,
    'Kentucky': 8,
    'Louisiana': 8,
    'Maine': 4,
    'Maryland': 10,
    'Massachusetts': 11,
    'Michigan': 16,
    'Minnesota': 10,
    'Mississippi': 6,
    'Missouri': 10,
    'Montana': 3,
    'Nebraska': 5,
    'Nevada': 6,
    'New Hampshire': 4,
    'New Jersey': 14,
    'New Mexico': 5,
    'New York': 29,
    'North Carolina': 15,
    'North Dakota': 3,
    'Ohio': 18,
    'Oklahoma': 7,
    'Oregon': 7,
    'Pennsylvania': 20,
    'Rhode Island': 4,
    'South Carolina': 9,
    'South Dakota': 3,
    'Tennessee': 11,
    'Texas': 38,
    'Utah': 6,
    'Vermont': 3,
    'Virginia': 13,
    'Washington': 12,
    'West Virginia': 5,
    'Wisconsin': 10,
    'Wyoming': 3}

STATES = ['Alabama',
          'Alaska',
          'Arizona',
          'Arkansas',
          'California',
          'Colorado',
          'Connecticut',
          'Delaware',
          'Florida',
          'Georgia',
          'Hawaii',
          'Idaho',
          'Illinois',
          'Indiana',
          'Iowa',
          'Kansas',
          'Kentucky',
          'Louisiana',
          'Maine',
          'Maryland',
          'Massachusetts',
          'Michigan',
          'Minnesota',
          'Mississippi',
          'Missouri',
          'Montana',
          'Nebraska',
          'Nevada',
          'New Hampshire',
          'New Jersey',
          'New Mexico',
          'New York',
          'North Carolina',
          'North Dakota',
          'Ohio',
          'Oklahoma',
          'Oregon',
          'Pennsylvania',
          'Rhode Island',
          'South Carolina',
          'South Dakota',
          'Tennessee',
          'Texas',
          'Utah',
          'Vermont',
          'Virginia',
          'Washington',
          'West Virginia',
          'Wisconsin',
          'Wyoming'
          ]

COUNTRY = "United States of America"


class DataGenerator:
    """
    Class has functions to create a series of CSV documents with Region data, Vote Data and Polling Data
    """
    BEGIN_DATE = datetime.datetime(2016, 1, 1)
    END_DATE = datetime.datetime(2020, 11, 3)
    # More recent date is "bigger" than one prior
    POLLS = []
    REGIONS = []
    NEXT_POLL_ID = 0
    NEXT_VOTE_ID = 0
    NEXT_REGION_ID = 0
    NEXT_MULTI_REGIONAL_POLL = 0
    FOLDER = "bank"

    def __init__(self):
        pass

    @staticmethod
    def get_date_between_dates(start_date: datetime, end_date: datetime) -> datetime:
        """
        Returns a random date between start_date and end_date
        :param start_date: datetime
        :param end_date: datetime
        :return: datetime
        """
        time_between_dates = end_date - start_date
        if end_date == start_date:
            return start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def generate_poll_csv(self) -> None:
        """
        Creates a CSV document with Polling Data
        """
        poll_string = "id,choices,start_date,end_date,is_open,region,results,election_id\n"
        vote_string = "id,poll_id,date,vote\n"
        for x in range(500):

            start_date = self.get_date_between_dates(self.BEGIN_DATE, self.END_DATE)
            end_date = self.get_date_between_dates(start_date, self.END_DATE)
            poll_string += str(self.NEXT_POLL_ID) + ",0;1," + str(start_date) + "," + \
                           str(end_date) + "," + str(end_date > datetime.datetime.now()) + "," \
                           + str(random.randint(0, len(STATES) - 1)) + ","

            result = {0: 0, 1: 0}
            for i in range(500, random.randint(501, 1500)):
                vote_string += str(self.NEXT_VOTE_ID) + "," + str(self.NEXT_POLL_ID) + "," \
                               + str(self.get_date_between_dates(start_date, end_date)) + ","
                vote = random.choice(CANDIDATES)
                result[vote] += 1
                vote_string += str(vote) + "\n"
                self.NEXT_VOTE_ID += 1

            poll_string += "0:" + str(result[0]) + ";1:" + str(result[1]) + "," + str(random.randint(0, 1)) + "\n"
            self.NEXT_POLL_ID += 1

        with open("./" + self.FOLDER + "/polls.csv", "w") as file:
            file.write(poll_string)
        with open("./" + self.FOLDER + "/votes.csv", "w") as file:
            file.write(vote_string)

    def generate_multi_regional_poll(self) -> None:
        """
        Creates a CSV document with Polling Data
        """
        multi_region_poll_string = \
            "id,choices,start_date,end_date,is_open,regions,poll_ids,overall_result,election_id\n"
        poll_string = ""
        vote_string = ""

        for y in range(20):  # number of multi regional polls
            state_set = set()  # regions to be used
            start_date = self.get_date_between_dates(self.BEGIN_DATE, self.END_DATE)
            overall_result = {0: 0, 1: 0}
            election = str(random.randint(0, 1))
            end_date = self.get_date_between_dates(start_date, self.END_DATE)
            multi_region_poll_string += str(self.NEXT_MULTI_REGIONAL_POLL) + ",0;1," + str(start_date) + "," \
                + str(end_date) + "," + str(end_date > datetime.datetime.now()) + ","

            for x in range(50):
                state_set.add(str(random.randint(0, len(STATES)-1)))

            for region in state_set:
                multi_region_poll_string += region + ";"

            multi_region_poll_string = multi_region_poll_string[:-1] + ","

            # ---- make polls ------
            for region in state_set:

                poll_string += str(self.NEXT_POLL_ID) + ",0;1," + str(start_date) + "," + \
                               str(end_date) + "," + str(end_date > datetime.datetime.now()) + "," \
                               + region + ","

                poll_result = {0: 0, 1: 0}

                for i in range(500, random.randint(501, 1500)):
                    vote_string += str(self.NEXT_VOTE_ID) + "," + str(self.NEXT_POLL_ID) + "," \
                                   + str(self.get_date_between_dates(start_date, end_date)) + ","
                    vote = random.choice(CANDIDATES)
                    poll_result[vote] += 1
                    vote_string += str(vote) + "\n"
                    self.NEXT_VOTE_ID += 1

                poll_string += "0:" + str(poll_result[0]) + ";1:" + str(poll_result[1]) + "," + election + "\n"
                multi_region_poll_string += str(self.NEXT_POLL_ID) + ";"
                overall_result[0] += poll_result[0]  # A little bit of hard coding, sue me
                overall_result[1] += poll_result[1]
                self.NEXT_POLL_ID += 1
            multi_region_poll_string = multi_region_poll_string[:-1] + ",0:" + str(overall_result[0]) + ";1:" \
                                       + str(overall_result[1]) + "," + election + "\n"
            self.NEXT_MULTI_REGIONAL_POLL += 1

        with open("./" + self.FOLDER + "/polls.csv", "a") as file:
            file.write(poll_string)
        with open("./" + self.FOLDER + "/votes.csv", "a") as file:
            file.write(vote_string)
        with open("./" + self.FOLDER + "/multi_regional_polls.csv", "w") as file:
            file.write(multi_region_poll_string)


    def generate_region_csv(self) -> None:
        """
        Creates a CSV document with Region data
        """
        region_string = "id,electoral_votes,name\n"
        for region in STATES:
            region_string += str(self.NEXT_REGION_ID) + "," + str(ELECTORAL_VOTES[region]) + "," + region + "\n"
            self.NEXT_REGION_ID += 1
        with open("./" + self.FOLDER + "/regions.csv", "w") as file:
            file.write(region_string)


if __name__ == '__main__':
    thing = DataGenerator()
    thing.generate_poll_csv()
    thing.generate_region_csv()
    thing.generate_multi_regional_poll()
