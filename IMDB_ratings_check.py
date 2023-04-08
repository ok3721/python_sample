#Special thanks to https://github.com/itsmehemant7/PyMovieDb/
from PyMovieDb import IMDB
import json
import pandas as pd

file = 'C:/Users/X1 Carbon/Documents/name.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet1')

for index, row in df1.iterrows():
    imdb = IMDB()
    res = imdb.get_by_name(row["Name"])
    result = json.loads(res)
    status = list(result)[0]
    if status == "status":
        print(row["Name"] + "no exists")
        pass
    else:
        type = result["type"]
        rating = result["rating"]['ratingValue']
        name = result["name"]
        if len(result["director"]) == 0:
            director = ""
        else:
            director = result["director"][0]["name"]
        print("Name: " + str(name) + "/Type: "+ str(type)+ "/Director: "+ str(director) + "/Rating: " +str(rating))
