# Currency Converter Chatbot

A Telegram chatbot that converts currency values in real time using natural language inputs. Built using Google's Dialogflow for Natural Language Understanding (NLU), Flask for the backend API, and a currency exchange API to fetch live rates.

---

## 🖥️ User Interface Overview

The user interface is a Telegram chatbot that accepts natural language inputs like `Convert 100 USD to INR` and responds instantly with the converted amount, providing a simple and intuitive experience without requiring any graphical UI.

![image](https://github.com/user-attachments/assets/1c9f2bf8-5351-4b61-b47c-20b83e9dd8ba)

---

## 🎬 Project Demonstration

**User Input on Telegram:**
```bash
# Some sample inputs are:

Convert 100 USD to INR
How much is a euro worth in Indian rupees?
How much is one franc in euros?
I need to convert 20 pounds into dollars
How much is 100 dollars in Indian rupees?
Convert ten thousand won to rupees
```

**Bot Response:**
```bash
#Some sample examples are:

Quick math coming up! 100.0 USD will be 8593.59 INR. Let me know if you need a historical rate too!
1.0 USD will be 0.86 EUR
Absolutely! 100.0 USD will be 8593.59 INR. Anything else you want to convert?
Here’s the conversion: 10000.0 KRW will be 619.87 INR. Want to compare with another currency?
```

---

## 🧩 Architectural Design

The architecture illustrates a Telegram chatbot integrated with Dialogflow for NLU and a Flask backend for real-time currency conversion. Dialogflow communicates with the backend via webhook (exposed using Ngrok) and returns responses back to the user through the Telegram interface.

![image](https://github.com/user-attachments/assets/ac147a19-9a34-486b-92ef-0456dea68455)

---

## 🚀 Features

- 🌍 Real-time currency conversion
- 🧠 Natural language understanding using Dialogflow
- 🤖 Telegram bot interface
- 🌐 Flask backend with API integration
- 🔄 Ngrok tunneling for local development with Dialogflow webhooks

---

## 🔍 How It Works

- **User Interaction**: The user sends a natural language query (e.g., `Convert 100 USD to INR`) through the Telegram Bot.
- **Intent Recognition (Dialogflow)**: The query is sent to Dialogflow, which detects the user’s intent (e.g., `currency conversion`) and extracts relevant entities:
    - `unit-currency`: Contains the amount and the base currency (e.g., `100 USD`).
    - `currency-name`: Contains the target currency (e.g., `INR`).
- **Webhook Call to Backend**: For conversion queries, Dialogflow triggers a webhook that sends a POST request to the Flask backend (exposed via Ngrok during local development).
- **Currency Conversion Logic**: The Flask backend uses a Currency Exchange API (e.g., `Freecurrencyapi`) to fetch live exchange rates and performs the conversion.
- **Response Flow**: The converted amount is returned as a webhook response to Dialogflow, which then sends it back to the Telegram Bot interface, completing the loop.
  
---

## 🛠️ Tech Stack

- **Frontend / Bot Interface**: Telegram Bot
- **Natural Language Understanding**: [Dialogflow](https://dialogflow.cloud.google.com/)
- **Backend**: Python Flask
- **API for Currency Conversion**: [Freecurrencyapi](https://freecurrencyapi.com/)
- **Tunneling**: [Ngrok](https://ngrok.com/)

---

## 🛠️ Setup Instructions

Follow these steps to set up the Currency Converter Telegram Chatbot locally:

### 1. 🧾 Clone the Repository
```bash
git clone https://github.com/Sayan-Mondal2022/currency_converter.git
cd currency_converter
```

### 2. 🐍 Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🔑 Setup Environment Variables
Create a `.env` file in the root directory and add the following:
```bash
API_KEY=your_currency_api_key
```

### 5. 🧠 Setup Dialogflow

- Go to Dialogflow Console.
- Create a new agent (or use an existing one).
- Define intents (e.g., `CurrencyConversionIntent`).

Set up entities:
- unit-currency (e.g., `100 USD`)
- currency-name (e.g., `INR`)
In the Fulfillment section, enable Webhook and paste the Ngrok URL (from next step).

### 6. 🚀 Start Flask Server
```bash
python app.py
```

### 7. 🌐 Expose Localhost with Ngrok
In a **new terminal**, run *After installing ngrok*:
```bash
ngrok http 5000
```

Copy the HTTPS URL and update your Dialogflow webhook URL with:
```bash
https://<your-ngrok-subdomain>.ngrok.io/webhook
```

### 8. 💬 Connect Telegram Bot
- Open Telegram and search for @BotFather.
- Create a new bot and copy the token.
- Set the webhook in your Flask app to use this token.
- Start chatting with your bot!

### ✅ You're all set!
Send messages like:
```bash
Convert 100 USD to INR
How much is 50 EUR in GBP?
```

---

## 🗂️ Project Structure

```bash
currency-converter-chatbot/
│
├── .gitignore                   # Git ignore rules (should include .venv, .env, __pycache__)
├── app.py                       # Main Flask application handling webhook logic
├── architecture_diagram.png     # Contains Project architectural diagram.
├── convert.py                   # Handling the currency conversion by connecting with the Currency API
├── requirements.txt             # List of Python dependencies
└── README.md                    # Project documentation
```

---

## 🙏 Acknowledgement

I would like to express my sincere gratitude to the following platforms and tools that made this project possible:

- [Google Dialogflow](https://dialogflow.cloud.google.com/) – for providing powerful NLU capabilities.
- [Telegram Bot API](https://core.telegram.org/bots/api) – for enabling smooth bot communication.
- [Python Flask](https://flask.palletsprojects.com/en/stable/) – for building a lightweight backend server.
- [Ngrok](https://ngrok.com/) – for exposing local servers securely to the web.
- [Freecurrencyapi](https://freecurrencyapi.com/) – for providing real-time currency exchange data.

Special thanks to the open-source community for documentation, examples, and inspiration.

---
