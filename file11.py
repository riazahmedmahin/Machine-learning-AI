import pandas as pd

# cars = pd.read_csv("EncodedData.csv") #-> throws UnicodeDecodeError

cars = pd.read_csv("EncodedData.csv", encoding="latin-1")
print(cars)