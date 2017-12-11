from read import load_data
from times import extractUnit
from read import columns

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sys import argv

def meanUpvotesForVar(var=None):
    """
    var is a column name in dataframe.
    varLabel is a column name for new dataframe
        aggregated upon var.

    Prints up to 100 var entries with most votes,
    in descending order.
    """

    err_mes = "Usage: python upvotes.py [variable]\n\
        \n\
        A variable can be headline, submission_time or url.\n\
        \n\
        e.g. python times.py headline"

    # stop if no unit is given by user
    if len(argv) == 1:
        print(err_mes)
        return

    var = argv[1] if argv[1] != "-f" else var

    if var not in columns:
        print(err_mes)
        return
    
    # load data
    df = load_data()

    # process var data
    # 1. headline length
    if var == "headline":
        x = df[var].apply(lambda x: len(str(x)))
        var_new = "Headline length"
    # 2. submission time
    elif var == "submission_time":
        x = df[var].apply(extractUnit, args=("hour", ))
        var_new = "Submission time"
    elif var == "url":
        x = df[var]
        var_new = "Domain"

    # create dataframe of upvotes and var data
    up_label = "upvotes"
    up_x = pd.concat([x, df[up_label]], axis=1)

    # average number of upvotes across var data
    up_x_piv = up_x.pivot_table(index=var, values=up_label, aggfunc=np.mean)

    # rename column and index of new dataframe
    up_label_new = "Mean number of upvotes"
    up_x_piv = up_x_piv.rename(columns={up_label: up_label_new})
    #up_x_piv.set_index(var, inplace=True)
    up_x_piv.index.name = var_new
    

    # show mean number of upvotes per var data entry
    pd.set_option("display.max_row", len(up_x_piv))
    print(up_x_piv.sort_values(by=up_label_new, ascending=False).iloc[:100])

if __name__ == "__main__":
    meanUpvotesForVar()