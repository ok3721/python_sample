import datetime
import pandas as pd

# file = 'list2.xlsx'
# xl = pd.ExcelFile(file)
# df1 = xl.parse('Sheet1')


dd = []
tt = []
for i in range(3):
    start_date = datetime.datetime(2021, 3, 12)
    current_date = start_date + datetime.timedelta(days=i)
    hourtimes = ["12:00", "15:00", "20:00"]

    for hourtime in hourtimes:
        date = current_date.strftime("%Y/%m/%d")
        print(date)
        print(hourtime)
        dd.append(date)
        tt.append(hourtime)

columns = ['Date', 'Time']
df = pd.DataFrame(list(zip(dd, tt)), columns=columns)

print(df)

df.to_excel('list3.xlsx')
