import pandas as pd

# read csv file
cars = pd.read_csv("Automobile.csv")

print(cars.info())