from flask import Flask, request, jsonify
from flask_cors import CORS

import os

from dotenv import load_dotenv

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# IMPORT MODULES
# =========================================

from checker import check_email_breach
from checker import check_username_breach

from password_checker import check_password_strength

from url_scanner import scan_url

from ai_summary import generate_ai_summary

from risk_analysis import analyze_risk

# =========================================
# FLASK APP
# =========================================

app = Flask(__name__)

# =========================================
# ENABLE CORS
# =========================================

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)

# =========================================
# HOME ROUTE
# =========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "message":
        "BreachShield AI Backend Running Successfully"

    })


# =========================================
# EMAIL BREACH CHECK
# =========================================

@app.route(
    "/check_email",
    methods=["POST", "OPTIONS"]
)

def check_email():

    try:

        data = request.get_json()

        email = data.get("email")

        if not email:

            return jsonify({

                "error":
                "Email is required"

            }), 400

        result = check_email_breach(email)

        return jsonify(result)

    except Exception as error:

        return jsonify({

            "error":
            str(error)

        }), 500


# =========================================
# USERNAME CHECK
# =========================================

@app.route(
    "/check_username",
    methods=["POST", "OPTIONS"]
)

def check_username():

    try:

        data = request.get_json()

        username = data.get("username")

        if not username:

            return jsonify({

                "error":
                "Username is required"

            }), 400

        result = check_username_breach(username)

        return jsonify(result)

    except Exception as error:

        return jsonify({

            "error":
            str(error)

        }), 500


# =========================================
# PASSWORD CHECK
# =========================================

@app.route(
    "/check_password",
    methods=["POST", "OPTIONS"]
)

def check_password():

    try:

        data = request.get_json()

        password = data.get("password")

        if not password:

            return jsonify({

                "error":
                "Password is required"

            }), 400

        result = check_password_strength(password)

        return jsonify(result)

    except Exception as error:

        return jsonify({

            "error":
            str(error)

        }), 500


# =========================================
# URL SCANNER
# =========================================

@app.route(
    "/scan_url",
    methods=["POST", "OPTIONS"]
)

def url_scan():

    try:

        data = request.get_json()

        url = data.get("url")

        if not url:

            return jsonify({

                "error":
                "URL is required"

            }), 400

        result = scan_url(url)

        return jsonify(result)

    except Exception as error:

        return jsonify({

            "error":
            str(error)

        }), 500


# =========================================
# AI SUMMARY
# =========================================

@app.route(
    "/ai_summary",
    methods=["POST", "OPTIONS"]
)

def ai_summary():

    try:

        data = request.get_json()

        email = data.get("email")

        breach_count = data.get("breach_count")

        password_strength = data.get("password_strength")

        url_status = data.get("url_status")

        notes = data.get("notes")

        # =====================================
        # RISK ANALYSIS
        # =====================================

        risk_result = analyze_risk(

            breach_count,
            password_strength,
            url_status

        )

        # =====================================
        # GEMINI AI SUMMARY
        # =====================================

        ai_result = generate_ai_summary(

            email=email,

            breach_count=breach_count,

            password_strength=password_strength,

            url_status=url_status,

            notes=notes,

            risk_level=risk_result["risk_level"]

        )

        return jsonify({

            "summary":
            ai_result["summary"],

            "risk_level":
            risk_result["risk_level"],

            "threat_status":
            risk_result["threat_status"]

        })

    except Exception as error:

        return jsonify({

            "error":
            str(error)

        }), 500


# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    port = int(

        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=False
    )