import numpy as np
import pandas as pd

df = pd.DataFrame(...) # your table with date column
parts = np.array_split(df, 10) # split into 10 parts
for i in range(10):
    part = parts[i]
    name = part['date'].iloc[0] # get the first date value of each part
    part.to_excel(f'{name}.xlsx') # save each part as an xlsx file with name as date
