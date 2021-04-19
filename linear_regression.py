#! /usr/bin/env python3
# a script that plots scatterplot and makes a liner regression using the iris file as input
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def get_regression_line(x, y):
    """
    This is a function that makes a scatter 
    plot and linear regression 
    parameters 
    -----------
    x : dataframe that would be used on x-axix
    y : datframe to be used on y_axix

    Returns
    -------
    plot and linear regression line fit. 
    """
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = "")
    plt.plot(x, slope * x + intercept)
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    return


if __name__ == '__main__':

    
    dataframe = pd.read_csv("iris.csv")
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    virginica = dataframe[dataframe.species == "Iris_virginica"]
    setosa = dataframe[dataframe.species == "Iris_setosa"]

    x1 = versicolor.petal_length_cm
    y1 = versicolor.sepal_length_cm
    x2 = virginica.petal_length_cm
    y2 = virginica.sepal_length_cm
    x3 = setosa.petal_length_cm
    y3 = setosa.sepal_length_cm

    result1 = get_regression_line(x1, y1)
    result2 = get_regression_line(x2, y2)
    result3 = get_regression_line(x3, y3)
    plt.savefig("all_three_species.png")
    plt.close('all')
    quit()
