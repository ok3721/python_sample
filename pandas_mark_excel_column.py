import pandas as pd

file = 'Untitled.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet1')

print(df1)
i = 0
for index, row in df1.iterrows():
    if i < 9:
        if row["status"] != "foo":
            print(row["video_name"])
            print(row["time"])
            df1.loc[index, 'status'] = 'uploaded'
            i += 1
            print(i)
        else:
            continue
    else:
        break
