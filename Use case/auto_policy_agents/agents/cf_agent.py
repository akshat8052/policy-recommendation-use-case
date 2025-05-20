def collaborative_filtering_agent(state):
    from tools.collab_filtering import load_user_policy_data, train_svd_model, get_top_n_recommendations
    user_id = state.user_profile['Full Name']
    interactions_df = load_user_policy_data('data/updated_auto_policy_user_data_samples.csv')
    algo, trainset = train_svd_model(interactions_df)

    # Filter based on eligible policies only
    eligible_policy_names = [p['Policy Name'] for p in state.eligible_policies]
    top_cf = get_top_n_recommendations(algo, trainset, user_id, eligible_policy_names, n=5)

    # Return policy objects that match
    matched_policies = [p for p in state.eligible_policies if p['Policy Name'] in top_cf]
    return {"cf_policies": matched_policies}
