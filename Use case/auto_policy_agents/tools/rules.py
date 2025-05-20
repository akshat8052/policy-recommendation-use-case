from datetime import datetime

CURRENT_YEAR = datetime.now().year

def filter_eligible_policies(user, policies):
    results = []
    age = CURRENT_YEAR - int(user["Date of Birth"].split("-")[0])
    vehicle_age = CURRENT_YEAR - int(user["Vehicle Year"])
    for policy in policies:
        if (
            age >= policy["Minimum Age Required"] and
            user["Years of Driving Experience"] >= policy["Minimum Driving Experience (Years)"] and
            vehicle_age <= policy["Vehicle Age Limit (Years)"] and
            user["Vehicle Usage"] == policy["Vehicle Use Type Covered"] and
            user["License State"] in policy["State Availability"] and
            (not policy["Continuous Insurance Required"] or user["Has Continuous Insurance"]) and
            user["Claims in Last 5 Years"] <= policy["Max Past Claims Allowed"] and
            (user["Violations in Last 5 Years"] == 0 or user["Years of Driving Experience"] >= policy["Violation-Free Period (Years)"])
        ):
            results.append(policy)
    return results

def score_policies(user, policies):
    results = []
    for policy in policies:
        score = 0
        if user["Coverage Type"] == policy["Coverage Type"]:
            score += 20
        if policy["Collision Deductible"] <= user["Deductible Preference"]:
            score += 15
        for cov in user["Wants Optional Coverage"].split(", "):
            if cov in policy["Optional Coverages Included"]:
                score += 10
        # if user["Willing to Use Telematics"] and policy["Telematics Discount Available"]:
            # score += 10
        if policy["Base Premium (Annual)"] < 1200:
            score += 10
        if policy["Customer Rating (out of 5)"] >= 4.5:
            score += 10
        if policy["Avg Claims Process Time (days)"] <= 3:
            score += 10
        if policy["Mobile App Available"]:
            score += 5
        if policy["24/7 Support"]:
            score += 5
        policy["score"] = score
        results.append(policy)
    return sorted(results, key=lambda x: x["score"], reverse=True)
