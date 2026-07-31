// =============================================
// Elements
// =============================================

const processButton = document.getElementById("process-btn");
const askButton = document.getElementById("ask-btn");

const youtubeInput = document.getElementById("youtube-url");
const questionInput = document.getElementById("question");

const answerBox = document.getElementById("answer-box");

const status = document.getElementById("processing-status");

const loader = document.getElementById("loader");


// =============================================
// Process Video
// =============================================

processButton.addEventListener("click", async () => {

    const url = youtubeInput.value.trim();

    if (url === "") {

        alert("Please enter a YouTube URL.");

        return;
    }

    loader.classList.remove("hidden");

    status.innerHTML = "";

    try {

        const response = await fetch("/process-video", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                youtube_url: url

            })

        });

        const data = await response.json();

loader.classList.add("hidden");

if (!response.ok) {

    status.innerHTML = "❌ " + data.detail;

    return;
}

status.innerHTML = "✅ " + data.message;

    }

    catch (error) {

        loader.classList.add("hidden");

        status.innerHTML = "❌ Failed to process video.";

        console.error(error);

    }

});


// =============================================
// Ask Question
// =============================================

askButton.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (question === "") {

        alert("Please enter a question.");

        return;

    }

    answerBox.innerHTML = "Thinking...";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                question: question

            })

        });

        const data = await response.json();

        answerBox.innerHTML = data.answer;

    }

    catch (error) {

        answerBox.innerHTML = "Error while getting answer.";

        console.error(error);

    }

});