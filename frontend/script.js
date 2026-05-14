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
// GENERATE REPORT
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



    loadingGif.style.display = "inline-block";

    dynamicResults.innerHTML = "";



    try {

        // EMAIL

        const emailResponse = await fetch(

            "http://127.0.0.1:5000/check_email",

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



        // USERNAME

        const usernameResponse = await fetch(

            "http://127.0.0.1:5000/check_username",

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



        // PASSWORD

        const passwordResponse = await fetch(

            "http://127.0.0.1:5000/check_password",

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



        // URL

        const urlResponse = await fetch(

            "http://127.0.0.1:5000/scan_url",

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



        // AI SUMMARY

        const aiResponse = await fetch(

            "http://127.0.0.1:5000/ai_summary",

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



        loadingGif.style.display = "none";



        // RESULTS

        dynamicResults.innerHTML = `

        <div class="results-section">

            <div class="result-card">

                <h3>Email Breach Checker</h3>

                <p>

                    ${emailData.status}

                    <br><br>

                    ${emailData.breaches.join("<br>")}

                </p>

            </div>



            <div class="result-card">

                <h3>Password Security</h3>

                <p>

                    ${passwordData.password_strength}

                </p>

            </div>



            <div class="result-card full-width">

                <h3>AI Security Summary</h3>

                <p>

                    ${aiData.summary.replace(/\n/g,"<br>")}

                </p>

            </div>

        </div>

        `;

    }

    catch(error) {

        loadingGif.style.display = "none";



        dynamicResults.innerHTML = `

        <div class="result-card">

            <h3>Backend Error</h3>

            <p>

                Backend server is not running.

            </p>

        </div>

        `;
    }
}