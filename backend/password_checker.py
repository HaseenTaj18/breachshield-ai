import re

# =========================================
# PASSWORD STRENGTH CHECKER
# =========================================

def check_password_strength(password):

    """
    Analyze password strength
    using cybersecurity-based rules
    """



    # =====================================
    # INITIAL SCORE
    # =====================================

    score = 0

    feedback = []



    # =====================================
    # LENGTH CHECK
    # =====================================

    if len(password) >= 12:

        score += 30

    elif len(password) >= 8:

        score += 20

    else:

        feedback.append(

            "Password length is too short."
        )



    # =====================================
    # UPPERCASE CHECK
    # =====================================

    if re.search(r"[A-Z]", password):

        score += 15

    else:

        feedback.append(

            "Add uppercase letters."
        )



    # =====================================
    # LOWERCASE CHECK
    # =====================================

    if re.search(r"[a-z]", password):

        score += 15

    else:

        feedback.append(

            "Add lowercase letters."
        )



    # =====================================
    # NUMBER CHECK
    # =====================================

    if re.search(r"[0-9]", password):

        score += 15

    else:

        feedback.append(

            "Add numeric values."
        )



    # =====================================
    # SPECIAL CHARACTER CHECK
    # =====================================

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):

        score += 20

    else:

        feedback.append(

            "Add special characters."
        )



    # =====================================
    # COMMON PASSWORD CHECK
    # =====================================

    common_passwords = [

        "123456",

        "password",

        "admin",

        "qwerty",

        "12345678",

        "password123",

        "welcome",

        "abc123"

    ]



    if password.lower() in common_passwords:

        score = 10

        feedback.append(

            "This password is commonly used and unsafe."
        )



    # =====================================
    # FINAL STRENGTH LEVEL
    # =====================================

    if score >= 80:

        strength = "Strong"

        risk = "Low"



    elif score >= 50:

        strength = "Medium"

        risk = "Medium"



    else:

        strength = "Weak"

        risk = "High"



    # =====================================
    # AI STYLE SECURITY MESSAGE
    # =====================================

    ai_security_message = f"""

AI Password Security Analysis:

The password strength is classified as {strength}.

Cybersecurity risk level associated with this password is {risk}.

Security recommendations:

"""



    if feedback:

        for item in feedback:

            ai_security_message += f"\n• {item}"

    else:

        ai_security_message += (

            "\n• No major weaknesses detected."
        )



    # =====================================
    # RETURN RESULT
    # =====================================

    return {

        "password_strength":
        strength,

        "risk":
        risk,

        "score":
        score,

        "feedback":
        feedback,

        "ai_security_message":
        ai_security_message

    }