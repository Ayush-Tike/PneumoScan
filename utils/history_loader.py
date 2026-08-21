import pandas as pd
import json

def load_history(file):

    history = {}

    if file.name.endswith(".csv"):

        df = pd.read_csv(file)

        row = df.iloc[0].to_dict()

        # normalize column names
        history = {k.lower().strip(): str(v).strip() for k,v in row.items()}

    elif file.name.endswith(".json"):

        history = json.load(file)

        history = {k.lower().strip(): str(v).strip() for k,v in history.items()}

    return history