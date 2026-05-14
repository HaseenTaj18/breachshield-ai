import os
import google.generativeai as genai

from dotenv import load_dotenv

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# GEMINI API CONFIGURATION
# =========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(

    api_key=GEMINI_API_KEY
)

# =========================================
# LOAD GEMINI MODEL
# =========================================

model = genai.GenerativeModel(

    "gemini-1.5-flash"
)

# =========================================
# GENERATE AI SECURITY SUMMARY
# =========================================

def generate_ai_summary(

    email,
    breach_count,
    password_strength,
    url_status,
    notes,
    risk_level

):

    """
    Generate professional
    AI-powered cybersecurity report
    using Gemini AI
    """



    # =====================================
    # PROMPT
    # =====================================

    prompt = f"""

You are an advanced cybersecurity AI analyst.

Analyze the following cybersecurity scan results and generate a professional AI-powered security assessment report.

User Data:

Email:
{email}

Breach Count:
{breach_count}

Password Strength:
{password_strength}

Suspicious URL Status:
{url_status}

Overall Risk Level:
{risk_level}

Additional User Notes:
{notes}

Generate a detailed professional report with:

1. Executive Summary
2. Threat Analysis
3. Exposure Analysis
4. Password Security Insights
5. URL Threat Intelligence
6. Recommended Actions
7. Cybersecurity Best Practices
8. Final AI Security Conclusion

Keep the response professional,
modern and cybersecurity-focused.

"""



    try:

        # =================================
        # GENERATE AI RESPONSE
        # =================================

        response = model.generate_content(

            prompt
        )



        ai_text = response.text



        # =================================
        # RETURN AI RESULT
        # =================================

        return {

            "summary":
            ai_text

        }



    except Exception as error:

        # =================================
        # FALLBACK RESPONSE
        # =================================

        fallback_summary = f"""

AI Cybersecurity Report

Risk Level:
{risk_level}

Threat Analysis:
The provided credentials and URL indicators suggest potential cybersecurity exposure.

Exposure Analysis:
Detected breach count:
{breach_count}

Password Security:
Password strength classified as:
{password_strength}

URL Threat Intelligence:
URL status:
{url_status}

Recommended Actions:

• Enable Two-Factor Authentication
• Change exposed passwords immediately
• Avoid suspicious URLs
• Monitor account activity regularly
• Use password managers
• Update credentials frequently

Final AI Security Conclusion:
User should take proactive cybersecurity measures to reduce future exposure risks.

"""



        return {

            "summary":
            fallback_summary,

            "error":
            str(error)

        }