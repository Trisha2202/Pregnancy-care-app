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

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    const chatBox = document.getElementById('chatBox');
    chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatBox.innerHTML += `<p><strong>AI:</strong> ${data.reply}</p>`;
    document.getElementById('userInput').value = "";
}