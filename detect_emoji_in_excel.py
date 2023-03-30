import pandas as pd
import emoji

file = 'D:/tico.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet2')

counter = 0
for index, row in df1.iterrows():
#     print(row["name"])
    ec = emoji.emoji_count(row["name"])
    if ec > 0:
        print(index, row["name"], "emoji!", ec)
        counter +=1
    else:
        continue
    
print(counter)
