import pandas as pd

# read csv file
cars = pd.read_csv("Automobile.csv", header=[0, 1])
print(cars)