def intake_agent(state):
    from tools.data_loader import get_user_profile
    user_profile = get_user_profile()
    return {"user_profile": user_profile}
