@app.route('/chatbot', methods=['GET'])
def chatbot_page():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
            }
            #chat-container {
                width: 350px;
                height: 500px;
                border: 1px solid #ddd;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                padding: 10px;
            }
        </style>
    </head>
    <body>
        <div id="chat-container">
            <h3>Welcome to the Chatbot</h3>
            <p>Type your message below:</p>
            <input type="text" id="user-input" placeholder="Say something..." />
            <button onclick="sendMessage()">Send</button>
            <p id="response"></p>

            <script>
                async function sendMessage() {
                    const userInput = document.getElementById("user-input").value;
                    const responseArea = document.getElementById("response");

                    const response = await fetch("https://chatbot-theoneitappears-im-using.onrender.com/chat", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ user_id: "123456", message: userInput })
                    });

                    const data = await response.json();
                    responseArea.innerHTML = data.response || "Error: Could not get a response";
                }
            </script>
        </div>
    </body>
    </html>
    '''
