import pandas as pd

# change data type
cars = pd.read_csv("Automobile.csv", dtype={'mileage': 'float64'})

print(cars['mileage'].dtypes)