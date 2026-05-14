// =====================================
// RENDER BACKEND URL
// =====================================

const BASE_URL =
"https://breachshield-backend.onrender.com";



// =====================================
// SHOW FORM SECTION
// =====================================

function showFormSection() {

    const mainSection =
    document.getElementById("mainSection");

    mainSection.style.display = "block";

    mainSection.scrollIntoView({

        behavior: "smooth",
        block: "start"
    });
}



// =====================================
// GENERATE FULL AI REPORT
// =====================================

async function generateFullReport() {

    const email =
    document.getElementById("emailInput").value;

    const username =
    document.getElementById("usernameInput").value;

    const password =
    document.getElementById("passwordInput").value;

    const url =
    document.getElementById("urlInput").value;

    const notes =
    document.getElementById("notesInput").value;



    const loadingGif =
    document.getElementById("loadingGif");

    const dynamicResults =
    document.getElementById("dynamicResults");



    // =====================================
    // VALIDATION
    // =====================================

    if (

        email === "" ||

        username === "" ||

        password === "" ||

        url === ""

    ) {

        alert(
            "Please fill all required fields."
        );

        return;
    }



    // =====================================
    // SHOW LOADING
    // =====================================

    loadingGif.style.display =
    "inline-block";

    dynamicResults.innerHTML = "";



    try {

        // =====================================
        // EMAIL CHECK
        // =====================================

        const emailResponse = await fetch(

            `${BASE_URL}/check_email`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    email: email
                })
            }
        );

        const emailData =
        await emailResponse.json();



        // =====================================
        // USERNAME CHECK
        // =====================================

        const usernameResponse = await fetch(

            `${BASE_URL}/check_username`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    username: username
                })
            }
        );

        const usernameData =
        await usernameResponse.json();



        // =====================================
        // PASSWORD CHECK
        // =====================================

        const passwordResponse = await fetch(

            `${BASE_URL}/check_password`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    password: password
                })
            }
        );

        const passwordData =
        await passwordResponse.json();



        // =====================================
        // URL SCAN
        // =====================================

        const urlResponse = await fetch(

            `${BASE_URL}/scan_url`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    url: url
                })
            }
        );

        const urlData =
        await urlResponse.json();



        // =====================================
        // AI SUMMARY
        // =====================================

        const aiResponse = await fetch(

            `${BASE_URL}/ai_summary`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    email: email,

                    breach_count:
                    emailData.breach_count,

                    password_strength:
                    passwordData.password_strength,

                    url_status:
                    urlData.status,

                    notes: notes
                })
            }
        );

        const aiData =
        await aiResponse.json();



        // =====================================
        // HIDE LOADING
        // =====================================

        loadingGif.style.display =
        "none";



        // =====================================
        // DISPLAY RESULTS
        // =====================================

        dynamicResults.innerHTML = `

        <div class="results-section">

            <div class="result-card">

                <h3>Email Breach Analysis</h3>

                <p>

                    <strong>Status:</strong>
                    ${emailData.status}

                    <br><br>

                    <strong>Breaches:</strong>

                    <br>

                    ${emailData.breaches.join("<br>")}

                </p>

            </div>



            <div class="result-card">

                <h3>Username Exposure</h3>

                <p>

                    ${usernameData.message}

                </p>

            </div>



            <div class="result-card">

                <h3>Password Security</h3>

                <p>

                    <strong>Strength:</strong>

                    ${passwordData.password_strength}

                    <br><br>

                    <strong>Risk:</strong>

                    ${passwordData.risk}

                </p>

            </div>



            <div class="result-card">

                <h3>URL Threat Analysis</h3>

                <p>

                    <strong>Status:</strong>

                    ${urlData.status}

                    <br><br>

                    <strong>Risk Level:</strong>

                    ${urlData.risk_level}

                </p>

            </div>



            <div class="result-card full-width">

                <h3>AI Cybersecurity Summary</h3>

                <p>

                    ${aiData.summary.replace(/\n/g,"<br>")}

                </p>

            </div>

        </div>

        `;
    }



    // =====================================
    // ERROR HANDLING
    // =====================================

    catch(error) {

        console.log(error);

        loadingGif.style.display =
        "none";



        dynamicResults.innerHTML = `

        <div class="result-card">

            <h3>Backend Error</h3>

            <p>

                Unable to connect with
                AI backend server.

                <br><br>

                Please make sure Render
                deployment is live.

            </p>

        </div>

        `;
    }
}