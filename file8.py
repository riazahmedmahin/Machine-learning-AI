# import pandas library
import pandas as pd

cars = pd.read_csv("Automobile.csv", usecols=['sunroof'])
print("Before : \n", cars)

# read csv file with boolean values
cars = pd.read_csv("Automobile.csv", usecols=['sunroof'], true_values=["Yes"], false_values=["No"])
print("After : \n", cars)