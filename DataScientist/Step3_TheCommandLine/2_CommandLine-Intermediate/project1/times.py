from dateutil.parser import parse
from read import load_data
from sys import argv

def extractUnit(timestamp, unit):
    """
    return unit from timestamp in UTC format.
    A unit can be year, month, day or hour.
    
    procs is a dictionary where key is a unit
    and values is a command string for the unit.
    """

    return eval("parse(timestamp)." + unit)


def printSubmissionTimes(unit=None):
    
    err_mes = "Usage: python times.py [unit]\n\
        \n\
        A unit can be year, month, day or hour.\n\
        \n\
        e.g. python times.py hour"

    # stop if no unit is given by user
    if len(argv) == 1:
        print(err_mes)
        return

    procs = {"year", "month", "day", "hour"}
    
    unit = argv[1] if argv[1] != "-f" else unit

    if unit not in procs:
        print(err_mes)
        return        
    
    # read in dataset
    df = load_data()

    # get hour from each row of submission_time column
    h = df["submission_time"].apply(extractUnit, args=(unit, ))

    # get value counts and sort it in descending order
    h = h.value_counts().sort_values(ascending=False)

    # print series
    print("{}: Occurences".format(unit))
    for index, value in h.iteritems():
        print(str(index) + ": " + str(value))

# note: In case another script imports a function,
# printSubmissionTimes() from running automatically
# if this line ('f __name__ == "__main__":) is missing.
if __name__ == "__main__":
    printSubmissionTimes()