document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");
    const chatApiUrl = "http://localhost:5000/api/chat"; // API endpoint

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    async function sendMessage() {
        const messageText = userInput.value.trim();
        if (messageText === "") return;

        appendMessage(messageText, "user-message");
        userInput.value = "";
        userInput.disabled = true;
        sendButton.disabled = true;

        try {
            const response = await fetch(chatApiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: messageText }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            appendMessage(data.reply, "bot-message");

        } catch (error) {
            console.error("Error sending message to API:", error);
            appendMessage("Desculpe, não consegui me conectar ao servidor. Tente novamente mais tarde.", "bot-message error-message");
        } finally {
            userInput.disabled = false;
            sendButton.disabled = false;
            userInput.focus();
        }
    }

    function appendMessage(text, className) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", className);
        const p = document.createElement("p");
        p.textContent = text;
        messageDiv.appendChild(p);
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
    }
});
