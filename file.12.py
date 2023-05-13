import pandas as pd

student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

# Create DataFrame from dict
student_df = pd.DataFrame(student_dict)
# before rename
print(student_df)

# after rename column
student_df = student_df.rename(columns={'marks': "percentage"})
print(student_df)