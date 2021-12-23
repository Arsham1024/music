import numpy as np
import pandas as pd

def showdata():

    with open("./output/new_releases.csv", "r") as f:
        imported_data = pd.read_csv(f , index_col=False)

    print(imported_data)
    data = pd.DataFrame(imported_data, columns=indexing)


    with pd.option_context('display.max_columns', None):  # more options can be specified also
        print(data)

if __name__ == '__main__':

    indexing = ["Artist", "Song" , "Date Released", "Avg", "Number of People Who Rated", "Wants"]
    showdata()