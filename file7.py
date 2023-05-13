import pandas as pd

# read csv file and give column names
cars = pd.read_csv("Automobile.csv", names = ['company_name', 'type', 'len','etype','milage', 'sunroof'])
# DataFrame with new columns
print(cars.columns)