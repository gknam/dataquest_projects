import pandas as pd
from read import load_data, columns
from sys import argv

def printTop100urls():
    """
    Prints 100 most often appearing domains
    in a descending order
    """

    # ensure no argument is provided in command line
    if len(argv) > 1:
        print("Usage: python count.py")
        return

    # read in dataset
    df = load_data()

    # get domains
    urls = df["url"]

    # remove null values
    urls.dropna(inplace=True)
    
    # count domains and sort results by count then by domain
    url_val_c = urls.value_counts()
    url_val_c = url_val_c.reset_index()
    url_val_c.rename(columns={"index": "url", "url": "count"}, inplace=True)
    url_val_c.sort_values(by=["count", "url"], ascending=[False, True], inplace=True)

    # print 100 most often occuring domains
    for index, row in url_val_c[["url", "count"]].iloc[:100].iterrows():
        print(row["url"] + ": " + str(row["count"]))

if __name__ == "__main__":
    # print 100 most-often-appearing domains        
    printTop100urls()