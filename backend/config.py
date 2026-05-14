import os
from dotenv import load_dotenv

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# FLASK CONFIGURATION
# =========================================

class Config:

    # =====================================
    # BASIC SETTINGS
    # =====================================

    SECRET_KEY = os.getenv(

        "SECRET_KEY",

        "breachshield_ai_secret"
    )



    DEBUG = os.getenv(

        "DEBUG",

        "True"
    ) == "True"



    # =====================================
    # SERVER SETTINGS
    # =====================================

    HOST = os.getenv(

        "HOST",

        "0.0.0.0"
    )



    PORT = int(

        os.getenv(

            "PORT",

            5000
        )
    )



    # =====================================
    # GEMINI AI SETTINGS
    # =====================================

    GEMINI_API_KEY = os.getenv(

        "GEMINI_API_KEY"
    )



    GEMINI_MODEL = os.getenv(

        "GEMINI_MODEL",

        "gemini-1.5-flash"
    )



    # =====================================
    # REPORT SETTINGS
    # =====================================

    REPORT_FOLDER = os.getenv(

        "REPORT_FOLDER",

        "reports"
    )



    # CREATE REPORT DIRECTORY

    if not os.path.exists(

        REPORT_FOLDER
    ):

        os.makedirs(

            REPORT_FOLDER
        )



    # =====================================
    # ALLOWED FRONTEND ORIGINS
    # =====================================

    ALLOWED_ORIGINS = [

        "http://127.0.0.1:5500",

        "http://localhost:5500",

        "http://127.0.0.1:3000",

        "http://localhost:3000"
    ]



    # =====================================
    # CYBERSECURITY SETTINGS
    # =====================================

    MAX_URL_LENGTH = 500

    MAX_PASSWORD_LENGTH = 128

    MAX_USERNAME_LENGTH = 50



    # =====================================
    # AI SECURITY SETTINGS
    # =====================================

    AI_REPORT_MAX_TOKENS = 2048

    AI_TEMPERATURE = 0.7



    # =====================================
    # THREAT KEYWORDS
    # =====================================

    SUSPICIOUS_KEYWORDS = [

        "login",

        "verify",

        "secure",

        "bonus",

        "free",

        "gift",

        "wallet",

        "banking",

        "paypal",

        "update",

        "crypto",

        "account"
    ]



    # =====================================
    # SHORTENED URL SERVICES
    # =====================================

    SHORTENED_URLS = [

        "bit.ly",

        "tinyurl.com",

        "goo.gl",

        "t.co",

        "shorturl.at"
    ]



    # =====================================
    # COMMON WEAK PASSWORDS
    # =====================================

    COMMON_PASSWORDS = [

        "123456",

        "password",

        "password123",

        "admin",

        "qwerty",

        "welcome",

        "abc123"
    ]



# =========================================
# EXPORT CONFIG
# =========================================

config = Config()