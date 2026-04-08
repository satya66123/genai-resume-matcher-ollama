import json

def save_result(data):
    try:
        with open("data/history.json", "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(data)

    with open("data/history.json", "w") as f:
        json.dump(history, f, indent=2)