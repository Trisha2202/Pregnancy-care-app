function saveMood() {
  let mood = document.getElementById("mood").value;
  let result = document.getElementById("result");

  if (mood === "Sad" || mood === "Stressed") {
    result.innerHTML = "💙 It's okay. Consider talking to someone you trust.";
  } else {
    result.innerHTML = "😊 Thank you for sharing your mood!";
  }
}
function checkSafety() {
    const age = document.getElementById('babyAge').value;
    const item = document.getElementById('searchItem').value.trim().toLowerCase();
    const resultDiv = document.getElementById('result');

    if(!age) {
        alert("Please select baby's age!");
        return;
    }
    if(!item) {
        alert("Please enter an item to search!");
        return;
    }

    const safeItems = babySafetyData[age].safe;
    const unsafeItems = babySafetyData[age].unsafe;

    // Check if any safe item includes the searched text
    const isSafe = safeItems.find(i => i.includes(item));
    const isUnsafe = unsafeItems.find(i => i.includes(item));

    if(isSafe) {
        resultDiv.style.color = "green";
        resultDiv.textContent = `✅ "${item}" is SAFE for a baby aged ${age} months.`;
    } else if(isUnsafe) {
        resultDiv.style.color = "red";
        resultDiv.textContent = `❌ "${item}" is NOT SAFE for a baby aged ${age} months.`;
    } else {
        resultDiv.style.color = "orange";
        resultDiv.textContent = `⚠️ Safety information for "${item}" is not available.`;
    }
}
async function sendMessage() {
    const userMessage = document.getElementById('userInput').value;
    if(!userMessage) return;

async function sendMessage() {
    const userInput = document.getElementById("userInput");
    const language = document.getElementById("language").value;
    const message = userInput.value.trim();

    if (message === "") return;

    addMessage(message, "user");
    userInput.value = "";

    try {
        const response = await fetch("https://pregnancy-care-app.onrender.com/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                language: language
            })
        });

        if (!response.ok) {
            addMessage("⚠️ Server error. Please try again.", "bot");
            return;
        }

        const data = await response.json();
        addMessage(data.reply, "bot");

    } catch (error) {
        addMessage("❌ Cannot connect to server. Please start backend.", "bot");
        console.error(error);
    }
}