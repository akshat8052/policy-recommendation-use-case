def eligibility_agent(state):
    from tools.rules import filter_eligible_policies
    from tools.data_loader import load_policy_data
    policies = load_policy_data()
    eligible = filter_eligible_policies(state.user_profile, policies)

    return {"eligible_policies": eligible}
