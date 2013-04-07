import os
import json

JSON_PATH = os.path.join(os.path.dirname(__file__), "data.json")


def save_data(data):
    fh = open(JSON_PATH, "w")
    json_data = json.dumps(data)
    fh.write(json_data)
    fh.close()
    #print data


def read_data():
    if os.path.exists(JSON_PATH):
        try:
            fh = open(JSON_PATH)
            content = fh.read()
            fh.close()
            #print content
            return json.loads(content)
        except:
            return []
    else:
        return []

