import math
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None, 'display.width', None)

def string_toint(col_name):
    col = df[col_name]
    # This one line of code will grab every single string in ratings and remove ","
    # Then it will turn it into an int for processing later
    # Replaces "-" with -infinity
    for i in range(len(col)):
        col[i] = int(col[i].replace(",", '')) if col[i] != "-" else math.inf

    # Replace the col with the original
    df.replace(col_name , col)

if __name__ == '__main__':

    # Read in the data into pandas
    path = "./output/new_releases.csv"
    df = pd.read_csv(path)

    # col to change to strings
    col_name = "# Ratings"
    string_toint(col_name)

    df.to_csv("./output/new_releases.csv", index=False)

