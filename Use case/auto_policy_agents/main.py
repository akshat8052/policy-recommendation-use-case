import streamlit as st
from langgraph.graph import StateGraph
from agents.intake_agent import intake_agent
from agents.eligibility_agent import eligibility_agent
from agents.scoring_agent import scoring_agent
from agents.explainer_agent import explainer_agent
from agents.feedback_agent import feedback_agent
from agents.cf_agent import collaborative_filtering_agent
from agents.reflection_agent import reflection_agent
from datetime import date

# Set up Streamlit page
st.set_page_config(page_title="Auto Policy Recommender", layout="centered")
st.title("🚗 Auto Policy Recommendation System")

# Input fields for user profile
with st.form("user_input_form"):
    st.subheader("User Profile")
    full_name = st.text_input("Full Name", "John Doe")
    dob = st.date_input("Date of Birth",min_value=date(1950, 1, 1))
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    license_state = st.selectbox("License State", ["CA", "TX", "NY", "FL", "IL", "PA", "OH", "GA", "NC", "MI"])
    years_driving = st.slider("Years of Driving Experience", 1, 50, 5)
    accidents = st.slider("Accidents in Last 5 Years", 0, 5, 0)
    violations = st.slider("Violations in Last 5 Years", 0, 5, 0)
    claims = st.slider("Claims in Last 5 Years", 0, 5, 0)

    st.subheader("Vehicle Details")
    vehicle_year = st.number_input("Vehicle Year", min_value=2000, max_value=2025, value=2018)
    vehicle_usage = st.selectbox("Vehicle Usage", ["Personal", "Business", "Rideshare"])
    ownership_status = st.selectbox("Ownership Status", ["Owned", "Financed", "Leased"])
    parking = st.selectbox("Primary Parking Location", ["Garage", "Street", "Driveway"])
    zip_code = st.text_input("ZIP Code", "10001")

    st.subheader("Insurance Preferences")
    has_continuous_insurance = st.checkbox("Has Continuous Insurance", value=True)
    coverage_type = st.selectbox("Coverage Type", ["Liability Only", "Full Coverage"])
    deductible = st.selectbox("Deductible Preference", [250, 500, 1000])
    optional_coverages = st.multiselect("Optional Coverages", ["Roadside Assistance", "Rental Reimbursement", "Gap Insurance"])
    # telematics = st.checkbox("Willing to Use Telematics", value=True)

    # st.subheader("Feedback (for testing Reflection Agent)")
    # feedback = st.text_area("User Feedback", "Satisfied with top policy.")

    submit = st.form_submit_button("Recommend Policy")

if submit:
    # Convert to user_profile dict
    user_profile = {
        "Full Name": full_name,
        "Date of Birth": str(dob),
        "Gender": gender,
        "Marital Status": marital_status,
        "Driver’s License Number": "XXX1234567",
        "License State": license_state,
        "Years of Driving Experience": years_driving,
        "Accidents in Last 5 Years": accidents,
        "Violations in Last 5 Years": violations,
        "Claims in Last 5 Years": claims,
        "Vehicle Year": vehicle_year,
        "Vehicle Usage": vehicle_usage,
        "Ownership Status": ownership_status,
        "Primary Parking Location": parking,
        "ZIP Code": zip_code,
        "Has Continuous Insurance": has_continuous_insurance,
        "Coverage Type": coverage_type,
        "Deductible Preference": deductible,
        "Wants Optional Coverage": ", ".join(optional_coverages),
        # "Willing to Use Telematics": telematics,
        "Insurance Provider": "NA"
    }


    from tools.state_schema import State
    # schema = {
    #     "user_profile": dict,
    #     "eligible_policies": list,
    #     "scored_policies": list,
    #     "explanation": str,
    #     "feedback": str,
    #     "reflection": str
    # }

    builder = StateGraph(State)
    builder.add_node("Intake", lambda _: {"user_profile": user_profile})
    builder.add_node("Eligibility", eligibility_agent)
    builder.add_node("Scoring", scoring_agent)
    builder.add_node("Explainer", explainer_agent)
    # builder.add_node("Feedback", lambda state: {"feedback": feedback})
    builder.add_node("Reflection", reflection_agent)

    builder.set_entry_point("Intake")
    builder.add_edge("Intake", "Eligibility")
    builder.add_node("CollaborativeFiltering", collaborative_filtering_agent)
    builder.add_edge("Eligibility", "CollaborativeFiltering")
    builder.add_edge("CollaborativeFiltering", "Scoring")

    # builder.add_edge("Eligibility", "Scoring")
    # builder.add_edge("Scoring", "Explainer")
    # builder.add_edge("Explainer", "Feedback")
    # builder.add_edge("Feedback", "Reflection")
    builder.add_edge("Explainer", "Reflection")
    builder.set_finish_point("Reflection")
    graph = builder.compile()
    result = graph.invoke(State())
    
    st.success("✅ Policy Recommended Successfully!")
    # st.markdown(f"### 📝 Explanation:\n{result['explanation']}")
    st.subheader("📋 Top Recommended Policies")

    for card in result["explanation"]:
        with st.container():
            st.markdown(card)
            st.markdown("---")

    st.markdown(f"### 💭 Reflection:\n{result['reflection']}")
