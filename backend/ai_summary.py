import google.generativeai as genai
import os

# =====================================
# CONFIGURE GEMINI
# =====================================

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# =====================================
# GENERATE AI SUMMARY
# =====================================

def generate_ai_summary(
    email,
    breach_count,
    password_strength,
    url_status,
    notes,
    risk_level
):

    try:

        prompt = f"""

        You are an AI cybersecurity expert.

        Create a SHORT cybersecurity summary.

        Details:
        Email: {email}
        Breaches: {breach_count}
        Password Strength: {password_strength}
        URL Status: {url_status}
        Risk Level: {risk_level}
        Notes: {notes}

        Keep response:
        - short
        - professional
        - clean
        - under 100 words

        """

        response = model.generate_content(prompt)

        return {

            "summary":
            response.text.strip()

        }

    except Exception as error:

        return {

            "summary":
            f"AI Summary unavailable: {str(error)}"

        }