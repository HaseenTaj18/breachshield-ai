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

    risk_score = 0

    risk_level = "Low"

    threat_status = "Secure"



    # =====================================
    # BREACH ANALYSIS
    # =====================================

    if breach_count >= 5:

        risk_score += 50

    elif breach_count >= 3:

        risk_score += 35

    elif breach_count >= 1:

        risk_score += 20



    # =====================================
    # PASSWORD ANALYSIS
    # =====================================

    password_strength = password_strength.lower()



    if password_strength == "weak":

        risk_score += 35

    elif password_strength == "medium":

        risk_score += 20

    elif password_strength == "strong":

        risk_score += 5



    # =====================================
    # URL ANALYSIS
    # =====================================

    if url_status == "danger":

        risk_score += 40

    elif url_status == "warning":

        risk_score += 20

    elif url_status == "safe":

        risk_score += 5



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
    # AI-STYLE RECOMMENDATIONS
    # =====================================

    recommendations = []



    if breach_count > 0:

        recommendations.append(

            "Change passwords immediately for breached accounts."

        )



    if password_strength.lower() == "weak":

        recommendations.append(

            "Use a stronger password with symbols, numbers and uppercase letters."

        )



    if url_status == "danger":

        recommendations.append(

            "Avoid visiting suspicious or phishing websites."

        )



    if len(recommendations) == 0:

        recommendations.append(

            "No major cybersecurity risks detected."
        )



    # =====================================
    # FINAL RESULT
    # =====================================

    return {

        "risk_score":
        risk_score,

        "risk_level":
        risk_level,

        "threat_status":
        threat_status,

        "recommendations":
        recommendations

    }