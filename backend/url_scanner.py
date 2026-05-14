import re
import validators
from urllib.parse import urlparse

# =========================================
# AI URL SCANNER
# =========================================

def scan_url(url):

    """
    Analyze suspicious URLs
    using cybersecurity heuristics
    """



    # =====================================
    # CLEAN URL
    # =====================================

    url = url.strip()



    # =====================================
    # INVALID URL
    # =====================================

    if not validators.url(url):

        return {

            "status":
            "danger",

            "message":
            "Invalid URL format detected.",

            "risk_level":
            "High",

            "threats": [

                "Malformed URL",

                "Potential phishing attempt"

            ]

        }



    # =====================================
    # PARSE URL
    # =====================================

    parsed_url = urlparse(url)

    domain = parsed_url.netloc.lower()



    # =====================================
    # SUSPICIOUS KEYWORDS
    # =====================================

    suspicious_keywords = [

        "login",

        "verify",

        "secure",

        "banking",

        "update",

        "free",

        "bonus",

        "crypto",

        "gift",

        "wallet",

        "paypal",

        "account"

    ]



    # =====================================
    # SHORTENED URL DOMAINS
    # =====================================

    shortened_domains = [

        "bit.ly",

        "tinyurl.com",

        "goo.gl",

        "t.co",

        "shorturl.at"

    ]



    # =====================================
    # RISK VARIABLES
    # =====================================

    risk_score = 0

    threats_detected = []



    # =====================================
    # HTTP CHECK
    # =====================================

    if url.startswith("http://"):

        risk_score += 25

        threats_detected.append(

            "Non-secure HTTP protocol"
        )



    # =====================================
    # DOMAIN LENGTH CHECK
    # =====================================

    if len(domain) > 30:

        risk_score += 15

        threats_detected.append(

            "Suspiciously long domain name"
        )



    # =====================================
    # SPECIAL CHARACTERS CHECK
    # =====================================

    if re.search(r"[@%]", url):

        risk_score += 20

        threats_detected.append(

            "Suspicious special characters found"
        )



    # =====================================
    # KEYWORD ANALYSIS
    # =====================================

    for keyword in suspicious_keywords:

        if keyword in url.lower():

            risk_score += 10

            threats_detected.append(

                f"Suspicious keyword detected: {keyword}"
            )



    # =====================================
    # SHORTENED URL CHECK
    # =====================================

    for short_domain in shortened_domains:

        if short_domain in domain:

            risk_score += 20

            threats_detected.append(

                "Shortened URL detected"
            )



    # =====================================
    # MULTIPLE DASHES CHECK
    # =====================================

    if domain.count("-") >= 3:

        risk_score += 15

        threats_detected.append(

            "Excessive hyphens detected"
        )



    # =====================================
    # DETERMINE STATUS
    # =====================================

    if risk_score >= 60:

        status = "danger"

        risk_level = "High"



    elif risk_score >= 30:

        status = "warning"

        risk_level = "Medium"



    else:

        status = "safe"

        risk_level = "Low"



    # =====================================
    # AI SECURITY MESSAGE
    # =====================================

    if status == "danger":

        message = """

AI Cybersecurity Analysis:

This URL appears highly suspicious and may be associated with phishing, credential theft or malicious activity.

Avoid visiting or submitting sensitive information.

"""



    elif status == "warning":

        message = """

AI Cybersecurity Analysis:

This URL contains suspicious indicators.

Proceed carefully and verify legitimacy before interacting.

"""



    else:

        message = """

AI Cybersecurity Analysis:

No major malicious indicators were detected in this URL.

The URL appears relatively safe.

"""



    # =====================================
    # RETURN RESULT
    # =====================================

    return {

        "status":
        status,

        "risk_level":
        risk_level,

        "risk_score":
        risk_score,

        "message":
        message,

        "domain":
        domain,

        "threats":
        threats_detected

    }