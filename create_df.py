import json
from operator import index
import pandas as pd

with open("posuto/posuto/postaldata.json") as file:
    data = json.load(file)
    df = pd.DataFrame(data)


postal_codes = list(df.columns)

new_data = {
    "Postal Code": [],
    "Prefecture Name": [],
    "City": []
}

for postal_code in postal_codes:
    full_postal_code = "〒" + str(postal_code)
    full_postal_code = full_postal_code[0:4] + "-" + full_postal_code[4::]

    prefecture_name = data[postal_code]["prefecture"]
    city_name = data[postal_code]["city"]
    new_data["Postal Code"].append(full_postal_code)
    new_data["Prefecture Name"].append(prefecture_name)
    new_data["City"].append(city_name)
    
    
return_df = pd.DataFrame.from_dict(new_data)

return_df.to_csv("postal_code_n_prefecture.csv",index=True)
