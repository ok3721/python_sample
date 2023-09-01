from datetime import datetime
import json



with open('/home/aoss/Documents/mengzhu.json', "r") as cookief: 
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        da = cookie.get("expiry","None")
        if da != "None":
            nda = datetime.fromtimestamp(da)
            print(nda)
