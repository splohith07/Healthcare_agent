async function askAgent() {
    let question = document.getElementById("userInput").value;

    console.log("Sending question:", question);

    let response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })   // IMPORTANT!!
    });

    let data = await response.json();
    console.log("Server replied:", data);

    document.getElementById("responseBox").innerText = data.answer;
}
