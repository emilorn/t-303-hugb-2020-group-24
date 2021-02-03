from src.app.Controller.Controller import Controller


class Main:
    def __init__(self):
        raise NotImplemented()

    # not implemented yet

    def main(self, functions):
        exit = False
        while exit != True:
            for function in functions:
                print(function)
            print()
            _input_ = input("Input function for test: ")
            if _input_ == "0":
                break
            controller_instance = Controller()
            controller_instance.input_parser(_input_)


# Main start here


def main():
    functions = ["\n1: See politician profiles",
                 "2: See polling data for entire country",
                 "3: See polling data for individual region",
                 "4: See polling data for both individual region and entire country",
                 "5: See polling data history for individual region",
                 "6: See results from previous polls\n",
                 "0: To exit"
                 ]

    controller = Controller()

    # As a voter I would like to see politician profiles,
    # so that i can easily educate myself on individual politicians
    # get all polls
    print("PRINTING ALL CANDIDATES -----\n\n")
    candidates = controller.get_all_candidates()
    for candidate in candidates:
        print(candidate)
    print("\n\n----------------------------")

    # As a political enthusiast, I want to see polling election data for an entire country.
    # So that I can get a better idea of how the elections are going.
    print("PRINTING ALL POLLS -----------\n\n")
    polls = controller.get_all_polls()
    for poll in polls:
        print(poll)
    print("\n\n----------------------------")

    # As a candidate I want to see polling data for an individual region
    # so that I can see what a certain region is leaning towards.
    print("PRINTING POLLS IN UTAH ----------\n\n")
    region = "Utah"
    polls = controller.get_current_polls_by_region(region)
    for poll in polls:
        print(poll)
    print("\n\n----------------------------")

    # As a campaign manager, I would like to see the polling data history for an individual region
    # so that I can see how a certain region has voted in the past.
    print("PRINTING POLLS BY REGION(Illinois) AND DATE(2019)")
    region = "Illinois"
    date = "2019-5-5 0:0:0"
    polls = controller.get_polls_by_region_and_date(region, date)
    for poll in polls:
        print(poll)
    print("\n\n----------------------------")


main()
