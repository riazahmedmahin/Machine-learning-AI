# get metadata of DataFrame
import pandas as pd

# read csv file
cars = pd.read_csv("Automobile.csv")

# display DataFrame

print(cars.info())