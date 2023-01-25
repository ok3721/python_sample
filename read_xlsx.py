import pandas

file = '/home/gg/Downloads/111.xlsx'
xl = pandas.ExcelFile(file)
df1 = xl.parse('Sheet1')

for index, row in df1.iterrows():
    print("Name" + " " + row["name"])
    print("date" + " " + row["date"])
    print("time" + " " + row["time"])
