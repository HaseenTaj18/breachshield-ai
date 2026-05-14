from datetime import datetime

# =========================================
# REPORT GENERATOR
# =========================================

def generate_security_report(

    email,
    risk_level,
    breach_count

):

    report = {

        "email": email,

        "risk_level": risk_level,

        "breach_count": breach_count,

        "generated_at":

        datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"
        ),

        "recommendations": [

            "Change Passwords",

            "Enable 2FA",

            "Avoid Suspicious Links",

            "Monitor Login Activity"
        ]
    }



    return report