# =========================================
# AI RISK ANALYSIS ENGINE
# =========================================

def analyze_risk(

    breach_count,
    password_strength,
    url_status

):

    """
    Analyze cybersecurity risk level
    based on:
    - breach count
    - password strength
    - suspicious URL status
    """

    # =====================================
    # DEFAULT VALUES
    # =====================================

    security_score = 100

    risk_score = 0

    risk_level = "Low"

    threat_status = "Secure"

    dark_web_risk = "No major exposure detected"

    phishing_risk = "Safe"

    recommendations = []

    # =====================================
    # BREACH ANALYSIS
    # =====================================

    if breach_count >= 5:

        risk_score += 50

        security_score -= 50

        dark_web_risk = (
            "High dark web exposure detected."
        )

    elif breach_count >= 3:

        risk_score += 35

        security_score -= 35

        dark_web_risk = (
            "Moderate exposure detected."
        )

    elif breach_count >= 1:

        risk_score += 20

        security_score -= 20

        dark_web_risk = (
            "Minor exposure detected."
        )

    # =====================================
    # PASSWORD ANALYSIS
    # =====================================

    password_strength = (
        password_strength.lower()
    )

    if password_strength == "weak":

        risk_score += 35

        security_score -= 30

        recommendations.append(

            "Use a stronger password with symbols, uppercase letters and numbers."

        )

    elif password_strength == "medium":

        risk_score += 20

        security_score -= 15

        recommendations.append(

            "Improve password complexity for better protection."

        )

    elif password_strength == "strong":

        risk_score += 5

        security_score -= 5

    # =====================================
    # URL ANALYSIS
    # =====================================

    url_status = url_status.lower()

    if url_status == "danger":

        risk_score += 40

        security_score -= 35

        phishing_risk = (
            "Dangerous phishing URL detected."
        )

        recommendations.append(

            "Avoid visiting suspicious or phishing websites."

        )

    elif url_status == "warning":

        risk_score += 20

        security_score -= 15

        phishing_risk = (
            "Potentially suspicious URL detected."
        )

    elif url_status == "safe":

        risk_score += 5

        security_score -= 5

        phishing_risk = "No phishing threat detected."

    # =====================================
    # FINAL RISK LEVEL
    # =====================================

    if risk_score >= 80:

        risk_level = "High"

        threat_status = "Danger"

    elif risk_score >= 45:

        risk_level = "Medium"

        threat_status = "Warning"

    else:

        risk_level = "Low"

        threat_status = "Secure"

    # =====================================
    # MINIMUM SECURITY SCORE
    # =====================================

    if security_score < 0:

        security_score = 0

    # =====================================
    # DEFAULT RECOMMENDATION
    # =====================================

    if len(recommendations) == 0:

        recommendations.append(

            "No major cybersecurity risks detected."

        )

    # =====================================
    # FINAL RESULT
    # =====================================

    return {

        # MAIN SCORES

        "risk_score":
        risk_score,

        "security_score":
        security_score,

        # THREAT LEVELS

        "risk_level":
        risk_level,

        "threat_status":
        threat_status,

        # EXTRA FEATURES

        "dark_web_risk":
        dark_web_risk,

        "phishing_risk":
        phishing_risk,

        # SECURITY RECOMMENDATIONS

        "recommendations":
        recommendations

    }