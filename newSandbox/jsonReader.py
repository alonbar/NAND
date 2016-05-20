import json
from pprint import pprint

if __name__ == "__main__":
    with open('c:/temp/3.json',encoding="utf8") as data_file:
        data = json.load(data_file)

    features = data['features']
    output_file = open("c:/temp/economy2.csv", "w")
    for feature in features:
        stat = feature["attributes"]["STAT08"]
        eschol = feature["attributes"]["eshcol"]
        output_file.write(str(stat) + "," + str(eschol) + "\n")

    output_file.close()


