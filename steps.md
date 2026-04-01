# 🚀 Steps to Run AI Messaging Automation System

---

## 🖥️ Run Without Docker (Local Setup)

### 1. Clone the Repository

git clone https://github.com/satya66123/ai-messaging-system.git

cd ai-messaging-system

---

### 2. Create Virtual Environment

python -m venv .venv

Activate environment:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Configure Environment Variables

Create `.env` file in root folder:

TWILIO_ACCOUNT_SID=your_sid

TWILIO_AUTH_TOKEN=your_token

---

### 5. Add Google Credentials

* Place `credentials.json` in root directory
* First run will generate `token.json`

---

### 6. Run Application

uvicorn app.main:app --reload

---

### 7. Open in Browser

http://127.0.0.1:8000

---

## 🐳 Run With Docker

### 1. Build Docker Image

docker build -t ai-messaging-system .

---

### 2. Run Container

docker run -p 8000:8000 --env-file .env ai-messaging-system

---

### 3. Open in Browser

http://localhost:8000

---

## ⚠️ Notes

* Ensure Docker is installed and running
* `.env` file is required for credentials
* Do not commit secrets to GitHub
* Gmail OAuth must be configured before running

---

## 🧪 Testing

* Click **Run Automation** button
* Verify:

  * Email fetched
  * AI response generated
  * Status displayed

---

## ✅ Expected Output

* Email content shown
* AI-generated reply
* Status: skipped / generated

---

## 🧠 Troubleshooting

* OAuth errors → Check Google Cloud test users
* Twilio errors → Verify SID/Auth Token
* UI not loading → Check root route
* Docker issues → Ensure correct port mapping

---

## 🎯 Result

Application runs successfully with:

UI → Gmail → AI → Rules → Output

---

## 📌 Recommendation

Start with **local setup**, then move to **Docker** for deployment.
