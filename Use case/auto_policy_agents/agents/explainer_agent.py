# def explainer_agent(state):
#     print('No of policies',len(state.scored_policies))
#     top_policy = state.scored_policies[0]  # Pydantic-style access
#     user = state.user_profile

#     # Generate explanation
#     explanation = f"""
# Top recommended policy: **{top_policy['Policy Name']}** by **{top_policy['Insurance Provider']}**

# 🧠 **Why this was recommended for you:**
# - You requested **{user['Coverage Type']}**, and this policy matches it.
# - Your state (**{user['License State']}**) is covered by this policy.
# - Your vehicle is **{2025 - user['Vehicle Year']} years old**, within the policy's limit of {top_policy['Vehicle Age Limit (Years)']} years.
# - The policy accepts drivers with up to {top_policy['Max Past Claims Allowed']} past claims — you have {user['Claims in Last 5 Years']}.
# - Your clean violation record meets the policy’s 3-year clean history requirement.

# 💰 **Policy Features:**
# - Collision Deductible: ${top_policy['Collision Deductible']}
# - Liability Limits: {top_policy['Liability Limits']}
# - Optional Coverage: {top_policy['Optional Coverages Included'] or 'None'}
# - Premium: ${top_policy['Base Premium (Annual)']} / year
# - Customer Rating: ⭐ {top_policy['Customer Rating (out of 5)']} / 5
# - Support: {'24/7' if top_policy['24/7 Support'] else 'Business hours only'}

# 🏁 **LangGraph Match Score**: **{top_policy['score']}**
#     """.strip()

#     return {"explanation": explanation}


# def explainer_agent(state):
#     policies = state.scored_policies
#     user = state.user_profile
#     explanations = []

#     print(f"No of policies: {len(policies)}")

#     for idx, policy in enumerate(policies[:5]):  # Show top 5
#         explanation = f"""
# ### 🛡️ Policy #{idx + 1}: **{policy['Policy Name']}** by **{policy['Insurance Provider']}**

# 🧠 **Why this fits you:**
# - Requested: **{user['Coverage Type']}**, and this policy provides it.
# - Your state (**{user['License State']}**) is covered.
# - Vehicle is **{2025 - user['Vehicle Year']}** years old (allowed: {policy['Vehicle Age Limit (Years)']}).
# - Accepts up to {policy['Max Past Claims Allowed']} claims — you have {user['Claims in Last 5 Years']}.
# - Violation-free period fits the requirement: {policy['Violation-Free Period (Years)']} years.

# 💰 **Policy Features:**
# - Deductible: ${policy['Collision Deductible']}
# - Limits: {policy['Liability Limits']}
# - Add-ons: {policy['Optional Coverages Included'] or 'None'}
# - Premium: ${policy['Base Premium (Annual)']} / year
# - Rating: ⭐ {policy['Customer Rating (out of 5)']} / 5
# - Support: {'24/7' if policy['24/7 Support'] else 'Business hours only'}

# 🏁 **Match Score**: **{policy['score']}**
#         """.strip()
#         explanations.append(explanation)

#     return {"explanation": explanations}



# from assistants.llm_assistant import call_llm
# from tools.prompts import top_policy_prompt, short_policy_prompt

# def explainer_agent(state):
#     policies = state.scored_policies[:5]  # Top 5
#     user = state.user_profile
#     explanations = []

#     # 🎯 Long explanation for top policy
#     top = policies[0]
#     top_prompt = top_policy_prompt.format(
#         name=user['Full Name'],
#         state=user['License State'],
#         coverage=user['Coverage Type'],
#         vehicle_age=2025 - user['Vehicle Year'],
#         driving_exp=user['Years of Driving Experience'],
#         claims=user['Claims in Last 5 Years'],
#         violations=user['Violations in Last 5 Years'],
#         policy_name=top['Policy Name'],
#         provider=top['Insurance Provider'],
#         premium=top['Base Premium (Annual)'],
#         deductible=top['Collision Deductible'],
#         rating=top['Customer Rating (out of 5)'],
#         limits=top['Liability Limits'],
#         addons=top['Optional Coverages Included'] or "None",
#         availability=top['State Availability'],
#         score=top['score']
#     )
#     explanations.append(call_llm(top_prompt))

#     # 📌 Short bullets for other policies
#     for idx, p in enumerate(policies[1:], start=2):
#         short_prompt = short_policy_prompt.format(
#             index=idx,
#             policy_name=p['Policy Name'],
#             provider=p['Insurance Provider'],
#             premium=p['Base Premium (Annual)'],
#             coverage=p['Coverage Type'],
#             rating=p['Customer Rating (out of 5)'],
#             addons=p['Optional Coverages Included'] or "None"
#         )
#         summary = call_llm(short_prompt)
#         explanations.append(f"**Policy #{idx}:** {summary}")

#     return {"explanation": explanations}


def explainer_agent(state):
    top_policy = state.scored_policies[0]
    user = state.user_profile

    explanation = f"""
Top recommended policy: **{top_policy['Policy Name']}** by **{top_policy['Insurance Provider']}**  
🔍 **Source**: _{top_policy.get('source', 'N/A')}_

🧠 **Why this was recommended for you:**
- You requested **{user['Coverage Type']}**, and this policy matches it.
- Your state (**{user['License State']}**) is covered by this policy.
- Your vehicle is **{2025 - user['Vehicle Year']} years old**, within the policy's limit of {top_policy['Vehicle Age Limit (Years)']} years.
- The policy accepts drivers with up to {top_policy['Max Past Claims Allowed']} past claims — you have {user['Claims in Last 5 Years']}.
- Your clean violation record meets the policy’s 3-year clean history requirement.

💰 **Policy Features:**
- Collision Deductible: ${top_policy['Collision Deductible']}
- Liability Limits: {top_policy['Liability Limits']}
- Optional Coverage: {top_policy['Optional Coverages Included'] or 'None'}
- Premium: ${top_policy['Base Premium (Annual)']} / year
- Customer Rating: ⭐ {top_policy['Customer Rating (out of 5)']} / 5
- Support: {'24/7' if top_policy['24/7 Support'] else 'Business hours only'}

🏁 **LangGraph Match Score**: **{top_policy['score']}**
    """.strip()

    return {"explanation": explanation}