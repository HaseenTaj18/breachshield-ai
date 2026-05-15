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
# FULL CORS FIX
# =========================================

CORS(
    app,
    supports_credentials=True
)

# =========================================
# HOME ROUTE
# =========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "status": "success",

        "message":
        "BreachShield AI Backend Running"

    })


# =========================================
# EMAIL CHECK
# =========================================

@app.route("/check_email", methods=["POST"])
def check_email():

    try:

        data = request.get_json()

        email = data.get("email", "")

        result = check_email_breach(email)

        return jsonify(result)

    except Exception as error:

        print(error)

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# =========================================
# USERNAME CHECK
# =========================================

@app.route("/check_username", methods=["POST"])
def check_username():

    try:

        data = request.get_json()

        username = data.get("username", "")

        result = check_username_breach(username)

        return jsonify(result)

    except Exception as error:

        print(error)

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# =========================================
# PASSWORD CHECK
# =========================================

@app.route("/check_password", methods=["POST"])
def check_password():

    try:

        data = request.get_json()

        password = data.get("password", "")

        result = check_password_strength(password)

        return jsonify(result)

    except Exception as error:

        print(error)

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# =========================================
# URL SCAN
# =========================================

@app.route("/scan_url", methods=["POST"])
def url_scan():

    try:

        data = request.get_json()

        url = data.get("url", "")

        result = scan_url(url)

        return jsonify(result)

    except Exception as error:

        print(error)

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# =========================================
# AI SUMMARY
# =========================================

@app.route("/ai_summary", methods=["POST"])
def ai_summary():

    try:

        data = request.get_json()

        email = data.get("email", "")

        breach_count = data.get("breach_count", 0)

        password_strength = data.get(
            "password_strength",
            "Unknown"
        )

        url_status = data.get(
            "url_status",
            "Unknown"
        )

        notes = data.get("notes", "")

        # =====================================
        # RISK ANALYSIS
        # =====================================

        risk_result = analyze_risk(

            breach_count,

            password_strength,

            url_status

        )

        # =====================================
        # AI SUMMARY
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

            "status": "success",

            "summary":
            ai_result["summary"],

            "risk_level":
            risk_result["risk_level"],

            "threat_status":
            risk_result["threat_status"]

        })

    except Exception as error:

        print(error)

        return jsonify({

            "status": "error",

            "message": str(error)

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