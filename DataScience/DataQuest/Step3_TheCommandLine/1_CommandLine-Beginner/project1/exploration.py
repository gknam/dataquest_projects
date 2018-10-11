import pandas as pd

if __name__ == "__main__":

    # read in dataset
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

    # display value counts in JJ column
    print(data["JJ"].value_counts())

    # display value counts in SCH_STATUS_MAGNET column
    print(data["SCH_STATUS_MAGNET"].value_counts())
