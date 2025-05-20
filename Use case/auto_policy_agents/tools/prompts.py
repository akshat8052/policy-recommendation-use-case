reflection_prompt = """
You are a senior insurance strategist AI. Based on the user feedback below and the explanation of the top recommended policy, reflect and provide:
1. A brief assessment of the recommendation quality.
2. One suggestion for improving the recommendation in future.

Feedback: {feedback}
Explanation: {explanation}
"""
# explainer_prompt = """
# You are an insurance advisor AI.

# Here’s a user:
# - Name: {full_name}
# - State: {state}
# - Coverage Type: {coverage_type}
# - Vehicle Year: {vehicle_year}
# - Driving Experience: {driving_exp} years
# - Claims in Last 5 Years: {claims}
# - Violations: {violations}

# Here are the top 5 matching policies:

# {policies}

# 🧠 Write a clear, friendly explanation of the top recommendations.
# - Explain which policy is best and why.
# - Mention standout features.
# - Help the user choose confidently.
# """


per_policy_explainer_prompt = """
You are an AI insurance advisor.

A user named {name} from {state} is looking for {coverage} coverage.
- Driving experience: {driving_exp} years
- Claims: {claims}, Violations: {violations}
- Vehicle is {vehicle_age} years old

Explain why the following policy is a good fit:

Policy #{index}: {policy_name} by {provider}
- Premium: ${premium} annually
- Deductible: ${deductible}
- Liability Limits: {limits}
- Optional Coverages: {addons}
- State Coverage: {availability}
- Rating: {rating}/5
- Match Score: {score}

Write a helpful, friendly, and personalized explanation for this policy.
Highlight the benefits, justify the fit, and keep it concise.
"""


top_policy_prompt = """
You are an insurance recommendation assistant.

Write a friendly, clear explanation for why this policy is a great match:

- User: {name} from {state}, looking for {coverage} coverage
- Vehicle age: {vehicle_age} years
- Driving exp: {driving_exp} years
- Claims: {claims}, Violations: {violations}

Policy: {policy_name} by {provider}
- Premium: ${premium} / year
- Deductible: ${deductible}
- Liability: {limits}
- Add-ons: {addons}
- States: {availability}
- Rating: {rating}/5
- Score: {score}

Focus on personal fit, benefits, and reassurance. Only bullet points.
"""


short_policy_prompt = """
Summarize this policy in one sentence for a driver:

- Name: {policy_name}
- Provider: {provider}
- Premium: ${premium}
- Coverage: {coverage}
- Add-ons: {addons}
- Rating: {rating}/5

Be brief, confident, and mention one standout feature.
"""
