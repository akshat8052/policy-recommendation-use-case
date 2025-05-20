# def scoring_agent(state):
#     from tools.rules import score_policies
#     scored = score_policies(state.user_profile, state.eligible_policies)
#     return {"scored_policies": scored}


def scoring_agent(state):
    from tools.rules import score_policies
    policies_to_score = state.cf_policies if state.cf_policies else state.eligible_policies
    scored = score_policies(state.user_profile, policies_to_score)

    # Tag CF origin
    for policy in scored:
        if policy["Policy Name"] in [p["Policy Name"] for p in state.cf_policies]:
            policy["source"] = "Collaborative Filtering"
        else:
            policy["source"] = "Eligibility Rules"
    return {"scored_policies": scored}