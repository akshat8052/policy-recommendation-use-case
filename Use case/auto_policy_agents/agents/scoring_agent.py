def scoring_agent(state):
    from tools.rules import score_policies
    scored = score_policies(state.user_profile, state.eligible_policies)
    return {"scored_policies": scored}
