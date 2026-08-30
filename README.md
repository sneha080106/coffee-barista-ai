# ☕ Coffee Barista AI

An AI-powered coffee assistant that understands what you're in the mood for and recommends the right coffee based on your preferences.

## ✨ Features

* 🤖 AI-powered coffee recommendations
* ☕ Understands preferences like hot/cold, strong/mild, dairy-free, etc.
* 📋 Uses a structured coffee menu
* 💬 Interactive chat interface
* ⚡ Built with Google ADK and Gemini
* 🚀 Deployed on Google Cloud Run

## 🛠️ Tech Stack

* **Python**
* **Google ADK**
* **Google Gemini / Vertex AI**
* **Streamlit**
* **Google Cloud Run**

## 🔄 How It Works

```text
User Preference
      ↓
Coffee Barista AI
      ↓
Understands Requirements
      ↓
Checks Coffee Menu
      ↓
Recommends Suitable Coffee
```

## 📁 Project Structure

```text
coffee-barista-ai/
├── coffee_agent/
│   ├── agent.py
│   ├── app.py
│   ├── menu.json
│   ├── data/
│   │   └── menu.txt
│   ├── requirements.txt
│   └── __init__.py
├── .gitignore
└── README.md
```

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/sneha080106/coffee-barista-ai.git
cd coffee-barista-ai
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r coffee_agent/requirements.txt
```

Run the application:

```bash
cd coffee_agent
streamlit run app.py
```

## 🌐 Live Demo

[Coffee Barista AI](https://coffee-ai-agent-nspw2mpfha-uc.a.run.app)

## 🎯 Project Goal

The goal of Coffee Barista AI is to provide a simple conversational experience for discovering coffee recommendations based on natural-language preferences.

---

**Built with ☕ + AI**

