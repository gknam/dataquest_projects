import pandas as pd

def load_data():
    """
    Read in data and add column labels
    """
    
    import pandas as pd
    from IPython.display import display

    # read in dataset
    df = pd.read_csv("hn_stories.csv", header=None)

    # add columns
    df.columns = columns
    
    return df

columns = ["submission_time", "upvotes", "url", "headline"]

if __name__ == "__main__":
    load_data()