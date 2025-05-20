import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from collections import defaultdict

def load_user_policy_data(path):
    df = pd.read_csv(path)
    interactions = []

    for index, row in df.iterrows():
        user = row['Full Name']
        taken_policies = row['Policies Taken']
        if pd.notna(taken_policies):
            for policy in taken_policies.split(','):
                interactions.append((user, policy.strip(), 1))  # implicit feedback

    return pd.DataFrame(interactions, columns=['user', 'item', 'rating'])

def train_svd_model(interactions_df):
    reader = Reader(rating_scale=(0, 1))
    data = Dataset.load_from_df(interactions_df[['user', 'item', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
    
    algo = SVD()
    algo.fit(trainset)
    
    return algo, trainset

def get_top_n_recommendations(algo, trainset, user_id, policy_list, n=5):
    taken_items = set([j for (j, _) in trainset.ur[trainset.to_inner_uid(user_id)]])
    all_items = set(trainset._raw2inner_id_items.keys())
    candidates = all_items - taken_items
    
    predictions = [(trainset.to_raw_iid(item), algo.predict(user_id, trainset.to_raw_iid(item)).est)
                   for item in candidates if trainset.to_raw_iid(item) in policy_list]
    
    top_n = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]
    return [iid for (iid, _) in top_n]
