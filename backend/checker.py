import re

# =========================================
# FAKE BREACH DATABASE
# =========================================

fake_breach_database = {

    "test@gmail.com": {

        "breaches": [
            "LinkedIn",
            "Adobe",
            "Dropbox"
        ],

        "leaked_data": [
            "Email",
            "Password",
            "Phone Number"
        ]
    },

    "admin@gmail.com": {

        "breaches": [
            "Twitter",
            "Canva"
        ],

        "leaked_data": [
            "Email",
            "Username"
        ]
    }
}



# =========================================
# EMAIL VALIDATION
# =========================================

def validate_email(email):

    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(email_regex, email)



# =========================================
# EMAIL BREACH CHECKER
# =========================================

def check_email_breach(email):

    if not validate_email(email):

        return {

            "status": "error",

            "message": "Invalid Email Format"
        }



    breach_info = fake_breach_database.get(email)



    if breach_info:

        return {

            "status": "breached",

            "email": email,

            "breaches":
            breach_info["breaches"],

            "leaked_data":
            breach_info["leaked_data"],

            "breach_count":
            len(breach_info["breaches"])
        }



    return {

        "status": "safe",

        "message": "No breach found"
    }



# =========================================
# USERNAME BREACH CHECKER
# =========================================

def check_username_breach(username):

    exposed_usernames = [

        "admin",
        "hacker123",
        "darkshadow",
        "testuser"
    ]



    if username.lower() in exposed_usernames:

        return {

            "status": "breached",

            "message":
            "Username found in leaked databases"
        }



    return {

        "status": "safe",

        "message":
        "Username not found in breaches"
    }