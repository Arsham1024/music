import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# ------------------------------------- KNN:
def knn(data):
    pass
    # Mean normalized value for number of Ratings
    # temp = data['# Ratings'][:]
    # for i in range(len(temp)):
    #     temp = int(temp[i])

    # print(type(temp))



# ------------------------------------- Helper Functions:
def load():
    with open("./output/new_releases.csv", "r") as f:
        data = pd.read_csv(f , index_col=False, header=0)
    return data
def pretty_print(data):
    # Special print functions
    with pd.option_context('display.max_columns', None):
        print(data.head(10))

def save():
    pass

def pretty_plot(data):
    data.plot(kind = 'scatter', x="Avg" , y="# Ratings")
    plt.show()

# ------------------------------------- Helper Settings:
# Pandas
pd.set_option('display.max_columns',None, 'display.width', None)

# ------------------------------------- Main:
if __name__ == '__main__':
    # Load data set
    data = load()
    # Check the data
    pretty_print(data)
    pretty_plot(data)

    knn(data)







