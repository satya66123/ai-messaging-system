# 🚀 AI Messaging Automation System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AI](https://img.shields.io/badge/LLM-Ollama-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Overview

AI Messaging Automation System is a full-stack intelligent application that automates email processing using AI.
It reads emails, applies rule-based logic, generates contextual responses, and optionally sends messages via WhatsApp.

This project demonstrates real-world integration of AI, APIs, and backend systems.

---

## 🧠 Key Features

* 📩 Gmail API integration (read emails)
* 🤖 AI-powered response generation (Ollama / LLaMA)
* 🧠 Rule-based decision engine
* 📲 WhatsApp messaging integration (Twilio)
* 🌐 Interactive web UI (FastAPI + HTML)
* 🔐 Secure credential management using `.env`
* 🐳 Dockerized for portability

---

## ⚙️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Backend    | FastAPI (Python)      |
| AI Engine  | Ollama (LLaMA)        |
| Email API  | Gmail API             |
| Messaging  | Twilio WhatsApp API   |
| Frontend   | HTML, CSS, JavaScript |
| Deployment | Docker                |

---

## 🔄 System Architecture

Email → Rule Engine → AI Processing → Response → UI / WhatsApp

---

## 🚀 How It Works

1. Fetch latest email from Gmail
2. Analyze content using rule engine
3. Classify email (Critical / Important / Ignore)
4. Generate AI response using LLM
5. Display result in UI or send via WhatsApp

---

## 📊 Sample Output

* Email classified as **Critical Security Alert**
* AI generates safe and contextual response
* Displayed in UI dashboard

---

## 🔐 Security Practices

* Sensitive data stored in `.env`
* Secrets removed from Git history
* Token rotation implemented
* API credentials never exposed

---

## 🧪 API Endpoints

| Endpoint            | Description                   |
| ------------------- | ----------------------------- |
| `/`                 | UI Dashboard                  |
| `/smart-automation` | Runs full automation pipeline |

---

## 🐳 Docker Support

Application is fully containerized and can run anywhere using Docker.

---

## 📈 Future Enhancements

* Database integration (logs/history)
* Multi-user authentication
* Cloud deployment (AWS / Render)
* Advanced AI classification

---

## 👨‍💻 Author

**Nekkanti Satya Srinath**

---

## 🏁 Project Status

![Completed](https://img.shields.io/badge/Status-Completed-success)

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!
