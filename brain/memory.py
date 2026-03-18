import json
MEM_FILE = "data/memory.json"

def load():
    try:
        return json.load(open(MEM_FILE))
    except:
        return []

def save(item):
    data = load()
    data.append(item)
    json.dump(data, open(MEM_FILE, "w"))