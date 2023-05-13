import pandas as pd

# read csv file
cars = pd.read_csv("Automobile.csv")

# get a element using row and column labels
print(cars.at[1,'company'])