import matplotlib.pyplot as plt
import pandas as pd
import re
from sys import argv

def do(topicString):
    # read in label info for dataset
    contents = pd.read_csv("data/CRDC2013_14content.csv")

    # read in dataset
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

    # get each school's total number of enrolled students
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]

    # get sums of all of the columns that break down enrollment by race and gender.
    cols = [col for col in data.columns \
    if col.startswith(topicString) and \
    "_LEP_" not in col and \
    "_504_" not in col and \
    "_IDEA_" not in col]

    cols_sums = data[cols].sum()
    
    # get sums of all of the columns that break down enrollment by race.
    cols_ng = []
    oldCol_ng = None
    
    for col in sorted(cols):
        
        # remove gender label
        col_ng = col[:-2]
        
        # add columns for both genders together
        if oldCol_ng == col_ng:
            data[col_ng] = data[col_ng].add(data[col])
            cols_ng.append(col_ng)
        else:
            data[col_ng] = data[col]
            oldCol_ng = col_ng

    cols_ng_sums = data[cols_ng].sum()

    # rename columns
    cols_map = {}
    cols_ng_map = {}
    
    topic = None
    for index, row in contents[["NAME", "LABEL"]].iterrows():

        name = row["NAME"]

        if name in cols:
            row_split = row["LABEL"].split(": ")
            new_label = "".join(row_split[1:])
            
            # dict for gender+race data
            cols_map[name] = new_label
        
            # dict for race data
            cols_ng_map[name[:-2]] = re.sub("\ Male$|\ Female$", "", new_label)

            # get topic
            if topic == None:
                topic = row_split[0]

    cols_sums.rename(index=cols_map, inplace=True)
    cols_ng_sums.rename(index=cols_ng_map, inplace=True)

    # get all schools' total number of enrolled students
    all_enrollment = data["total_enrollment"].sum()
    
    # get ratio of each enrolled gender-race group among the total enrolled students
    cols_perc = cols_sums / all_enrollment * 100
    ax = cols_perc.sort_values().plot.bar()
    ax.set_title(topic)
    plt.show()
    
    print("Percentages of groups categorised by gender and race")
    print(round(cols_sums / all_enrollment * 100, 2))
    print()
    
    # get ratio of each enrolled race group among the total enrolled students    
    cols_ng_perc = cols_ng_sums / all_enrollment * 100
    ax = cols_ng_perc.sort_values().plot.bar()
    ax.set_title(topic)
    plt.show()
    
    print("Percentages of groups categorised by race")
    print(round(cols_ng_sums / all_enrollment * 100, 2))

if __name__ == "__main__":
    do(topicString=argv[1])
