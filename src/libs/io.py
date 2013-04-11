import os
import json


def save_data(data, path):
    fh = open(path, "w")
    json_data = json.dumps(data)
    fh.write(json_data)
    fh.close()
    #print data


def read_data(path):
    if os.path.exists(path):
        try:
            fh = open(path)
            content = fh.read()
            fh.close()
            #print content
            return json.loads(content)
        except:
            return []
    else:
        return []

