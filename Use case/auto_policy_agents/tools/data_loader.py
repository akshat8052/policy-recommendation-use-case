import pandas as pd

def get_user_profile():
    df = pd.read_csv("data/users.csv")
    return df.iloc[0].to_dict()

def load_policy_data():
    df = pd.read_csv("data/policies.csv")
    return df.to_dict(orient="records")
